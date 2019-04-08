import csv



def main():
    # load .txt file
    with open('graph.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=' ')
        for row in readCSV:
            # read the boi
            pass
    print("Welcome to ThanosNet")
    choice = 0
    while choice != 3:
        print()
        print("1) Check if user exists")
        print("2) Check connection between users")
        print("3) Quit")
        choice = int(input(">  "))
main()