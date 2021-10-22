# Question 8
conn = psycopg2.connect(host="localhost", 
                        port="5432", 
                        user="postgres", 
                        password="19981208", 
                        database="postgres"
                       )
cur = conn.cursor()

#Creating table as per requirement


sql = '''SELECT * FROM EMPLOYEE LIMIT 10'''

cur.execute(sql)


print("Data Visualization successfully.")
conn.commit()

    
cur.close()
conn.close()