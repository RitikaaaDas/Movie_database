import sqlite3

# Connect to SQLite database
print("Connection Successful! \n")
cur = sqlite3.connect('MOVIE.db')

# Create table (Movie)
table_creation = '''CREATE TABLE MOVIE
                    (MOVIE_ID INT PRIMARY KEY NOT NULL,
                    MOVIE_NAME TEXT NOT NULL,
                    ACTOR TEXT NOT NULL,
                    ACTRESS TEXT NOT NULL,
                    YEAR_RELEASED INT NOT NULL,
                    DIRECTOR_NAME TEXT NOT NULL);'''

print("Table Created Successfully! \n")
cur.execute(table_creation)


# Inserting data table
row1 = '''INSERT INTO MOVIE 
            (MOVIE_ID,MOVIE_NAME,ACTOR,ACTRESS,YEAR_RELEASED,DIRECTOR_NAME)
            VALUES
            (1,'Shershah','Sidharth Malhotra',
            'Kiara Advani',2021,'Vishnuvardhan');'''

row2 = '''INSERT INTO MOVIE 
            (MOVIE_ID,MOVIE_NAME,ACTOR,ACTRESS,YEAR_RELEASED,DIRECTOR_NAME)
            VALUES
            (2,'Gabbar is Back','Akshay Kumar',
            'Shruti Hassan',2015,'Krish Jagarlamudi');'''
    
row3 = '''INSERT INTO MOVIE 
            (MOVIE_ID,MOVIE_NAME,ACTOR,ACTRESS,YEAR_RELEASED,DIRECTOR_NAME)
            VALUES
            (3,'Uri: The Surgical Strike','Vicky Kaushal',
            'Yami Gautam',2019,'Aditya Dhar');'''
        
row4 = '''INSERT INTO MOVIE 
            (MOVIE_ID,MOVIE_NAME,ACTOR,ACTRESS,YEAR_RELEASED,DIRECTOR_NAME)
            VALUES
            (4,'Hasee Toh Phasee','Sidharth Malhotra',
            'Parineeti Chopra',2014,'Vinil Mathew');'''
            
row5 = '''INSERT INTO MOVIE 
            (MOVIE_ID,MOVIE_NAME,ACTOR,ACTRESS,YEAR_RELEASED,DIRECTOR_NAME)
            VALUES
            (5,'Band Baaja Baaraat','Ranveer Singh',
            'Anushka Sharma',2010,'Maneesh Sharma');'''
    
cur.execute(row1)
cur.execute(row2)
cur.execute(row3)
cur.execute(row4)
cur.execute(row5)


print("Records Entered Into table successfully! \n")

# Querying all rows from the table
query = cur.execute('''SELECT MOVIE_ID,MOVIE_NAME,ACTOR,
                     ACTRESS,YEAR_RELEASED,DIRECTOR_NAME 
                     FROM MOVIE''')

print("MOVIE_ID \t| MOVIE_NAME \t\t| ACTOR \t\t| ACTRESS \t\t| YEAR_RELEASED | DIRECTOR_NAME")
print("-"*120)

for row in query:
   print(str(row[0])+"\t| "+row[1][:10]+"..\t\t| "+row[2][:10]+"..\t\t| "+row[3][:10]+"..\t\t| "+str(row[4])+"\t\t| "+row[5])
   print("-"*120)

print("\nQuerying records successful! \n");

# Query.
query2 = cur.execute('''SELECT * FROM MOVIE 
                      WHERE
                      ACTOR = "Sidharth Malhotra";''')

print("\nDetails of the movie with 'Actor' as 'Sidharth Malhotra' are- \n")

print("MOVIE_ID \t| MOVIE_NAME \t\t| ACTOR \t\t| ACTRESS \t\t| YEAR_RELEASED | DIRECTOR_NAME")
print("-"*120)
for row in query2:
   print(str(row[0])+"\t| "+row[1][:10]+"..\t\t| "+row[2][:10]+"..\t\t| "+row[3][:10]+"..\t\t| "+str(row[4])+"\t\t| "+row[5])
   print("-"*120)

print("\nQuery successful! \n")

cur.commit()
cur.close()