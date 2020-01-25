import pandas as pd
'''batsman={ 1:{'Type':'Left-arm','Name':'Gautam Gambhir','Matches':101,'Runs':6012,'Average':67,'Heighest score':140},
          2:{'Type':'Left-arm','Name':'Virendra sahwag','Matches':300,'Runs':7612,'Average':96,'Heighest score':219},
          3:{'Type':'Right-arm','Name':'Rohit Sharma','Matches':251,'Runs':7299,'Average':105,'Heighest score':210}
        }
print("Type\tName\tMatches\tRuns\tAverage\t Heighest")
for p_id,p_info in batsman.items():
  #  print("\n Player Id",p_id)
    for key in p_info:
        print(p_info[key],"  ",end="")
    print()
    
print()
'''
#Another way
squad={'batsman':{ 1:{'Type':'','Name':'Gautam Gambhir','Matches':101,'Runs':6012,'Average':67,'Heighest score':140},
          2:{'Type':'Left-arm','Name':'Virendra sahwag','Matches':300,'Runs':7612,'Average':96,'Heighest score':219},
          3:{'Type':'Right-arm','Name':'Rohit Sharma','Matches':251,'Runs':7299,'Average':105,'Heighest score':210}
        }}
df=pd.DataFrame(squad['batsman'])
print(df)

print("\n",squad['batsman'][1]['Runs'])
Runs=[]
Name=[]
for i in range(1,4):
    Runs.append([squad['batsman'][i]['Runs']])
    Name.append([squad['batsman'][i]['Name']])
print(max(Runs))
print(Name[Runs.index(max(Runs))])
