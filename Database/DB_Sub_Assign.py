
#This will import the sqlite3 functionality
import sqlite3

#This will create a database named "test_2", with nothing in it
conn = sqlite3.connect('test_2.db')


#This is a "with" loop, meaning that while the connection is open the following
#code will run until it is closed
with conn:
    #This line will shorten "conn.cursor()" to just "curs" for ease of execution
    curs = conn.cursor()
    #This SQL statement creates a table named "tbl_txt_docs" within the test_2 database
    curs.execute("CREATE TABLE IF NOT EXISTS tbl_txt_docs(\
    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
    col_fileName TEXT)")
    #This will save, or commit the work that we put into creating the table 
    conn.commit()
#This will close the connection to the test_2 database
conn.close()


fileList = ('information.docx','Hello.txt','myImage.png',\
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

conn = sqlite3.connect('test_2.db')

for x in fileList:
    if x.endswith('.txt'):
        with conn:
            curs = conn.cursor()
            curs.execute("INSERT INTO tbl_txt_docs (col_fileName) VALUES (?)", (x,))
            print(x)
conn.close()
