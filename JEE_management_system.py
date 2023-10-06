#%%

import mysql.connector as sqlconlib
sqlcon = sqlconlib.connect(host="localhost" , user="root" ,passwd="Mysql&6903+;-:")

#Checking if the connection is successful
if sqlcon.is_connected():
    print('Sucessfully Connected to MySQL database')
else:
    print('Error connecting to MySQL database')

#Establishing cursor object
cursor=sqlcon.cursor()
    
cursor.execute("CREATE DATABASE IF NOT EXISTS Student_Data")
cursor.execute("Use Student_Data")

table_reg_creation_query = '''
CREATE TABLE IF NOT EXISTS Registration_Data
(RollNo VARCHAR(10) PRIMARY KEY ,
Student_Name varchar(20) ,
Guardian_Name varchar(20) ,
Age int(3) ,
Date_Of_Birth varchar(11) ,
State varchar(20) ,
Paper varchar(10))
'''
cursor.execute( table_reg_creation_query )


table_marks_creation_query = '''
CREATE TABLE IF NOT EXISTS Marks_Data
(RollNo varchar(10) PRIMARY KEY,
Marks int(5))
'''
cursor.execute( table_marks_creation_query )

table_rank_creation_query = '''
CREATE TABLE IF NOT EXISTS Rank_Data
(RollNo varchar(10) PRIMARY KEY ,
Student_Name varchar(20) ,
Marks int(5) ,
Student_Rank int(5))
'''
cursor.execute( table_rank_creation_query )

states_acronyms_dict = {"Andhra Pradesh":"AP" , "Bihar":"BH" , "Goa":"GA" , "Gujarat":"GU" , "Haryana":"HA" , "Karnataka":"KA" , "Kerala":"KE" , "Madhya Pradesh":"MP" , "Maharashtra":"MH" , "Punjab":"PU" , "Tamil Nadu":"TN" , "Uttar Pradesh":"UP" , "West Bengal":"WB" , "Chandigarh":"CH" , "Delhi":"DH"}
institutes_rank_dict = { 99:"IIT Bombay" , 199:"IIT Delhi" , 299:"IIT Kharagpur" , 399:"IIT Kanpur" , 499:"IIT Madras" }

#Insert record into Registration_Data table
def addentry():
     SNAME = input(" Enter Student's Name : ")
     GNAME = input(" Enter Guardian's Name : ")
     DOB = input(" Enter your Date of Birth (yyyy/mm/dd) : ")
     State = input(" Enter your state : ")
     Paper = input(" Enter your paper(B.Tech/B.Arch) : ")
     Age = int(2022-int(DOB[:4]))
     selection__records_query = 'SELECT * FROM Registration_Data WHERE State= "{}" '.format(State)
     cursor.execute( selection__records_query )
     l = len(cursor.fetchall())
     State_Code = states_acronyms_dict[State]
     RollNo = State_Code + f'{l+1:03}'
     record_insertion_query = 'INSERT INTO Registration_Data VALUES ( "{}" , "{}" , "{}" , {} , "{}" ,"{}" , "{}")'.format( RollNo , SNAME , GNAME , Age , DOB , State , Paper )
     cursor.execute(record_insertion_query)
     sqlcon.commit()
     print("Dear " , SNAME , " you have sucessfully registered for JEE Mains 2022 for paper " , Paper ,". Your Roll Number is " , RollNo)

#Insert record into Marks_Data table using RollNo.
def marks_entry():
     RollNo = input(" Enter Student Roll No. : ")
     Marks = int(input(" Enter Marks : "))
     record_insertion_query = 'INSERT INTO Marks_Data VALUES ( "{}" , {} )'.format(RollNo , Marks)
     cursor.execute(record_insertion_query)
     sqlcon.commit()

#Display all existing records in Registration_Data table
def display():
     cursor.execute("SELECT * FROM Registration_Data")
     existing_records_reg_table = cursor.fetchall()
     if len( existing_records_reg_table ) == 0:
          print( "There are no registrations till now" )
     else:
          print("RollNo","Student Name","Guardian Name","Age","Date of Birth","State","Paper")
          for row in existing_records_reg_table :
               print(row)


#Display details of candidate from Registration_Data table using Roll no.
def candisplay():  
     RollNo = input(" Enter Roll No. : ")
     selection_records_query = 'SELECT * FROM Registration_Data WHERE RollNo = "{}" '.format(RollNo)
     cursor.execute(selection_records_query)
     existing_records_reg_table = cursor.fetchall()
     for row in existing_records_reg_table :
         print("\n Roll Nu. = ", row[0] )
         print(" Student's Name = ", row[1] )
         print(" Guardian's Name = ", row[2] )
         print(" Age = ", row[3] )
         print(" Date of Birth = ", row[4] )
         print(" State = ", row[5] )
         print(" Paper = ", row[6] )


