# Question 6
#In the first section, Python will check if you need to install Pscycopg2 library and install it.
import subprocess
import sys

import psycopg2

#tweak the database parameters to match your specific postgres database.
conn = psycopg2.connect(host="localhost", 
                        port="5432", 
                        user="postgres", 
                        password="19981208", 
                        database="postgres"
                       )
cur = conn.cursor()

#Creating table as per requirement
sql ='''CREATE TABLE EMPLOYEE(
   ID SERIAL,
   FNAME VARCHAR(10),
   LNAME VARCHAR(10)
)'''
cur.execute(sql)


print("Table created successfully.")
conn.commit()
    
cur.close()
conn.close()