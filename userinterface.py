import logging
import random

import grpc
from Soldier import Soldier
import time

import battle_pb2
import battle_pb2_grpc

def printLayout(matrix, N, M):
    noOfSpaces = len(str(M))+1
    for i in range(N):
        for j in range(N):
            if matrix[i][j]=="-":
                print(matrix[i][j], end=" "*noOfSpaces)
            else:
                print(matrix[i][j], end=" ") 
        print("")


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


def run():

    # Input Matrix Size
    N = int(input('Enter size of the matrix(N): '))
    matrix = [["-" for i in range(N)] for j in range(N)]

    # Input Soldiers.
    M = int(input('Enter the no. of soldiers: '))
    while M > N*N:
        print("Wrong number of soldiers. Please enter a number less than N*N.")
        M = int(input('Enter the no. of soldiers: '))

    # Place Soldiers randomnly
    soldiersList = []
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
        soldiersList.append(soldier)
        portNo += 1

    print("Initial posititons of soldiers\n\n")
    print("<------------------------------------------------------------------------------------------------------>")
    print("\n\n")
    printLayout(matrix, N, M)

    # Input time
    T = int(input('Enter the duration of the battle (in secs): '))
    t = int(input('Enter the time gap between two missile launches(in secs): '))

    for sol in soldiersList:
        print(sol.soldierId, sol.portNo)

    while T != 0:
        temp = t
        missile_type = input('Enter type of missile to fire: ')
        x_axis, y_axis = map(int, input('Enter the coordinates for missile launch:').split(' '))
        print(missile_type, (x_axis, y_axis))
        with grpc.insecure_channel("localhost:50051") as channel:
            stub = battle_pb2_grpc.BattleStub(channel)
            response = stub.missile_launched(battle_pb2.MissileLaunchRequest(x_coordinate=x_axis, y_coordinate=y_axis))
            print("Battle client received: " + response.message)                                                                                                                                    
        while temp > 0:
            temp -= 1
            time.sleep(1)
        T -= t

if __name__ == "__main__":
    logging.basicConfig()
    run()
