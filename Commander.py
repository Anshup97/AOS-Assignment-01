from concurrent import futures
import logging
import time
import grpc
import battle_pb2
import battle_pb2_grpc
import SoldierClient_pb2
import SoldierClient_pb2_grpc
import random
import Soldier


class Battle(battle_pb2_grpc.BattleServicer):
    commanderId = 0
    x_coord = -1234
    y_coord = -1234
    N = 0
    M = 0
    T = 0
    t = 0
    soldiersList = []
    matrix = [[]]

    def SendGameDetails(self, request, context):
        self.T = request.T
        self.N = request.N
        self.M = request.M
        self.t = request.t
        return battle_pb2.GameDetailsReply(message="Game Details Received!!")
    
    def createSoldiers(self):
        N = self.N
        matrix = [["-" for i in range(self.N)] for j in range(self.N)]
        M = self.M
        noOfZeros = len(str(M))
        portNo = 50052
        for i in range(1, M+1):
            row = random.randint(0, N-1)
            col = random.randint(0, N-1)
            while matrix[row][col] != "-":
                row = random.randint(0, N-1)
                col = random.randint(0, N-1)
            id = ("S" + "0"*(noOfZeros-len(str(i))) + str(i)) if i < pow(10, noOfZeros) else ("S" + str(i))
            matrix[row][col] = id
            soldier = Soldier(id, random.randint(0, 4), (row, col), True, portNo)
            self.soldiersList.append(soldier)
            portNo += 1
        self.matrix = matrix

    def SoldierReady(self, request, context):
        for i in range(self.T):
            yield SoldierClient_pb2.MissileApproachingReply(x_coordinate=self.x_coord, y_coordinate=self.y_coord)
            time.sleep(self.t)

    # def missile_approaching(self, request, context):
    #     with grpc.insecure_channel("localhost:50052") as channel:
    #         stub = SoldierClient_pb2_grpc.SoldierClientStub(channel)
    #         response = stub.missile_approaching(SoldierClient_pb2.MissileApproachingRequest(x_coordinate=self.x_coord, y_coordinate=self.y_coord))
    #         print("Soldier client received: " + str(response.x_coordinate) + " " + str(response.y_coordinate))
    #         return
        
    def missile_launched(self, request, context):
        self.x_coord = request.x_coordinate
        self.y_coord = request.y_coordinate
        self.SoldierReady(request, context)
        return battle_pb2.MissileLaunchReply(message="Missile Launched!!! \n X-axis = " + 
                                             str(request.x_coordinate) + " Y-axis = " + str(request.y_coordinate))

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
