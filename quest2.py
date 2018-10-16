import mysql.connector
import sys

global conn,cursor;

conn=mysql.connector.connect(host="localhost",user="root",db="users181041008",password="root",)
def connection():
	if conn.is_connected():
		print("Connected to database")
	else:
		print("Not connected")

def Insertion():
	ID=input("Enter ID : ")
	Fname=input("Enter First name : ")
	Lname=input("Enter Last name : ")
	DOB=input("Enter DOB : ")
	query="INSERT INTO users181041008(ID,Fname,Lname,DOB) VALUES(%s,%s,%s,%s)"
	args=(ID,Fname,Lname,DOB);
	mycursor = conn.cursor();	
	mycursor.execute(query,args);
	conn.commit();




def Retrive_all():
	query="SELECT *from users181041008"
	mycursor = conn.cursor();
	mycursor.execute(query);
	rows = mycursor.fetchall();
	print("No of Record: ", mycursor.rowcount)
	#print(rows)
	for row in rows:
		print(row);




def Alter_table(attribute):
	query="ALTER TABLE users181041008 ADD %s varchar(50)"%(attribute)
	#args=(attribute);
	mycursor=conn.cursor();
	mycursor.execute(query);
	print("Successfully altered ")
	conn.commit();



def main():
	while(True):
		connection()
		print("Choose an operation to perform ")
		print("1:Insertion \n")
		print("2:Retrieve all \n")
		print("3:Alter Table \n")
		print("q:Quit \n")
		option=input("Select any : ")
	
		if(option=='1'):
			Insertion();
		elif(option=='2'):
			Retrive_all()
			
		elif(option=='3'):
			attribute=input("Mention the attribute to add in table :")
			Alter_table(attribute)
			
		elif(option=='q'):
			sys.exit()
		else:
			print("You have Entered wrong option")

if __name__=='__main__':
	main()
