def swap(number):
    vid = number < 0
    if vid:
        number = -number  

    ost = number % 10

    count = 0
    temp = number
    while temp > 0:
        count += 1
        temp //= 10

    first = number // (10 ** (count - 1))

    middle = number % (10 ** (count - 1)) 
    middle //= 10  


    new_number = ost * (10 ** (count - 1)) + middle * 10 + first

    if vid:
        new_number = -new_number

    return new_number

num = int(input("Input: "))
result = swap(num)
print("Result:", result)
