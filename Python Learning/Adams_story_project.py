



new_hero = input('What is the name of your new character?')
new_villan = input("Who is the new villan of the story?")
new_victim = input( "Who is the victim of the story?")
new_weapon = input("What sharp weapon does the hero use to slay the villan?")
new_gender = input("Is your hero a he or a she?")

print ("--------------")

beginning = {
    'scene1': f'{new_hero} went deep down into the forest. '
     f' And met with {new_villan} by accident. {new_villan} scared {new_hero} and {new_gender} ran away. '
     f' {new_gender} got lost and wondered through the forest.'}

middle = {
    'scene1': f"This gave {new_villan} enough time to arrive at {new_hero}'s home to eat {new_victim}."
              f" When {new_hero} arrived at home, {new_gender} saw the {new_villan} disguised as "
    f"{new_victim}."
    f" {new_hero} went closer to give a hug. "
    f" {new_villan} used this opportunity to eat {new_hero} and then went to sleep feeling tired after eating."
}

end = {
    'scene1': f"Then {new_hero} quickly got out the {new_weapon}  and started to cut open {new_villan}'s stomach"
    f" from the inside out. "
    f"  {new_villan} screamed and then died leaving it's skin.  {new_hero} used the skin to make a winter coat out of it"
    f" and spent the days remembering mourning over {new_victim} "
     "The End."
}


print(beginning)
print(middle)
print(end)
#Homework
#Using the above story and our amazing ways of gathering user input make the story more interactive.
#Ask the user to complete the story
#rebuild/ reassign and assign it to the items in the hash.
#Re-print the story

#Homework should be a new project, new repo and new githun repo .
#should also be a read.me

