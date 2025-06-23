for chickens in range(36):
    rabbits = 35 - chickens
    total_legs = chickens * 2 + rabbits * 4
    if total_legs == 94:
        print("Chickens:", chickens)
        print("Rabbits:", rabbits)
        break
