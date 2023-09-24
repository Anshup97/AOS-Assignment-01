from concurrent import futures
import logging
import time
import grpc
import battle_pb2
import battle_pb2_grpc
import SoldierClient_pb2
import SoldierClient_pb2_grpc


class Battle(battle_pb2_grpc.BattleServicer):
    x_coord = 0
    y_coord = 0

    def SoldierReady(self, request, context):
        hello_reply = SoldierClient_pb2.MissileApproachingReply(x_coordinate=self.x_coord
                                                                , y_coordinate=self.y_coord)
        yield hello_reply
        return

    def missile_approaching(self, request, context):
        with grpc.insecure_channel("localhost:50052") as channel:
            stub = SoldierClient_pb2_grpc.SoldierClientStub(channel)
            response = stub.missile_approaching(SoldierClient_pb2.MissileApproachingRequest(x_coordinate=self.x_coord, y_coordinate=self.y_coord))
            print("Soldier client received: " + str(response.x_coordinate) + " " + str(response.y_coordinate))
            return
        
    def missile_launched(self, request, context):
        self.x_coord = request.x_coordinate
        self.y_coord = request.y_coordinate
        self.missile_approaching(request, context)
        return battle_pb2.MissileLaunchReply(message="Missile Lauched!!! \n X-axis = " + 
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
