

def student_Info():
    print("*** Student Personal Information *** ")
    Name=input("Enter the student's Name : ")
    Age=int(input("Enter the student's Age : "))
    Mobile_Number=input("Enter the student's Mobile_Number : ")
    Email_Id=input("Enter the student's Email_Id : ")
    Department=input("Enter student's Department : ")
    Roll_Number=input("Enter student's Roll_Number : ")
    City=input("Enter student's City : ")

    print("*** Student Marks *** ")

    Python=float(input(f"Enter Python Marks : "))
    Java=float(input("Enter Java Marks: "))
    Data_Base=float(input("Enter Data Base Marks : "))
    Data_Science=float(input("Enter Data Science : "))
    Web_Development=float(input("Enter Web Development : "))
    
    Total_Marks=Python+Java+Data_Base+Data_Science+Web_Development
    Avg_Marks=Total_Marks/5
    if (int(Python)>= 35 & int(Java)>= 35 & int(Data_Base)>= 35 & int(Data_Science)>= 35 & int(Web_Development) >= 35):
        Result="Pass"
        if Avg_Marks>=75:
            Grade="Distinction"
        elif (Avg_Marks>=60 & Avg_Marks<75):
            Grade="First Class"
        elif (Avg_Marks>=50 & Avg_Marks<60):
            Grade="Second Class"
    else:
        Result="Fail"
        Grade="Fail"     
    
    print("Student personal information : ")
    print(f"Full Name : {Name}")
    print(f"Age : {Age}")
    print(f"Mobile Number : {Mobile_Number}")
    print(f"Email Id : {Email_Id}")
    print(f"Department : {Department}")
    print(f"Roll Number : {Roll_Number}")
    print(f"City : {City}")
    
    print("Student Marks for 5 subjects : " )
    print(f"Python : {Python},Java : {Java},Database : {Data_Base}, Data Science : {Data_Science}, Web Development : {Web_Development}")
    print(f"Total Marks : {Total_Marks}, Average marks : {Avg_Marks}, Result : {Result}, Grade : {Grade}")

if(__name__=="__main__"):
    value=1
    while True:
        
        if value==1:
            student_Info()
        elif value==2:
            break
        else:
            print("Enter a valid option")
        
        print("Choose below options")
        print("""
            1 --> Enter Student Information
            2 --> There is no more students to enter details
            """)
        value=int(input("Enter An option : ")) 
        