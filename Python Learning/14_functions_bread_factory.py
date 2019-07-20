#Our bread factory

def make_dough(ingrediant1, ingrediant2):
    if'wheat' in ingrediant1 and 'water' in ingrediant2:
        return'dough'
    else:
        return 'wrong ingredients. you used ' + ingrediant1 + ' ' + ingrediant2


def bake_bread(semi_product):
    if semi_product =='dough':
        return 'bread'
    else:
        return 'wrong ingredients. you used' + ' ' + semi_product



print(make_dough('wheat', 'water'))
print(make_dough('cement', 'water'))
print(make_dough('cement', 'water') == 'dough')
#
# #Tests
# print('call function make_dough, expect dough to be retunred')
# print(make_dough('wheat','water') == 'dough')
#
# print("called funtion make_dough with wrong with wrong ingredients. Expect it to return wrong ingredients")
# print(make_dough('cement', 'water') == 'wrong ingredients')
#
# print('call function make_bread, expect bread to be retunred')
# print(bake_bread('dough') == 'bread')
#
# print('called function bake_bread with wrong ingredients. expect outcome to be wrong ingredients')
# print(bake_bread('chocolate cement') == 'wrong ingredients')