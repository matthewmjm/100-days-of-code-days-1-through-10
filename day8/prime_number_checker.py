#Write your code below this line ๐
def prime_checker(number):
    if n > 1:
        for x in range(2, int(n/2) + 1):
            if n % x == 0:
                print(f"{n} is not a prime number.")
                break
        else:
            print(f"{n} is a prime number.")
    else:
        print (f"{n} is not a prime number.")    

#Write your code above this line ๐
    
#Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)