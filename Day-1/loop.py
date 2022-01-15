#while loop
# x = 0
# while x<5:
#     print(x)
#     x= x+1

#for loop
# for x in range(5,10):
#     print(x)

#array
day = ("sat", "sun", "mon", "tus", "wed")

for d in day:
    #if(d=="tus"): break #loop stops
    if(d=="tus"): continue #loop continue
    print(d)
