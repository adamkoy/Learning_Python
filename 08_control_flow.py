# Control flow - IF functions or IF statements
#if < condition> :
    #Block of code
       # else:
         #Block of code
           #elif
             # Block of code


# age = 70
#
# if age>=70:
#     print("you can do everything but take it easy")
#
#     print('Your age is above 18, you can vote! ;D and go to prison')
#
# elif age > 16:
#     print("you can buy a lottery ticket and probably go to prison but your record will be cleaned after")
#
# else:
#     print("You are under age to vote")

#
# ####################################################################################################################
#
# weather ='rainy'
# ##Strip function
# weather = input("What is the weather like today?").lower().strip()
#
# if weather == 'rainy' or weather == 'stormy':
#
#     print('take an umbrella')
# elif weather == "sunny":
#     print("take your sun glasses and sunscreen")
#
# else:
#     print("Go live your life")

#
# I want a jacket when it is rainy and stormy
#
# I want an umbrella only when it is rainy
#
# I also want a umbrella if it is foggy, because you never
# if know.:
#
# Keep stuff from sunny


# weather = 'sunny'
#
# result1 = weather =='rainy'
# result2 = weather == 'Sunny'
#
#



weather = input("What is the weather like today?").lower().strip()


if weather == 'rainy and stormy':
  print("I want a jacket")

elif weather == 'rainy':
    print("Please take only your umbrella")

elif weather== "foggy":
    print("Take your umbrella if it is foggy ")

else:
    print("keep your stuff if it is sunny")
