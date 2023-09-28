import logging
import random

import grpc
import time

import battle_pb2
import battle_pb2_grpc

#Prints N X N Matrix.
def printLayout(matrix, N, M):
    noOfSpaces = len(str(M))+1
    for i in range(N):
        for j in range(N):
            if matrix[i][j]=="-":
                print(matrix[i][j], end=" "*noOfSpaces)
            else:
                print(matrix[i][j], end=" ") 
        print("")

def run():

    # Input Matrix Size
    N = int(input('Enter size of the matrix(N): '))
    # matrix = [["-" for i in range(N)] for j in range(N)]

    # Input Soldiers.
    M = int(input('Enter the no. of soldiers: '))
    while M > N*N:
        print("Wrong number of soldiers. Please enter a number less than N*N.")
        M = int(input('Enter the no. of soldiers: '))

    # Input total game time and time between each missile launch.
    T = int(input('Enter the duration of the battle (in secs): '))
    t = int(input('Enter the time gap between two missile launches(in secs): '))

    with grpc.insecure_channel("localhost:50051") as channel:
            stub = battle_pb2_grpc.BattleStub(channel)
            #Sending Game Details to the Commander.
            request = battle_pb2.GameDetailsRequest(N=N, M=M, T=T, t=t)
            response = stub.SendGameDetails(request)
            print("\nInitial posititons of soldiers\n\n")
            print("<------------------------------------------------------------------------------------------------------>")
            print("\n\n")
            # Get the soldier matrix from Commander server.
            response = stub.GetSoldierMatrix(battle_pb2.MatrixRequest(message="Get Soldier Matrix!!"))
            #Get Commander Details.
            commanderResponse = stub.GetCommander(battle_pb2.GetCommanderRequest(message="Who is the Commander?"))
            n = N
            #De-serializing the matrix received from Commander. 
            matrix1 = []
            for i in response.matrix:
                matrix1.append(list(i.row)) 
            matrix = [["-" for i in range(n)] for j in range(n)]
            for i in range(n):
                for j in range(n):
                    matrix[i][j] = matrix1[i][j].value 
            printLayout(matrix, N, M)
            print("\n" + commanderResponse.commanderId + " is the commander.\n\n")
            while T >= t:
                temp = t
                #User Inputs the missile type and coordinates to launch.
                missile_typ = input('Enter type of missile to fire: ')
                x_axis, y_axis = map(int, input('Enter the coordinates for missile launch:').split(' '))
                print(missile_typ, (x_axis, y_axis))
                stub = battle_pb2_grpc.BattleStub(channel)
                #Intimate the commander missile has been lauched and send missile details.
                response = stub.missile_launched(battle_pb2.MissileLaunchedRequest(missile_type=missile_typ, x_coordinate=x_axis, y_coordinate=y_axis))
                print(response.message)
                #Get updated soldier matrix after missile launch.
                response = stub.GetSoldierMatrix(battle_pb2.MatrixRequest(message="Get Soldier Matrix!!"))
                matrix1 = []
                for i in response.matrix:
                    matrix1.append(list(i.row))
                matrix = [["-" for i in range(n)] for j in range(n)]
                for i in range(n):
                    for j in range(n):
                        matrix[i][j] = matrix1[i][j].value 
                #Invoking printLayout() function after every missile launch to let the user know about position of the soldiers.
                printLayout(matrix, N, M)   
                #Timer for game.                                                                                                                                 
                while temp > 0:
                    temp -= 1
                    time.sleep(1)
                T -= t
            #Printing the status of each soldier after game is over.
            response = stub.status_all(battle_pb2.SoldierStatusAllRequest(message="Send all soldier status!!"))
            statuses = response.statuses
            statuses = statuses.strip()
            statusOfAllSoldiers = statuses.split(' ')

            #Status of all soldiers from status_all() remote call.
            print("\n\nStatus of all the soldiers :- \n")
            soldiersAlive = 0
            for i in range(len(statusOfAllSoldiers)):
                if str(statusOfAllSoldiers[i]) == "True":
                    soldiersAlive += 1
                    print("Soldier " + str(i+1) + " - " + "Alive")
                else:
                    print("Soldier " + str(i+1) + " - " + "Dead")

            #Deciding result of the game.
            if soldiersAlive >= (M//2):
                print("\n\n Congratulations!!! , you have won the battle.")
            else:
                print("Game Over. Better luck next time!!")
    

if __name__ == "__main__":
    logging.basicConfig()
    run()
