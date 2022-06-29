import numpy as np
import pandas as pd
from lxml import objectify
import json
from pandas.io.json import json_normalize
# from pandas.io.pytables import HDFStore
import pickle
from sqlalchemy import create_engine
import sqlite3
import psycopg2


csvframe = pd.read_csv("ch01_01.csv")
print(csvframe)

print(pd.read_table("ch01_01.csv", sep=','))

print(pd.read_csv('ch05_02.csv', header=None))
print()
print(pd.read_csv('ch05_02.csv', names= ['white', 'red', 'blue', 'green', 'animal']))
print()
print(pd.read_csv('ch05_03.csv', index_col=['color', 'status']))

print(pd.read_table('ch05_04.txt', sep='\s+', engine='python'))
print()

print(pd.read_table("ch05_05.txt", sep ="\D+", header=None, engine='python'))

log_file = pd.read_table("ch05_06.txt", sep=',', skiprows=[0,1,3,6])
print(log_file)

print()
df = pd.read_csv('ch05_02.csv', skiprows=[2], nrows=3, header=None)
print(df)


out = pd.Series()
i = 0
pieces = pd.read_csv('ch01_01.csv', chunksize=3)
for piece in pieces:
    out._set_value(i, piece['white'].sum())
    i = i+1
print(out)

frame = pd.DataFrame(np.arange(16).reshape((4,4)),
                     index=['red', 'blue', 'yellow', 'white'],
                     columns= ['ball', 'pen', 'pencil', 'paper'])

frame.to_csv('ch05_07.csv')
frame.to_csv('ch05_07b.csv', index= False, header= False)
print(frame)

frame3 = pd.DataFrame([[6,np.nan,np.nan,6,np.nan],
    [np.nan,np.nan,np.nan,np.nan,np.nan],
    [np.nan,np.nan,np.nan,np.nan,np.nan],
    [20,np.nan,np.nan,20.0,np.nan],
    [19,np.nan,np.nan,19.0,np.nan]
    ], index=['blue','green','red','white','yellow'],
       columns=['ball','mug','paper','pen','pencil'])

print(frame3)
frame3.to_csv("ch05_08.csv")
frame3.to_csv("ch05_09.csv", na_rep= 'NaN')

frame = pd.DataFrame(np.arange(4).reshape(2,2))

print(frame.to_html())
print()

frame = pd.DataFrame( np.random.random((4,4)),
    index = ['white','black','red','blue'],
    columns = ['up','down','right','left'])
print(frame)

s = ['<HTML>']
s.append('<HEAD><TITLE>My DataFrame</TITLE></HEAD>')
s.append('<BODY>')
s.append(frame.to_html())
s.append('</BODY></HTML>')
html = "".join(s)

html_file = open('my_frame.html', 'w')
html_file.write(html)
html_file.close()

print()
print(pd.read_html("my_frame.html")[0])

xml = objectify.parse('books.xml')
print(xml)
root = xml.getroot()
print(root.Book.Author)
print(root.Book.PublishDate)

print([child.tag for child in root.Book.getchildren()])
print()

frame = pd.DataFrame(np.random.random((4,4)),
    index = ['exp1','exp2','exp3','exp4'],
    columns = ['Jan2015','Fab2015','Mar2015','Apr2005'])
print(frame)

frame.to_excel('data2.xlsx')


frame = pd.DataFrame(np.arange(16).reshape(4,4),
    index=['white','black','red','blue'],
    columns=['up','down','right','left'])
frame.to_json('frame.json')

print(pd.read_json('frame.json'))
file = open('books.json', 'r')
text = file.read()
text = json.loads(text)
print(text)

print(json_normalize(text, 'books'))

print(json_normalize(text,'books',['nationality','writer']))

# HDF5 (Hierachial data format) for handling binary data format

# frame = pd.DataFrame(np.arange(16).reshape(4,4),
#     index=['white','black','red','blue'],
#     columns=['up','down','right','left'])
#
# store = HDFStore('mydata.h5')
# store['obj1'] = frame
# store['obj2'] = frame

data = {'color': ['white','red'], 'value':[5,7]}
pickled_data = pickle.dumps(data)

print(pickled_data)

nframe = pickle.loads(pickled_data)
print(nframe)

# Pickle in pandas for serialization
frame = pd.DataFrame(np.arange(16).reshape(4,4),
                    index =['up','down','left','right'])

frame.to_pickle('frame.pkl')

df = pd.read_pickle('frame.pkl')
print(df)

# interacting with databases

# engine = create_engine('postgresql://scott:tiger@localhost:5432/mydatabase')

frame = pd.DataFrame( np.arange(20).reshape(4,5),
    columns=['white','red','blue','black','green'])
print(frame)

engine = create_engine('sqlite:///foo.db')

# frame.to_sql('colors', engine)
print(pd.read_sql('colors', engine))

# query1 = """ Drop table test"""
query2 = """
 
    CREATE TABLE test(
     a VARCHAR(20),
     b VARCHAR(20),
     c REAL, 
     d INTEGER
    );
"""

con = sqlite3.connect(':memory:')
# con.execute(query1)
con.execute(query2)


data = [('white','up',1,3),
    ('black','down',2,8),
    ('green','up',4,4),
    ('red','down',5,5)]

stmt = "INSERT INTO test VALUES(?,?,?,?)"
con.executemany(stmt, data)
cursor = con.execute("Select * from test")
print(cursor)

rows = cursor.fetchall()
print(rows)
con.commit()











































































