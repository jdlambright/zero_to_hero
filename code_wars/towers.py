def tower_builder(n_floors):
    tower = []
    floor = 1

    while floor <= n_floors:
        tower.append(f"{' ' * (n_floors - floor)}" + f"{'*' * floor}" + f"{'*' * (floor-1)}" + f"{' ' * (n_floors - floor)}")
        floor += 1
    print(tower)
    return tower

tower_builder(3)
