#For loops - using dictionaries /Hashes

# for <placeholder> in <dict>:
  #run block of code
# name/money is key
#
#
# dict_data = {
#         'name': 'Branson',
#         'money':200,
# #     }
# #
# #print(dict_data['name'])
# #
#
# #We use the key to access the values of the dictionary.
# for key_placeholder in dict_data:
#     #when we iterate over a hash/dictionary.
#     #the placweholder, holds each individual key during each iteration
#     print(key_placeholder) #This is the key ;)
# #     value = dict_data[key_placeholder] #user key and dictionary to extract individual value of a key
# #     print(value)
#
# dict_data = {
#         'name': 'Branson',
#         'money': 200,
#     }
#
# for key_placeholder in dict_data:
#         print(key_placeholder+ ':', dict_data[key_placeholder])

dict_data = {
        'name': 'Branson',
        'money': 200,
    }

embedded_dict_data = {
1:{
        'name': 'Bronson',
       'money':'200'
},
2: {
    'name':'Tania',
    'money': 300
},
3:{
    'name':'Tylor',
    'money': 400
    }
}


for key in embedded_dict_data:
    print(embedded_dict_data[key])
    print(type(embedded_dict_data[key]))



for item in embedded_dict_data.values():
    print(item)
    print(type(item))