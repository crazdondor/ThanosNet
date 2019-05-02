# Bennett Falkenberg, Brewer Slack, Quinlan Bingham
# ThanosNet

import csv
from graph import Graph
import time
import random

def check_user(graph):
    user = input("Input user name: ")
    print(graph.user_exists(user))

def check_connection(graph):
    user1 = input("Input user 1 name: ")
    user2 = input("Input user 2 name: ")
    val = graph.check_connection(user1, user2)
    if val == -1:
        print('One or both of these users do not exist')
    else:
        print(val)

def best_friend_chain(graph):
    user1 = input("Input your name: ")
    user2 = input("Input the person's name you want to check: ")
    visit_or_not = []
    user_list = graph.get_users()
    for i in range(len(user_list)):
        visit_or_not.append('u')
    
    current_node = user1
    path = []
    path_values = []
    path.append(current_node)
    max_loops = len(user_list)
    curr_loop = 0
    while current_node != user2:
        # if the loop has run more  times than there are vertices, there is no connection, break
        if  curr_loop > max_loops:
            path.clear()
            break
        # start by marking the current node as visited
        for i in range(len(user_list)):
            if user_list[i] == current_node:
                visit_or_not[i] = 'v'
        
        # now, we define neighbors of current node
        neighbors = []
        values = []
        for i in range(len(user_list)):
            val = graph.check_connection(current_node, user_list[i])
            if val > 0 and visit_or_not[i] == 'u':
                neighbors.append(user_list[i])
                values.append(val)

        # if the node we're looking for is a neighbor, append it to the path and break
        if user2 in neighbors:
            val = graph.check_connection(current_node, user2)
            path_values.append(val)
            path.append(user2)
            break

        # find best neighbor to go to
        greatest_val = 0
        for i in range(len(neighbors)):
            if values[i] > greatest_val:
                greatest_val = values[i]
        
        # set current node to best valued node
        for i in range(len(neighbors)):
            if greatest_val == values[i]:
                current_node = neighbors[i]
                break
        
        # append new current node
        path.append(current_node)
        path_values.append(greatest_val)
        curr_loop +=  1

    # print the path, if there is a  path
    if (len(path) != 0):
        for i in range(len(path)-1):
            print(path[i] + " -> " + str(path_values[i]) + " ->")
        print(path[len(path)-1])
    else:
        print("There is no connection between " + user1 + " and " + user2)

def snap(graph):
    print("Dread it.")
    time.sleep(1)
    print()
    print("Run from it.")
    time.sleep(1)
    print()
    print("Destiny still arives.")
    print()
    time.sleep(1)
    
    users = graph.users

    users_before = ', '.join(map(str, users)) 
    print("Population before the snap:", users_before)
    print()
    for row in graph.adj_matrix:
        print(row)
    time.sleep(1)

    num_to_snap = len(graph.users)/2
    snap_indices = set()
    while len(snap_indices) < num_to_snap:
        snap_indices.add(random.randint(0,len(graph.users) - 1))

    reverse_snap_indices = list(snap_indices)
    reverse_snap_indices.reverse()

    for index in reverse_snap_indices:
        graph.adj_matrix.remove(graph.adj_matrix[index])

    for row in graph.adj_matrix:
        for index in reverse_snap_indices:
            row.pop(index)
    
    print()
    for index in reverse_snap_indices:
        time.sleep(1)
        print(users[index], "has turned into dust")
        print()
    
    for row in graph.adj_matrix:
        print(row)



 

def main():
    graph = Graph()
    # load .txt file
    with open('graph.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=' ')
        # create list of users
        for row in readCSV:
            graph.add_user(row[0])
            graph.add_user(row[1])
        # initialize adj matrix
        graph.init_adjmatrix()

    with open('graph.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=' ')
        # populate adj matrix
        for row in readCSV:
            val = int(row[2])
            name1 = row[0]
            name2 = row[1]
            graph.add_val(name1, name2, val)

    print("Welcome to ThanosNet, spoiler free since March 2019.")
    choice = 0
    while choice != 5:
        print()
        print("1) Check if user exists")
        print("2) Check connection between users")
        print("3) Best friend chain between you and another user")
        print("4) Thanos snaps his fingers")
        print("5) Quit")
        choice = int(input(">  "))
        if choice == 1:
            check_user(graph)
        elif choice == 2:
            check_connection(graph)
        elif choice == 3:
            best_friend_chain(graph)
        elif choice == 4:
            snap(graph)
main()