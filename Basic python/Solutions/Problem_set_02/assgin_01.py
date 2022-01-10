class BBA_Student:
    def __init__(self, name='', dept='BBA'):
        self.__name = name
        self.__department = dept

    def set_department(self, dept):
        self.__department = dept

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name

    def __str__(self):
        if self.__name=='':
            return 'Default Department: '+self.__department
        else:
            return 'Name: '+self.__name+' Department: '+self.__department


print(BBA_Student())
print(BBA_Student('Humpty Dumpty'))
print(BBA_Student('Little Bo Peep'))

