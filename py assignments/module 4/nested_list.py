matrix=[]
for i in range(5):
    #Append an empty sublist inside the list
    matrix.append([])
    for j in range(5):
        matrix[i].append([j])
print(matrix)

#nested list Comprehension
matix=[[j for j in range(5)] for i in range(5)]
print(matrix)
print()

#Flatter a given2D list

matrix=[[1,2,3],[4,5,6],[7,8,9]]
flatten_matrix=[]
for sublist in matrix:
    for val in sublist:
        flatten_matrix.append(val)
print(flatten_matrix)

#nested list comprehension to flatten a given 2d list
flatten_matrix=[val for sublist in matrix for val in sublist] #second way
print(flatten_matrix)

print()
planets=[['Mercury','Venus','Earth'],['Mars','Jupiter','Saturn'],['Uranus','Neptune','Pluto']]
flatten_planets= [planet for sublist in planets for planet in sublist if len(planet)<6]
print(flatten_planets)
