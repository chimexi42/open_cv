import  psycopg2
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import sqlite3
from psycopg2._psycopg import BINARY, NUMBER, STRING, DATETIME, ROWID
import pymongo

# engine = create_engine("postgres://postgres:chimexi42@localhost:5432/practice")
frame = pd.DataFrame(np.random.random((4,4)),
    index=['exp1','exp2','exp3','exp4'],
    columns=['feb','mar','apr','may'])

print(frame)

# client = MongoClient('localhost', 27017)