n = int(input("Enter a number: "))
div = 2

if n < 2:
    print("Not prime")
else:
    while div < n:
        if n % div == 0:
            print("Not prime")
            break
        div += 1
    else:
        print("Prime")