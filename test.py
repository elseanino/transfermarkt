from config import config
from dataframe import dataframe
from connection import connect
from connection import close

# Get path
dict_path = config(section='path')
path = dict_path['path']

print(dataframe(path))

conn = connect()
close(conn)

print(conn)
