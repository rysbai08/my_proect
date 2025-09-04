class Students:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Ilnur4ik(Students):
    def __init__(self):
        super().__init__('Ilnur', 17)
        