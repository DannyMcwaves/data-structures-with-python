
from structs import LinkedList


ll = LinkedList()
ll += 'Danny'
ll += 2
ll += 3
ll += 4
ll += 5

ll[4] = 'Johnny'
ll.insert(4, 'Homey')

ll.add('Homey')

ll.insert(6, 'Holy')
del ll[7]
print(len(ll))

# for i in ll:
#     print(i)

print(len(ll))

print('Danny' in ll)
