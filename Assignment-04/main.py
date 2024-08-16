#Assignment-04
name=input("Enter your Name : ")
print(f"Nice to meet you {name.capitalize()} \n\n.")

#taking favourit number
print("Plz Enter your three Favorite Number ..")
fav_number1=int(input("Enter your First favorite number : "))
fav_number2=int(input("Enter your Second favorite number : "))
fav_number3=int(input("Enter your Third favorite number :  "))

#Greeting massage
print(f"Hello ,{name.capitalize()}! Nice to meet you . ")


# creating a list of favourit number
favorite_number=[fav_number1,fav_number2,fav_number3]
print(f"your favorite number {favorite_number} Let's explore your favorite numbers:\n\n")


# Check Num is even and odd
for numbers in favorite_number:
    if numbers%2 ==0:
        print(f"The number {numbers} is Even .")
    elif numbers%2 ==1:
        print(f"The number {numbers} is Odd .")
    else:
        print(f"The Number {numbers} is Zero .")


# Sum of the list 
sum_fav_num= sum(favorite_number)
print(F"Amazing! The sum of your favorite numbers is: {sum_fav_num}\n\n")



# Now Check sum of Number is prime Number or not .
if sum_fav_num <=1:
    print(f"The Sum of favourit number is not the Prime Number .")

else:
    prime_num= True #boolen flag (assume is prime number)

    for i in range(2,sum_fav_num): # in range(2,num) first 2 show starting of loop from 2 and 2nd show ending before reach to the desire num .
        if sum_fav_num%2 == 0:
            prime_num= False
            break

if prime_num:
    print(f"{sum_fav_num} Wow ,  is a Prime Number .")
else:
    print(f"{sum_fav_num} is not a Prime Number .")