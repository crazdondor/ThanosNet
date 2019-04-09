import csv
from graph import Graph

def check_user(graph):
    user = input("Input user name: ")
    print(graph.user_exists(user))

def check_connection(graph):
    user1 = input("Input user 1 name: ")
    user2 = input("Input user 2 name: ")
    val = graph.check_connection(user1, user2)
    print(val)

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

    print("Welcome to ThanosNet")
    choice = 0
    while choice != 3:
        print()
        print("1) Check if user exists")
        print("2) Check connection between users")
        print("3) Quit")
        choice = int(input(">  "))
        if choice == 1:
            check_user(graph)
        elif choice == 2:
            check_connection(graph)
main()