import pickle

datastore = { "office" : {"medical":[
    {"room-number":100,"use":"reception","sq-feet":50,"price":75},
    {"room-number":101,"use":"waiting","sq-feet":250,"price":75},
    {"room-number":102,"use":"examination","sq-feet":125,"price":150},
    {"room-number":103,"use":"examination","sq-feet":125,"price":150},
    {"room-number":104,"use":"office","sq-feet":150,"price":100}],
    "parking":{"location":"primium","style":"covered","price":750}}}

out_file = open('datastore.dat','wb')
pickle.dump(datastore,out_file)
out_file.close()

in_file = open('datastore.dat','rb')
pb=pickle.load(in_file)
in_file.close()
print(pb)
