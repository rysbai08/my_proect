class Students:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Adam(Students):
    def __init__(self, name, age,):
        super().__init__('Adilet', 37)

class Ilnur4ik(Students):
    def __init__(self):
        super().__init__('Ilnur', 17)
        
class Kuti(Students):
    def __init__(self):
        super().__init__('Ayanokoji Kyoutaka', '17')
