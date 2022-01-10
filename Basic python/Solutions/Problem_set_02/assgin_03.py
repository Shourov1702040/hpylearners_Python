class Tournament:
    def __init__(self, name="Default"):
        self.__name = name
    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name

class Cricket_Tournament(Tournament):
    def __init__(self, name="Default",team_num=0,type="No type"):
        Tournament.__init__(self, name)
        self.team_no = team_num
        self.type = type

    def detail(self):
        return f"Cricket Tournament Name: {self.get_name()}\nNumber of player= {self.team_no}\nType: {self.type}"

class Tennis_Tournament(Tournament):
    def __init__(self, name="Default",team_num=0):
        Tournament.__init__(self, name)
        self.team_no = team_num

    def detail(self):
        return f"Tennis Tournament Name: {self.get_name()}\nNumber of player= {self.team_no}"

ct1 = Cricket_Tournament()
print(ct1.detail())
print("-----------------------")
ct2 = Cricket_Tournament("IPL",10,"t20")
print(ct2.detail())
print("-----------------------")
tt = Tennis_Tournament("Roland Garros",128)
print(tt.detail())