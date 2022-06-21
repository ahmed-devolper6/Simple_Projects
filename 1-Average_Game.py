#this is a simple game take numbers form user and get the sum of number and the average
corrent_number = float(input("Enter who many numbers u want to take: "))
counet = 0
summ = 0
while corrent_number > counet:
    take_number = float(input("Enter number: "))
    summ += take_number
    counet += 1
print(f"the sum of your number is = {summ}")
print(f"the average of your number is = {summ/corrent_number}")