#Update Candidate details in Registration Table
def update():
    while True:
        print(" \n Select the Record to be Updated:- ")
        print(" 1. Student Name ")
        print(" 2. Guardian Name ")
        print(" 3. Age ")
        print(" 4. Date of Birth ")
        print(" 5. Paper ")
        menu = int(input(" Your Choice : "))
        if menu == 1 :
            Roll = input(" Enter Your Roll No. : ")
            NewSname = input(" Enter correct Student Name : ")
            Sname_updation_record_query = 'UPDATE Registration_Data SET Student_Name = "{}" WHERE RollNo = "{}" '.format(NewSname , Roll)
            cursor.execute(Sname_updation_record_query)
            sqlcon.commit()
            print(" Updated ! ! ")
        if menu == 2:
            Roll = input(" Enter Your Roll No. : ")
            NewGname = input(" Enter correct Name : ")
            Gname_updation_record_query = 'UPDATE Registration_Data SET Guardian_Name = "{}" WHERE RollNo = "{}" '.format(NewGname , Roll)
            cursor.execute(Gname_updation_record_query)
            sqlcon.commit()
            print(" Updated ! ! ")
        if menu==3:
            Roll = input(" Enter Your Roll No. : ")
            NewAge = int(input(" Enter correct Age : "))
            Age_updation_record_query = 'UPDATE Registration_Data SET Age = {} WHERE Rollno = "{}" '.format(NewAge , Roll)
            cursor.execute(Age_updation_record_query)
            sqlcon.commit()
            print(" Updated ! ! ")
        if menu==4:
            Roll = input(" Enter Your Roll No. : ")
            NewDOB = input(" Enter correct Date of Birth : ")
            DOB_updation_record_query = 'UPDATE Registration_Data SET Date_Of_Birth = "{}" WHERE RollNo = "{}" '.format(NewDOB , Roll)
            cursor.execute(DOB_updation_record_query)
            sqlcon.commit()
            print(" Updated ! ! ")
        if menu==5:
            Roll = input(" Enter Your Roll No. : ")
            NewPaper = input(" Enter correct Paper : ")
            Paper_updation_record_query = 'UPDATE Registration_Data SET Paper = "{}" WHERE RollNo = "{}" '.format(NewPaper , Roll)
            cursor.execute(Paper_updation_record_query)
            sqlcon.commit()
            print(" Updated ! ! ")
        e = input("\n Do You Want To Go Back To Updation Menu ? (y/n) : ")
        if e == "n":
            break

     
def state_data():
     State = input(" Enter State Name : ")
     selection_record_query = 'SELECT * FROM Registration_Data WHERE State = "{}" '.format(State)
     cursor.execute(selection_record_query)
     all_records_of_state = cursor.fetchall()
     print("All Student Data for " , State , " :- ")
     print("RollNo" , "Student Name" , "Guardian Name" , "Age" , "Date of Birth" , "State" , "Paper")
     for row in all_records_of_state :
          print(row)

         
def age_data():
    Order = input("What kind of order Acesnding(a)/Decreasing(d)? : ")
    if Order == 'a':
        order = 'asc'
    elif Order == 'd':
        order = 'desc'
    selection_record_query = 'SELECT * FROM Registration_Data ORDER BY Age '+order+';' 
    cursor.execute(selection_record_query)
    all_records_reg = cursor.fetchall()
    print("RollNo" , "Student Name" , "Guardian Name" , "Age" , "Date of Birth" , "State" , "Paper")
    for row in all_records_reg :
        print(row)
   

#Display All India Rankings of All Students
def rankall():
     cursor.execute("SELECT * FROM Rank_Data ORDER BY Student_Rank")
     all_records_rank = cursor.fetchall()
     print("RollNo","Student Name","Marks","Rank")
     for row in all_records_rank :
          print(row)
  
#Display Student Marks and Rank        
def rankstu():   
     RollNo = input('Enter Roll No. : ')
     selection_record_query = 'SELECT * FROM Rank_Data WHERE RollNo = "{}" '.format(RollNo)
     cursor.execute(selection_record_query)
     record_rank = cursor.fetchall()
     for i in record_rank :
         print("Congratulations! ",i[1]," You have scored ",i[2]," marks in JEE Mains. You have secured a rank of ",i[3])

# Displaying institutes where candidate is eleigible to apply according to rank
def seatallo():
    RollNo = input(" Enter Roll No. : ")
    selection_record_query = 'SELECT * FROM Rank_Data WHERE RollNo = "{}" '.format(RollNo)
    cursor.execute(selection_record_query)
    records_rank = cursor.fetchall()
    for row in records_rank :
        Rank = row[3]
        Sname = row[1]
        print("Congratulations! ", Sname ,"\n Colleges Available are-")
        for i in institutes_rank_dict :
             if Rank <= i:
                  print( institutes_rank_dict[i])


    
        
#Generating Menu And Running The Application
while True:
    print("\n Main Menu")
    print("1. Candidate Registration")
    print("2. Display all existing Registration Records")
    print("3. Display Record for particular candidate using RollNo")
    print("4. Editing of Candidate Registration Data")
    print("5. State wise candidate data")
    print("6. Age wise candidate data")
    print("7. Enter Candidate Marks")
    print("8. All India Rankings")
    print("9. Student ranking")
    print("10. Seat Allocation")
    print("11. Exit")
    choice = int(input("\n Enter your Choice: "))
    if choice == 1:
        addentry()
    elif choice == 2:
        display()
    elif choice == 3:
        candisplay()
    elif choice == 4:
        update()
    elif choice == 5:
        state_data()
    elif choice == 6:
        age_data()
    elif choice == 7:
        marks_entry()
    elif choice == 8:
        rankall()
    elif choice == 9:
        rankstu()
    elif choice == 10:
        seatallo()
    elif choice == 11:
        print("Thank you for appearing in JEE Mains")
        break
    else :
        print('Please enter correct number listed in the menu.')
        continue
        




