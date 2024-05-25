class Nobel:
    def __init__(self,category, year, winner):
        self.category=category
        self.year=year
        self.winner=winner
    def __str__(self):
        return f"{self.category}, {self.year}, {self.winner}"
np2005=Nobel("Peace", 2005, "Muhammad Yunus")
print(np2005.__str__())