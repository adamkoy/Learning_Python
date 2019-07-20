import time

while True:
    swiping_choice= input("A young hot lassie has swiped you right. Will you swipe right back?").strip().lower()

    if swiping_choice == 'yes':
        print("congratulations, she wants to meet you tonight!")

    else:
        print("better luck next time")

    energy_levels = input("Do you have energy tonight?").strip().lower()

    if energy_levels == 'yes':
        print("Good boy, take a energy tablet just to be safe")
    else:
     print("forget it mate, you'll always be single!!!!")
    break

    choose_restaurant = input("She wants you to pick the restaurant. Where will you go?")

    if choose_restaurant == "curry":
        print( "She loves it and cant wait to spice things up")
        print("lovely jubbly")

    elif choose_restaurant == "Italian":
        print("Italian on a first date!? What were you thinking? GAME OVER")
        break

    else:
        print("Looks like she doesnt like your taste in food. Shes rejected you to date that hot italian guy who can cook curry")
        break




    print("you've ended up at the pub and you've been drinking for a few hours now")

    drunk= input("Do you think she's drunk?").strip().lower()

    if drunk == "yes":
        print("She's going to be an easy pull. Get to the dance floor and start grinding")

    else:
        print("You've got no chance pulling tonight. Be a gentleman and escort her home")
        time.sleep(2)
        print("Give a small kiss on the cheek to make her smile")
        break
   # "You are Ollie, a likeable young guy in search of love. Our story begins when Ollie comes across an attractive young woman on Tinder...");
    print("She's the one")
    break