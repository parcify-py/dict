robots = {'RD2R': 'repair'}
start = True

while start:
    robot = input("Enter name of robot: ")
    if robot in robots:
        print(f"Function: {robots[robot]}")
    else:
        choice = input("Robot not found. Type 'exit'or 'add': ").lower()
        if choice == 'exit':
            start = False
        elif choice == 'add':
            new_name = input("Enter name of new robot: ")
            new_func = input("Enter function of new robot: ")
            robots[new_name] = new_func

print(robots)
