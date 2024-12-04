class Calculator:
    def __init__(self , n):
        self.n = n
        
    def square(self):
        print(f"The sqaure of number is {self.n*self.n}")
        
    def cube(self):
        print(f"The cube of number is {self.n*self.n*self.n}")
    
    def sqRoot(self):
        print(f"The sqaure root of the number is {self.n**1/2}")
a = Calculator(4)
a.square()
a.cube()
a.sqRoot()