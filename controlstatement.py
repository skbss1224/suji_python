'''a=10
b=8
if(a>b):
    print("b is big value")
elif(a<b):
    print("a is big value")
else:
    print("none of these")
    
    '''
'''tamil=int(input("enter the tamil mark:"))
english=int(input("enter the english mark:"))
maths=int(input("enter the maths mark:"))
social=int(input("enter the social mark:"))
science=int(input("enter the science mark:"))
if(tamil<english):
    print("english mark is big")
elif(english<maths):
    print("maths mark is big")
elif(maths<social):
    print("social mark is big")
elif(social<science):
    print("science mark is big")
else:
    print("none of these")'''
    
'''nationality=input("enter the nationality:")
if(nationality=="indian"):
    print("you can apply for aadhar card")
else:
    print("you are not allow to apply aadharcard")'''
'''
# voter id
age=int(input("enter the age:"))
if(age>=18):
    print("you have 18 + age")
    nationality=input("enter the nationality:")
    if(nationality=="indian"):
        print("you can apply for voter id")
    else:
        print("you are not a indian")
else:
    print("below 18 age so you are  not allowed")'''
#blood donate
    
'''age=int(input("enter the age:"))
if(age>=18):
    print("you have 18+ age")
    weight=int(input("enter the weight:"))
    if(weight>=50):
        print("you can donate this blood")
    else:
        print("your weight is below")
else:
    print("age barror")'''
    
place=input("enter the place:")
if(place=="chennai"):
    print("you can selected bus",place)
    type=input("enter the bus type:")
    if(type=="ordinary"):
        print("you can selected bus",type)
        amount=int(input("enter the amount:"))
        if(amount>=150):
            bal=amount-150
            print("you can 1 ticket reserved")
            print("your balance amount is",bal)
        else:
            print("insuffiecient amount")
    elif(type=="delux"):
        print("you can selected bus",type)
        amount=int(input("enter the amount:"))
        if(amount>=250):
            bal=amount-250
            print("you can 1 ticket reserved")
            print("your balance amount is",bal)
        else:
            print("insuffiecient amount")
    elif(type=="superdelux"):
        print("you can selected bus",type)
        amount=int(input("enter the amount:"))
        if(amount>=350):
            bal=amount-350
            print("you can 1 ticket reserved")
            print("your balance amount is",bal)
        else:
            print("insuffiecient amount")
    elif(type=="sleeper"):
        print("you can selected bus",type)
        amount=int(input("enter the amount:"))
        if(amount>=450):
            bal=amount-450
            print("you can 1 ticket reserved")
            print("your balance amount is",bal)
        else:
            print("insuffiecient amount")
    else:
        print("A/c bus service not available")
elif(place=="coimbatore"):
    print("you can selected bus",place)
    type=input("enter the bus type:")
    if(type=="ordinary"):
        print("you can selected bus",type)
        amount=int(input("enter the amount:"))
        if(amount>=100):
            bal=amount-100
            print("you can 1 ticket reserved")
            print("your balance amount is",bal)
        else:
            print("insuffiecient amount")
    elif(type=="delux"):
        print("you can selected bus",type)
        amount=int(input("enter the amount:"))
        if(amount>=200):
            bal=amount-200
            print("you can 1 ticket reserved")
            print("your balance amount is",bal)
        else:
            print("insuffiecient amount")
    elif(type=="superdelux"):
        print("you can selected bus",type)
        amount=int(input("enter the amount:"))
        if(amount>=300):
            bal=amount-300
            print("you can 1 ticket reserved")
            print("your balance amount is",bal)
        else:
            print("insuffiecient amount")
    elif(type=="sleeper"):
        print("you can selected bus",type)
        amount=int(input("enter the amount:"))
        if(amount>=400):
            bal=amount-400
            print("you can 1 ticket reserved")
            print("your balance amount is",bal)
        else:
            print("insuffiecient amount")
    else:
        print("A/c bus service not available")
else:
    print("i have only two places availble in this bus chennai and coimbatore")