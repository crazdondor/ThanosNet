class Graph:

    def __init__(self):
        self.users = []
        self.adj_matrix = []

    def user_exists(self, user):
        if user in self.users:
            return True
        return False