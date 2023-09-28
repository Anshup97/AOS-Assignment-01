from concurrent import futures
import logging

import time

import grpc
import battle_pb2
import battle_pb2_grpc
import logging

class Battle(battle_pb2_grpc.BattleServicer):
    #Battle details received from User.
    N = 0
    M = 0
    T = 0
    t = 0

    #Matrix passed between commander, soldier and user.
    matrix = []
    matrixSet = False
    matrixRequest = 0
    x_coordinates = -1234
    y_coordinates = -1234
    missile_type = ""
    missileLaunched = False
    commanderId = ""

    #Receive battle details from User and sending it to the users.
    def SendGameDetails(self, request, context):
        Battle.N = request.N
        Battle.M = request.M
        Battle.T = request.T
        Battle.t = request.t
        with grpc.insecure_channel("localhost:50052") as channel:
            stub = battle_pb2_grpc.BattleStub(channel)
            response = stub.SendGameDetailsToSoldiers(battle_pb2.GameDetailsRequest(N=Battle.N, M=Battle.M, T=Battle.T, t=Battle.t))
            print(response.message)
        return battle_pb2.GameDetailsReply(message="Game Details Received By Commander.!!!")
    
    #Receive updated matrix from soldiers.
    def SetSoldierMatrix(self, request, context):
        Battle.matrixSet = True
        Battle.matrixRequest = request.matrix
        n = Battle.N
        matrix1 = []
        for i in request.matrix:
            matrix1.append(list(i.row))
        Battle.matrix = [["-" for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                Battle.matrix[i][j] = matrix1[i][j].value
        return battle_pb2.MatrixRequest(message="Received Updated Matrix from Soldiers...")
    
    #Sends matrix to the user.
    def GetSoldierMatrix(self, request, context):
        protoMat = []
        N = Battle.N
        while Battle.matrixSet == False:
            time.sleep(1)
        for i in range(N):
            ro = []
            for j in range(N):
                val = battle_pb2.MatrixValues(value=Battle.matrix[i][j])
                ro.append(val)
            protoRow = battle_pb2.MatrixRows(row=ro)
            protoMat.append(protoRow)
        Battle.matrixSet = False
        return battle_pb2.Matrix(matrix=protoMat)
    
    #Set commander initially and after elections.
    def SetCommander(self, request, context):
        Battle.commanderId = request.commanderId
        return battle_pb2.CommanderReply(message="Commander Set to " + Battle.commanderId)
    
    #Used by client to get commander information.
    def GetCommander(self, request, context):
        return battle_pb2.GetCommanderReply(commanderId=Battle.commanderId)
    
    #Missile type and coordinates received from user.
    def missile_launched(self, request, context):
        print(request.missile_type, request.x_coordinate, request.y_coordinate)
        Battle.missile_type = request.missile_type
        Battle.x_coordinates = request.x_coordinate
        Battle.y_coordinates = request.y_coordinate
        Battle.missile_approaching_soldiers(request.missile_type, (request.x_coordinate, request.y_coordinate))
        return battle_pb2.MissileLaunchedReply(message="Commander received the coordinates from user!!!")
    
    #Sends missile coordinates to soldiers.
    def missile_approaching_soldiers(missile_typ, missile_coordinates):
        with grpc.insecure_channel("localhost:50052") as channel:
            stub = battle_pb2_grpc.BattleStub(channel)
            response = stub.missile_approaching(battle_pb2.MissileApproachingRequest(missile_type=missile_typ,
                                                                                    x_coordinate=missile_coordinates[0],
                                                                                    y_coordinate=missile_coordinates[1]))
            print(response.message)
        return
    
    #Gets status of all soldiers.
    def status_all(self, request, context):
        with grpc.insecure_channel("localhost:50052") as channel:
            stub = battle_pb2_grpc.BattleStub(channel)
            response = stub.status_all(battle_pb2.SoldierStatusAllRequest(message="Send status of all soldiers."))
            return battle_pb2.SoldierStatusAllReply(statuses=response.statuses)


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    battle_pb2_grpc.add_BattleServicer_to_server(Battle(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
