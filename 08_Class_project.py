




spartan_clients = ['RBS', 'Goldmansach', 'Channel 4', 'Three','Earthpoint','Maresk', 'iSPL', 'BBC', 'Home Office',
                   'Spotify' ]
print(spartan_clients)
print(type(spartan_clients))

print(f"Sparta's client {spartan_clients[0]} is the coolest")
print(f"Sparta's client {spartan_clients[5]} is a very cool client of Sparta")
print(f"Sparta's client {spartan_clients[-3]} is a very demanding client of Sparta")
print(f"Sparta's client {spartan_clients[-6]} is a very high client of Sparta")
print(f"Sparta's client {spartan_clients[-8]} is the main client of Sparta")

print("Sparta's client" + spartan_clients[-6] + "is a very high client of Sparta")
print("Sparta's client" + spartan_clients[5] + "is a very cool client of Sparta")
print("Sparta's client" + spartan_clients[-9] + "is a very demanding client of Sparta")
print("Sparta's client" + spartan_clients[9] + "is the main client of Sparta")
print('------------------')
# The Little Red Riding Hook

Beginning = {
    'scene1': 'Little red riding hood went deep down into the forest',
    'scene2': 'She met with the wolf and she ran away',
    'scene3': 'She got lost and wondered through the forest' }

Middle = {
    'scene1': "The wolf arrived at red riding hood's home and ate her grandma",
    'Scene2':" Little Red riding Hood arrived at home and saw the wolf disguised as her Grandma",
    'scene3':"The wolf ate her and went to sleep"
}

End = {
    'scene1': "Little red hiding hood got her knife out and cut open from the wolf from the inside out",
    'Scene2': " She used the wolf's skin to make a winter coat",
    'scene3': "The End"
}

print(beginning[scene1])
print(middle)['scene1']

#Homework
#Using the above story and our amazing ways of gathering user input make the story more interactive.
#Ask the user to complete the story
#rebuild/ reassign and assign it to the items in the hash.
#Re-print the story

#Homework should be a new project, new repo and new githun repo .
#should also be a read.me
new_character = input()
print(new_character)