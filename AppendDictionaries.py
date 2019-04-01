
dictionary =  {
            'starTrekResurface_replicator':{'type': ['EventRentBuilding'], 'count': 0},
            'starTrek_turboLift':{'type': ['EventDecoration'], 'count': 0},
            'starTrekResurface_yellow':{'type': ['EventDecoration'], 'count': 0},
            'starTrekResurface_red':{'type': ['EventDecoration'], 'count': 0},
            'starTrekResurface_blue':{'type': ['EventDecoration'], 'count': 0},
            'starTrekResurface_warpCore':{'type': ['EventDecoration'], 'count': 0}
        }
rooms_dict = {'starTrekResurface_blankRoom%i'%i:{'type': ['EventDecoration', 'EventRentBuilding'], 'count': 0} for i in range(1,18)}


print 'dictonary:'
print dictionary

print '\nrooms'
print rooms_dict;

dictionary.update(rooms_dict)

print '\ndictonary:'
print dictionary