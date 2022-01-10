class Football:
    def __init__(self, team_name, name, role):
        self.__team = team_name
        self.__name = name
        self.role = role
        self.earning_per_match = 0
    def get_name_team(self):
        return 'Name: '+self.__name+', Team Name: ' +self.__team

class Player(Football):
    def __init__(self, team_name, name, role, goal, match):
        Football.__init__(self, team_name, name, role)
        self.goal = goal
        self.match = match
        self.ratio = 0
        self.earn = self.goal*1000 + self.match*10
    def calculate_ratio(self):
        self.ratio = self.goal/self.match
    def print_details(self):
        print(self.get_name_team())
        print("The role : "+self.role)
        print("Total goal : ",self.goal,", Total played : ",self.match)
        print("Goal ratio : ",self.ratio)
        print("Match earning : ",self.earn,"K")

class Manager(Football):
    def __init__(self, team_name, name, role,win):
        Football.__init__(self, team_name, name, role)
        self.win = win
        self.ratio = 0
        self.earn = self.win*1000

    def print_details(self):
        print(self.get_name_team())
        print("The role : "+self.role)
        print("Total win : ",self.win)
        print("Match earning : ",self.earn,"K")

player_one = Player('Juventus', 'Ronaldo', 'Striker', 25, 32)
player_one.calculate_ratio()
player_one.print_details()
print('------------------------------------------')
manager_one = Manager('Real Madrid', 'Zidane', 'Manager', 25)
manager_one.print_details()
