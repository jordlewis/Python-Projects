
#This will import the sqlite3 functionality
import sqlite3

#This will create a database named "test_2", with nothing in it
conn = sqlite3.connect('test_2.db')


#This is a "with" loop, meaning that while the connection is open the following
#code will run until it is closed
with conn:
    #This line will shorten "conn.cursor()" to just "curs" for ease of execution
    curs = conn.cursor()
    #This SQL statement creates a table named "tbl_txt_docs" within database test_2
    curs.execute("CREATE TABLE IF NOT EXISTS tbl_txt_docs(\
    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
    col_fileName TEXT)")    #This creates a column with a string value
    #This will save (commit) the work put into creating the table
    conn.commit()
#This will close the connection to the test_2 database, effectively stopping the "with" loop
conn.close()


#This is a multi-element tuple that the script will examine to print out any element with ".txt" at the end
fileList = ('information.docx','Hello.txt','myImage.png',\
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')


#This establishes the connection with the test_2 database
conn = sqlite3.connect('test_2.db')


#This "for" loop will look over the fileList tuple and checks which elements have ".txt" at the end of it and prints the results
for x in fileList:
    if x.endswith('.txt'): #checks for elements ending in ".txt"
        with conn:
            curs = conn.cursor()
            #This will insert the ".txt" files into tbl_txt_docs, inside of database test_2
            curs.execute("INSERT INTO tbl_txt_docs (col_fileName) VALUES (?)", (x,)) #This creates a 1 value tuple (per element)that can be concatenated
            print(x) #This prints the elements ending in ".txt"
#This closes out the connection to database test_2
conn.close()
