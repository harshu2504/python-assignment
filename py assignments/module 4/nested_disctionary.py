people={1:{'name':'john','age':30,'sex':'Male'},2:{'name':'merry','age':25,'sex':'Female'}}

for i in range(1,3):
    print(people[i]['name'],"  ",people[i]['age'],"  ",people[i]['sex'])

print("\nAfter appending new element\n")
people[3]={}
people[3]['name']='Luna'
people[3]['age']=26
people[3]['sex']='Female'
people[3]['married']='No'
print(people[3])

print("\nSecond way to add \n")
people[4]={'name':'Jack','age':24,'sex':'Male','married':'Yes'}
print(people[4])

print("\nTo delete element from dictionary \n")
del people[3]['married']
del people[4]['married']
print(people[3])
print(people[4])

print("\n to delete dictionary\n")
del people[3],people[4]
#print(people[3])
#print(people[4])

print("\n Displaying dictionary\n")
for p_id,p_info in people.items():
    print("\nPerson ID",p_id)
    for key in p_info:
        print(key+':',p_info[key])
