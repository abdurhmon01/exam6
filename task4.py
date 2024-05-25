import random
loto_player = []
for i in range(100):
    n=random.randrange(10**9,10**10)
    loto_player.append(n)
print(random.sample(loto_player,k=2))