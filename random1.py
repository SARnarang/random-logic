num = [3, 2, 7, 4, 9]

math = len(num)


user = int(input("num pos will go away: "))


i = 0
for x in num:
    
    if i != user:
       print(num[i])
    i+= 1
   