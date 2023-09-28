from concurrent import futures
import logging
import random

import grpc
import battle_pb2
import battle_pb2_grpc

class Soldier:
    def __init__(self, soldierId, speed, position, status):
        self.soldierId = soldierId
        self.speed = speed
        self.position = position
        self.status = status

class Soldiers(battle_pb2_grpc.BattleServicer):
    #Game Details
    N = 0
    M = 0
    T = 0
    t = 0
    matrix = []
    soldiersList = []
    commanderId = ""

    
    #Receives game details from Commander and creates soldier clients.
    def SendGameDetailsToSoldiers(self, request, context):
        Soldiers.N = request.N
        Soldiers.M = request.M
        Soldiers.T = request.T
        Soldiers.t = request.t
        Soldiers.createSoldiers()
        return battle_pb2.GameDetailsReply(message="Soldiers Received Game Details (N, M, T, t).")
    
    #Create 'M' number of Soldier clients and initializes the soldier matrix which is used throughout the battle.
    def createSoldiers():
        N = Soldiers.N
        M = Soldiers.M
        matrix = [["-" for i in range(N)] for j in range(N)]
        soldiersList = []
        noOfZeros = len(str(M))
        for i in range(1, M+1):
            row = random.randint(0, N-1)
            col = random.randint(0, N-1)
            while matrix[row][col] != "-":
                row = random.randint(0, N-1)
                col = random.randint(0, N-1)
            id = ("S" + "0"*(noOfZeros-len(str(i))) + str(i)) if i < pow(10, noOfZeros) else ("S" + str(i))
            matrix[row][col] = id
            soldier = Soldier(id, random.randint(0, 4), (row, col), True)
            soldiersList.append(soldier)
        Soldiers.matrix = matrix
        Soldiers.soldiersList = soldiersList
        Soldiers.sendMatrix(matrix)
        Soldiers.setCommander()

    #Sends updated matrix to the Commander.
    def sendMatrix(matrix):
        with grpc.insecure_channel("localhost:50051") as channel:
            stub = battle_pb2_grpc.BattleStub(channel)
            protoMat = []
            N = Soldiers.N
            for i in range(N):
                ro = []
                for j in range(N):
                    val = battle_pb2.MatrixValues(value=matrix[i][j])
                    ro.append(val)
                protoRow = battle_pb2.MatrixRows(row=ro)
                protoMat.append(protoRow)
            response = stub.SetSoldierMatrix(battle_pb2.Matrix(matrix=protoMat))
            print(response.message)
        return
    
    #Receives missile type and missile coordinates from Commander.
    def missile_approaching(self, request, context):
        for soldier in Soldiers.soldiersList:
            Soldiers.matrix = Soldiers.evasive_action(soldier, (request.x_coordinate, request.y_coordinate),
                                            request.missile_type,Soldiers.N,Soldiers.matrix,Soldiers.M)
        Soldiers.sendMatrix(Soldiers.matrix)
        for i in Soldiers.soldiersList:
            if i.soldierId == Soldiers.commanderId and i.status == False:
                Soldiers.setCommander()
        return battle_pb2.MissileApproachingReply(message="Missile Coordinates Received!!")

    #Take shelter function of soldier.
    def evasive_action(soldier, missile_coordinates,missile_type,N,matrix,M):
        if soldier.status == False:
            return matrix
        soldier_x=soldier.position[0]
        soldier_y=soldier.position[1]
        soldier_speed = soldier.speed
        permissible_cells=[]
        affected_coordinates=calculate_missile_radius(N,missile_type,missile_coordinates)
        flag=0
        if soldier.position in affected_coordinates:
                        for i in range(soldier_x-soldier_speed,soldier_x+soldier_speed+1):
                             for j in range(soldier_y-soldier_speed,soldier_y+soldier_speed+1):
                                    if i>=0 and i<=N-1 and j>=0 and j<=N-1:
                                        permissible_cells.append((i,j))
                        for i in range(0,len(permissible_cells)):
                            x=permissible_cells[i][0]
                            y=permissible_cells[i][1]
                            pos=(x,y)
                            if pos not in affected_coordinates and (matrix[x][y]=='-' or matrix[x][y] == "*"*(len(str(M))+1)):
                                dx=x
                                dy=y
                                flag=1
                                break
                        if flag == 1:
                            matrix[dx][dy]= soldier.soldierId
                            matrix[soldier_x][soldier_y] = "-"
                            for sol in Soldiers.soldiersList:
                                if sol.soldierId == soldier.soldierId:
                                    sol.position = (dx,dy)
                            
                            
                        else:
                            for sol in Soldiers.soldiersList:
                                if sol.soldierId == soldier.soldierId:
                                    sol.status = False
                            matrix[soldier_x][soldier_y] = "-"
        return matrix
    
    #Sends new commander details in the beginning of battle or in case of election.
    def setCommander():
        commander = random.choice(Soldiers.soldiersList)
        Soldiers.commanderId = commander.soldierId
        with grpc.insecure_channel("localhost:50051") as channel:
            stub = battle_pb2_grpc.BattleStub(channel)
            response = stub.SetCommander(battle_pb2.CommanderRequest(commanderId=commander.soldierId))
            print(response.message)
        return
    
    #Returns status of individual soldier.
    def status(self, request, context):
        for i in Soldiers.soldiersList:
            if i.soldierId == request.soldierId:
                return battle_pb2.SoldierStatus(isAlive=i.status)
        return battle_pb2.SoldierStatus(isAlive=False)
    
    #Returns status of all soldiers dead or alive.
    def status_all(self, request, context):
        statuses1 = ""
        for i in Soldiers.soldiersList:
            statuses1 += (str(i.status) + " ")
        return battle_pb2.SoldierStatusAllReply(statuses=statuses1)

        
#Prints matrix.
def printLayout(matrix, N, M):
    noOfSpaces = len(str(M))+1
    for i in range(N):
        for j in range(N):
            if matrix[i][j]=="-":
                print(matrix[i][j], end=" "*noOfSpaces)
            else:
                print(matrix[i][j], end=" ") 
        print("")

#Calculates all the coordinates in the dead zone.
def calculate_missile_radius(N, missile_type, position):
    x = position[0]
    y = position[1]
    list_of_coordinates_affected = []
    if missile_type == "M1":
        list_of_coordinates_affected.append((x, y))
        return list_of_coordinates_affected
    else:
        missile_type_number = int(missile_type[1])
        row1 = x - (missile_type_number-1)
        row2 = x + (missile_type_number-1)
        col1 = y - (missile_type_number-1)
        col2 = y + (missile_type_number-1)
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                if i>=0 and i<=N-1 and j>=0 and j<=N-1:
                    list_of_coordinates_affected.append((i, j))
            
        return list_of_coordinates_affected

            
def serve():
    port = "50052"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    battle_pb2_grpc.add_BattleServicer_to_server(Soldiers(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
