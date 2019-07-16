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


####################################################################################################################

weather ='rainy'
##Strip function 
weather = input("What is the weather like today?").lower().strip()

if weather == 'rainy' or weather == 'stormy':

    print('take an umbrella')
elif weather == "sunny":
    print("take your sun glasses and sunscreen")

else:
    print("Go live your life")




#
# bad_weather =='rainy'
# good_weather == 'Sunny'
# sunny_equipment == 'Sun glasses'
# water_protection == 'umbrella'
#
# weather = 'rainy'
#
# if bad_weather:
#     print(f"Today, we have bad weather you need to bring your {water_protection}")
#
# elif good_weather:
#     print(f"Dont worry today is perfect. Just bring your {sunny_equipment} in case")
#
#     weather = "Sunny"
#
#     if good_weather:
#         print(f"its great weather, leave you{water_protection} at home")
#
#     elif bad_weather:
#         print(f"Ow gosh, youre going to need to bring your {water_protection} and forget the{sunny_equipment}")