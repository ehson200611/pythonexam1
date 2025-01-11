# ### Task 1
# # Як комбайн A тонна ғалла даравид, ва дуюмаш B тонна камтар. Ҳар ду комбайн чӣ қадар ғалла даравиданд?

# n=int(input("A = "))
# m=int(input("B = "))

# print("First combine threshed",n ,"tons")
# print(f"Second combine threshed: {n} - {m} = {n-m} tons")
# print(f"total: {n} + {n-m} = {n+(n-m)} tons")




# ### Task 2
# # Дар автобус A мусофир буд. Дар истгоҳ B мусофир фаромад ва C мусофир даромад. Дар автобус чанд мусофир шуд?


# n=int(input())
# m=int(input())
# p=int(input())

# print((n-m)+p)



### Task 3
# Адади чорхонагӣ дода шудааст. Рақами калонтаринро дар ин адад ёбед.

# n=int(input())

# a=n//1000
# b=n//100%10
# c=n//10%10
# d=n%10

# if a>=b and a>=c and a>=d :
#     print(a)
# elif b>=a and b>=c and b>=d :
#     print(b) 
# elif c>=a and c>=b and c>=d :
#     print(c)  
# else :
#     print(d)        
                   
                   
                   
                   
# ### Task 4
# # Four integers are given. Find the number of positive, negative and zeros in the original set.


# n=int(input())
# m=int(input())
# p=int(input())
# i=int(input())
# pos=0
# neg=0
# zero=0
# if n > 0 : pos+=1
# if m > 0 : pos+=1
# if p > 0 : pos+=1
# if i > 0 : pos+=1
    
# if n < 0 : neg+=1
# if m < 0 : neg+=1
# if p < 0 : neg+=1
# if i < 0 : neg+=1
   
# if n==0 :  zero+=1
# if m==0 :  zero+=1
# if p==0 :  zero+=1
# if i==0 :  zero+=1
    
# print(f"Number of positive: {pos}")
# print(neg)
# print(zero)   

   
#    ### Task 5
# # Write a program to display the next and previous even number of the given number.



# n=int(input(f"the  number  is : "))

# if n%2==0 :
#    print(f"The next number for the number {n} is {(n+2)}")
#    print(f"The previous number for the number {n} is {(n-2)}")
# else :
#      print(f"The next number for the number {n} is {(n+1)}")
#      print(f"The previous number for the number {n} is {(n-1)}")

     
     
     
     
#  ### Task 6
# # Given a five-digit number. Find the sum and product of its digits.    
     
     
# n=int(input())

# s=n//10000
# a=n//1000%10
# b=n//100%10
# c=n//10%10
# d=n%10

# print(f"The sum of the digits is: {s+a+b+c+d}")
# print(f"The product of the digits is: {s*a*b*c*d}")




### Task 7
# Write a program to display n terms of natural numbers and their sum.



# n=int(input())
# sum=0
# m=1
# while m<=n :
    
#     print(f"The natural numbers up to 7th terms are: {m} ")
#     sum+=m
#     m+= 1  
    
# print(f"The sum of the natural numbers is: {sum}")     




### Task 8
# Given a real number — the price of 1 kg of sweets. Output cost of 1, 2, ..., 10 kg of sweets.


# cost =float(input())
# kg = 1
# while kg <= 10:
#     total = cost * kg
#     print(f"{kg} kg  {total}")
#     kg += 1





# ### Task 9
# # Write a program to find the factorial of a number.

# num=int(input("Input a number to find the factorial: 5"))
# cnt=1
# while num>0 :
#     cnt=cnt*num
#     num-=1
# print(f"The factorial of the given number is: {cnt}")






### Task 10
# Write a program to display the pattern like right angle triangle with numbers.




# n=int(input("Input number of rows:"))
# i=1
# while i<=n :
#     i+=1
#     print(i,end=" ")
#     j=1
#     while j<=i :
#         j=i-1
#     print(j)        
        
    
    
