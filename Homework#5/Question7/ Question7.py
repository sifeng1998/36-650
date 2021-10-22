# Question7
conn = psycopg2.connect(host="localhost", 
                        port="5432", 
                        user="postgres", 
                        password="19981208", 
                        database="postgres"
                       )
cur = conn.cursor()

#Creating table as per requirement


sql = '''Insert into EMPLOYEE (ID, FNAME, LNAME) VALUES
(generate_series(1,500),
substr(MD5(random()::text),0,10),
substr(MD5(random()::text),0,10))'''

cur.execute(sql)


print("Dummy variables created successfully.")
conn.commit()

    
cur.close()
conn.close()