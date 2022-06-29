import pandas as pd

snames = ['chioma', 'joshua', 'moses', 'prince', 'yusuf']
mathscore = [88, 77, 90, 67, 80]
chemscore = [57, 73, 84, 77, 95]
bioscore = [30, 58, 88, 69, 55]

studentResults = pd.DataFrame()

studentResults['Name'] = snames
studentResults['Math'] = mathscore
studentResults['Chem'] = chemscore
studentResults['Bio'] = bioscore

# print(studentResults)
# studentResults.to_csv("studentResults.csv")

df = pd.read_csv('studentResults.csv')
print(df)
print(df.columns)

header_list = list(df.columns)
print(header_list)

subdf = df[['Name', 'Math', 'Chem', 'Bio']]

print(subdf)

myname = input("What is your name? ")
print("Hi " + myname + ", I'm glad to say: Hello world!")
