class yuk:
    def __init__(self,km,kg):
        self.km = km
        self.kg = kg
    def info(self):
        return (self.km * 1000) + (self.kg * 1000)
        
natija = yuk(10,20)
print("yetkazib berish narxi", natija.info(), "so'm")