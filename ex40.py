# coding = utf-8
# let's do something about ditc
# so, let's get started.

cities = {'CA': 'San francisco','MI':'Detroit',
          'FL':'Jacksonville'}

cities['NY']='New York'
cities['OR']='Portland'

def find_city(themap,state): # positonal arguments
    if state in themap:
        return themap[state] # return arguments
    else:
        return "Not Found."

# ok pay attention!
cities['_find']=find_city

"""while True:
    print("State? (Enter to quit)",)
    state=input(">")

    if not state: break

    # This lineis the most important ever! study!
    city_found=cities['_find'](cities,state)
    print(city_found)"""
for i,k in cities.items():
    print("State:",i,"City:",k)
