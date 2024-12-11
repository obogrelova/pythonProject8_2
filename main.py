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

print(f"Средняя оценка по математике - {df['Mathematics_grade'].mean()}")
print(f"Медианная оценка по математике - {df['Mathematics_grade'].median()}")
print(f"Стандартное отклонение оценки по математике - {df['Mathematics_grade'].std()}")

print(f"Средняя оценка по физике - {df['Physics_grade'].mean()}")
print(f"Медианная оценка по физике - {df['Physics_grade'].median()}")
print(f"Стандартное отклонение оценки по физике - {df['Physics_grade'].std()}")

print(f"Средняя оценка по астрологии - {df['Astrology_grade'].mean()}")
print(f"Медианная оценка по астрологии - {df['Astrology_grade'].median()}")
print(f"Стандартное отклонение оценки по астрологии - {df['Astrology_grade'].std()}")

print(f"Средняя оценка по английскому языку - {df['English_language_grade'].mean()}")
print(f"Медианная оценка по английскому языку - {df['English_language_grade'].median()}")
print(f"Стандартное отклонение оценки по английскому языку - {df['English_language_grade'].std()}")

print(f"Средняя оценка по истории - {df['Story_grade'].mean()}")
print(f"Медианная оценка по истории - {df['Story_grade'].median()}")
print(f"Стандартное отклонение оценки по истории - {df['Story_grade'].std()}")

