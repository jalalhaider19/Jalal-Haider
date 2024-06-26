##Question1
import pandas as pd 

dataframe = pd.DataFrame({
 'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
 'Age': [24, 27, 22, 32, 29],
 'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
})

print(dataframe)

##Question2 
import pandas as pd 

df = pd.DataFrame({
 'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
 'Age': [24, 27, 22, 32, 29],
 'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
})

print(data['Name'])
print(df[df['Age'] > 25])
print(df[df['Age'].sort())


##Question3
import pandas as pd 

df['Age'] = [25, 28, 23, 33, 30]
print(df)


df2 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'City': ['San Francisco', 'Seattle', 'Austin', 'Dallas', 'Miami']
})
print(df2)

df['City'] = df2['City']
print(df)



##Question4 
#4.1 
for key, value in df['Name','Age']:
    print(key, value)


#4.2 
