class IceCream:
    Plain=0              
    Vanilla=5              
    ChocolateChip=5           
    Strawberry=10              
    Chocolate=10  
    def __init__(self, flavor, num_sprinkles):
        self.flavor = flavor
        self.num_sprinkles = num_sprinkles
    def vkus(self):
        if self.flavor == "ChocolateChip": res = self.ChocolateChip+self.num_sprinkles
        
        return f"{a.replece('"'," ")+self.num_sprinkles}"
ice1 = IceCream("ChocolateChip", 13)        
ice2 = IceCream("Vanilla", 0)  
ice3 = IceCream("Plain", 13)        
ice4= IceCream("Strawberry", 0)  
ice5 = IceCream("Chocolate", 13)        
print(ice1.vkus())