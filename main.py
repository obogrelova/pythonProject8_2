import pandas as pd

data = {
    'Name' : ['Jack', 'Eric', 'Alice', 'Kevin', 'Harry', 'Jesse', 'Bob', 'Roma', 'Darren', 'Anna'],
    'Mathematics_grade' : [5, 4, 4, 5, 3, 5, 5, 4, 4, 3],
    'Physics_grade' : [4, 4, 5, 5, 4, 5, 4, 5, 5, 4],
    'Astrology_grade' : [5, 5, 5, 4, 5, 4, 4, 5, 5, 4],
    'English_language_grade' : [4, 4, 4, 5, 5, 3, 4, 4, 5, 5],
    'Story_grade' : [4, 4, 4, 4, 5, 5, 3, 4, 5, 4]
}

df = pd.DataFrame(data)

print(df)