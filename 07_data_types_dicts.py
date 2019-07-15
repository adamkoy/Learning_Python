# Dictionaries AKA Hashes
# Dictionaries work with key: value pairs. As a appose with using a indexes
#Declaring a hash/ Dictionary
pika = {  }


# Dictionaries work with keys: values (key has to be a string)

pika = {
    'name': 'Derik Dice',
    'pokemon': 'pikachu',
    'age': 17 ,
    'personality': 'Grumpy'
}

print(pika)
print(type(pika))

#Access information using the keys
print(pika['age'])
print(pika['pokemon'])

# Re assign values, using the keys
pika['age'] = 18
print(pika['age'])

#Adding a key : value pair
pika['colour'] = 'Yellowish'
print(pika)

#Creating Key value first for first and last name
full_name= pika['name'].split()
print(full_name)
first_name = full_name[0]
print(first_name)
pika['first_name'] = first_name
pika ['last_name'] = full_name
print(pika)

# Important Methods
#Embeded data

pika = {
    'name': 'Derik Dice',
    'pokemon': 'pikachu',
    'age': 17 ,
    'personality': ['Horny', 'jumpy' ,'shocking', 'static']
}
print(pika['personality'])
print(pika['personality'])


pika = {
    'name': 'Derik Dice',
    'pokemon': 'pikachu',
    'age': 17 ,
    'personality':{

    'Horny':10000,
    'jumpy':100 }
}

print(pika['personality']['Horny'])

# important Methods - Same as array

keys = pika.keys()
print(keys)

values = pika.values()
print(values)