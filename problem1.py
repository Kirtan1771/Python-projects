class Programmer:
    company = "Google"
    
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
        
p = Programmer("Kirtan" , 1200000 , 382006)
print(p.company , p.name , p.salary , p.pin)
        