import mysql.connector
import sys

global conn,cursor;

conn=mysql.connector.connect(host="localhost",user="root",db="users181041008",password="root",)
def connection():
	if conn.is_connected():
		print("Connected to database")
	else:
		print("Not connected")

def Insertion(ID,Fname,Lname,DOB):
	query="insert into users181041008('ID','Fname','Lname','DOB') values('%s','%s','%s','%s')"
	args=(ID,Fname,Lname,DOB);
	mycursor = conn.cursor();	
	mycursor.execute(query,args);
	conn.commit();




def Retrive_all():
	query="Select *from users181041008"
	mycursor=conn.cursor();
	mycursor.execute(query);
	rows=cursor.fetchall();

	for row in rows:
		print(row)




def Alter_table():
	query="Alter users181041008 add constraint %s"
	args=(attribute);
	mycursor=conn.cursor();
	mycursor.execute(query,args);
	conn.commit();






def main():
	connection()
	print("Choose an operation to perform ")
	print("1:Insertion \n")
	print("2:Retrieve all \n")
	print("3:Alter Table \n")
	print("q:Quit \n")
	option=input("Select any : ")
	while(True):
		if(option=='1'):
			ID=input("Enter ID : ")
			Fname=input("Enter First name : ")
			Lname=input("Enter Last name : ")
			DOB=input("Enter DOB : ")
			Insertion(ID,Fname,Lname,DOB)
		elif(option=='2'):
			Retrive_all()
		elif(option=='3'):
			Alter_table()
		elif(option=='q'):
			sys.exit()
		else:
			print("You have Entered wrong option")

if __name__=='__main__':
	main()