class User:

    def __init__(self, name, password, points=135):
        self.name = name
        self.password = password
        self.points = points

    def __str__(self):
        return f'User {self.name} has  {str(self.points)} points'
