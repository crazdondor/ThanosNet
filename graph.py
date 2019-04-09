class Graph:

    def __init__(self):
        self.users = []
        self.adj_matrix = []

    def user_exists(self, user):
        if user in self.users:
            return True
        return False
    
    def check_connection(self,user1, user2):
        if not self.user_exists(user1) or not self.user_exists(user2):
            return -1
        name1_val = self.find_nameval(user1)
        name2_val = self.find_nameval(user2)
        for i, row in enumerate(self.adj_matrix):
            if i == name1_val:
                for j, col in enumerate(self.adj_matrix):
                    if j == name2_val:
                        return self.adj_matrix[i][j]

    def init_adjmatrix(self):
        self.adj_matrix = [[0 for i in range(len(self.users))] for j in range(len(self.users))]

    def add_user(self, user):
        if not self.user_exists(user):
            self.users.append(user)

    def find_nameval(self, name):
        for i in range(len(self.users)):
            if self.users[i] == name:
                return i

    def add_val(self, name1, name2, val):
        name1_val = self.find_nameval(name1)
        name2_val = self.find_nameval(name2)
        for i, row in enumerate(self.adj_matrix):
            if i == name1_val:
                for j, col in enumerate(self.adj_matrix):
                    if j == name2_val:
                        self.adj_matrix[i][j] = val
