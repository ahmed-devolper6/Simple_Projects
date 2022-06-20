def mullgame:
    for x in range(start,end+1):
        for y in range(1,11):
            print(f"{x} X {y} = {x*y}")
        print("....................")

start = int(input("enter the start: "))
end = int(input("Enter the end:"))
mullgame(start,end)
