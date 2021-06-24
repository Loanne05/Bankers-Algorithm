def main():
    print("\n-- BANKER'S ALGORITHM --")
    processes = int(input("Number of Processes : "))
    resources = int(input("Number of Resources : "))
    max_resources = [int(i) for i in input("Maximum Resources( Separated w/ spaces) : ").split()]

    print("\n-- ALLOCATED FOR EACH PROCESS --")
    print("Inputs must be separated with spaces")
    currently_allocated = [[int(i) for i in input(f"Process {j + 1} : ").split()] for j in range(processes)]
    print("\n--------------------------------")
    print("\n-- MAXIMUM FOR EACH PROCESS --")
    print("Inputs must be separated with spaces")
    max_need = [[int(i) for i in input(f"Process {j + 1} : ").split()] for j in range(processes)]
    print("\n------------------------------")

    allocated = [0] * resources
    for i in range(processes):
        for j in range(resources):
            allocated[j] += currently_allocated[i][j]
    print(f"\nTotal Allocated Resources : {allocated}")
    print("\n----------------------------------------")
    available = [max_resources[i] - allocated[i] for i in range(resources)]
    print(f"\nTotal Available Resources : {available}")
    print("\n----------------------------------------")
    need = [[0 for i in range(resources)] for i in range(processes)]
    for i in range(processes):
        for j in range(resources):
            need[i][j] = abs(max_need[i][j] - currently_allocated[i][j])
    print(f"\nTotal Needed Resources : {need}")
    print("\n----------------------------------------")
    running = [True] * processes
    count = processes
    while count != 0:
        safe = False
        for i in range(processes):
            if running[i]:
                executing = True
                for j in range(resources):
                    if max_need[i][j] - currently_allocated[i][j] > available[j]:
                        executing = False
                        break
                if executing:
                    print("\n")
                    print(f"Process {i + 1} is Executing")
                    running[i] = False
                    count -= 1
                    safe = True
                    for j in range(resources):
                        available[j] += currently_allocated[i][j]
                    break
        if not safe:
            print("The Processes are in an unsafe state.")
            break

        print(f"The process is in a safe state.\nAvailable Resources : {available}\n")
        print("\n----------------------------------------")



if __name__ == '__main__':
    main()