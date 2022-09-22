user_dict = {'f_name': 'wilbur', 'l_name': 'wright', 'age': '45', 'hometown': 'Millville', 'location': 'Kill Devil Hills', 'username':  'fliesplanes'}

print(user_dict['f_name'])
print(user_dict['l_name'])
print(user_dict['age'])
print(user_dict['hometown'])
print(user_dict['location'])
print(user_dict['username'])

print(f"This person's first name is {user_dict['f_name']}, their last name is {user_dict['l_name']}, and their username is {user_dict['username']}")
print(f"Wilber Wright's hometown is {user_dict['hometown']} but he last resided in {user_dict['location']}")

definitions = {'python': 'an interpreted computer language', 'variable': 'symbolic name for object', 'list': 'store many items with one variable', 'method': 'function belonging to object', 'if statement': 'conditional statement', 'dictionary': 'this', 'function': 'code that must be called'}

print(f"the language we are using is python, {definitions['python']}")
print(f"a variable is a {definitions['variable']}")
print(f"a list can be used to {definitions['list']}")
print(f"a method is a {definitions['method']}")
print(f"an if statement is a {definitions['if statement']}")
print(f"a dictionary is {definitions['dictionary']}")
print(f"a function is {definitions['function']}")

for definitions in definitions.values():
    print(definitions.title())

sc_counties = {
    'charleston': 'charleston',
    'york': 'york',
    'greenville': 'greenville',
    'anderson': 'anderson',
    'chester': 'west chester',
    'edgefield': 'edgefield'
}

sccountylist = ('charleston', 'york', 'greenville', 'anderson', 'chester', 'edgefield', 'abbeville', 'aiken', 'spartanburg', 'marion')

for counties in sc_counties.values():
    print(counties.title())

