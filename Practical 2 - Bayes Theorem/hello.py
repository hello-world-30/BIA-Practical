import pandas as pd
import numpy as np

df = pd.read_csv(r"D:\530068 TY\Practical 2 - Bayes Theorem\student-mat1.csv", delimiter=";")

# print(df.head(3))

df = pd.DataFrame(df)

df['grade_A'] = np.where(df['G3'] * 5 >= 80,1,0)

df['highabsences'] = np.where(df['absences'] >= 10,1,0)

df['count'] = 1

df = df[['grade_A', 'highabsences', 'count']]

print(df)

pt = pd.pivot_table(
    df, 
    values='count',
    index=['grade_A'],
    columns=['highabsences'],
    aggfunc=np.size,
    fill_value=0
)

print(pt)




total = pt[0][0] + pt[0][1] + pt[1][0] + pt[1][1]
P_A = (pt[0][1] + pt[1][1])/total

P_B = (pt[1][0] + pt[1][1])/total

P_A_when_B_given = pt[1][1]/total

print(P_A)
print(P_B)
print(P_A_when_B_given)


P_gradeA_when_highabsences = (P_A_when_B_given * P_B)/P_A

print(P_gradeA_when_highabsences)