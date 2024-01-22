from tkinter import *
from turtle import left
from PIL import ImageTk
from tkinter import messagebox, ttk
import pymysql
import datetime


class Login:

   def __init__(self,root):
      self.root=root
      self.root.title("Enrollment System")
      self.root.geometry("1366x700+0+0")
      
      self.root.resizable(False,False)
      self.loginform()

   def loginform(self):
      Frame_login=Frame(self.root,bg="white")
      Frame_login.place(x=0,y=0,height=700,width=1400)
      self.img=ImageTk.PhotoImage(file="rlogo1.png")
      img=Label(Frame_login,image=self.img).place(x=0,y=0,width=1750,height=700)
      
      frame_input=Frame(self.root,bg='#1E90FF')
      frame_input.place(x=270,y=80,height=550,width=350)
      
      label1=Label(frame_input,text="Get's Started",font=('impact',32,'bold'),fg="white",bg='#1E90FF')
      label1.place(x=50,y=20)
      
      label2=Label(frame_input,text="Username",font=("Goudy old style",20,"bold"),fg='white',bg='#1E90FF')
      label2.place(x=30,y=95)

      self.username=Entry(frame_input,font=("times new roman",15,"bold"),bg='lightgray')
      self.username.place(x=30,y=135,width=290,height=35)
      
      label3=Label(frame_input,text="Password",font=("Goudy old style",20,"bold"),fg='white',bg='#1E90FF')
      label3.place(x=30,y=175)
      
      self.password=Entry(frame_input,font=("times new roman",15,"bold"),bg='lightgray')
      self.password.place(x=30,y=215,width=290,height=35)
      
      label4=Label(frame_input,text="Confirm Password",font=("Goudy old style",20,"bold"),fg='white',bg='#1E90FF')
      label4.place(x=30,y=255)
      
      self.confirmpassword=Entry(frame_input,font=("times new roman",15,"bold"),bg='lightgray')
      self.confirmpassword.place(x=30,y=295,width=290,height=35)
      
      #btn1=Button(frame_input,text="forgot password?",cursor='hand2',font=('calibri',10),bg='white',fg='black',bd=0)
      #btn1.place(x=125,y=305)
      
      
      
      btn2=Button(frame_input,text="Login",command=self.login,cursor="hand2",font=("times new roman",15),fg="white",bg="#00008B",bd=0,width=26,height=1)
      btn2.place(x=30,y=345)

      btn3=Button(frame_input,command=self.Register,text="Not Registered?register",cursor="hand2",font=("calibri",10),bg='#DC143C',fg="white",bd=0)
      btn3.place(x=110,y=390)


   def login(self):
      if self.username.get()=="" or self.password.get()=="" or self.confirmpassword.get()=="":
         messagebox.showerror("Error","All fields are required",parent=self.root)
      else:
         try:
            con=pymysql.connect(host='localhost',user='root',password='root',
                                database='portal')
            
            cur=con.cursor()

            cur.execute('select * from register where username=%s and password=%s and confirmpassword=%s',(self.username.get(),self.password.get(), self.confirmpassword.get()))

            row=cur.fetchone()

            if row==None:
               messagebox.showerror('Error','Invalid Username And Password',parent=self.root)

               self.loginclear()
               self.username.focus()

            else:
               self.dashboard()
               con.close()

         except Exception as es:
            messagebox.showerror('Error',f'Error Due to : {str(es)}'
                                 ,parent=self.root)
 

   def Register(self):
      Frame_login1=Frame(self.root,bg="white")
      Frame_login1.place(x=0,y=0,height=700,width=1400)
      
      frame_input2=Frame(self.root,bg='#1E90FF', bd = 10, relief = RIDGE)
      frame_input2.place(x=220,y=35,height=620,width=890)
      self.img2=ImageTk.PhotoImage(file="rlogo2.png")
      img1=Label(frame_input2,image=self.img2, bg = '#1E90FF').place(x=365,y=10,width=105,height=105)

      label1=Label(frame_input2,text="Sign Up",font=('impact',32,'bold'),fg="white",bg='#1E90FF')
      label1.place(x=35,y=15)

      label2=Label(frame_input2,text="Username",font=("Goudy old style",20,"bold"),fg='white',bg='#1E90FF')
      label2.place(x=30,y=95)

      self.entry2=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')
      self.entry2.place(x=30,y=135,width=270,height=35)
      
      label3=Label(frame_input2,text="Email Address",font=("Goudy old style",20,"bold"),fg='white',bg='#1E90FF')
      label3.place(x=30,y=175)

      self.entry3=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')
      self.entry3.place(x=30,y=215,width=270,height=35)

      label4=Label(frame_input2,text="Password",font=("Goudy old style",20,"bold"),fg='white',bg='#1E90FF')
      label4.place(x=30,y=255)

      self.entry4=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')
      self.entry4.place(x=30,y=295,width=270,height=35)

      


      label5=Label(frame_input2,text="Confirm Password",font=("Goudy old style",20,"bold"),fg='white',bg='#1E90FF')
      label5.place(x=30,y=335)

      self.entry5=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')
      self.entry5.place(x=30,y=375,width=270,height=35)
      
      
      
      label6=Label(frame_input2,text="First Name",font=("Goudy old style",18,"bold"),fg='white',bg='#1E90FF')
      label6.place(x=480,y=95)

      self.entry6=Entry(frame_input2,font=("times new roman",13,"bold"),bg='lightgray')
      self.entry6.place(x=480,y=135,width=175,height=35)

      label7=Label(frame_input2,text="Last Name",font=("Goudy old style",18,"bold"),fg='white',bg='#1E90FF')
      label7.place(x=680,y=95)

      self.entry7=Entry(frame_input2,font=("times new roman",13,"bold"),bg='lightgray')
      self.entry7.place(x=680,y=135,width=175,height=35)

      label8=Label(frame_input2,text="Address",font=("Goudy old style",18,"bold"),fg='white',bg='#1E90FF')
      label8.place(x=480,y=175)

      self.entry8=Entry(frame_input2,font=("times new roman",13,"bold"),bg='lightgray')
      self.entry8.place(x=480,y=215,width=175,height=35)


      label9=Label(frame_input2,text="Phone Number",font=("Goudy old style",18,"bold"),fg='white',bg='#1E90FF')
      label9.place(x=680,y=175)

      self.entry9=Entry(frame_input2,font=("times new roman",13,"bold"),bg='lightgray')
      self.entry9.place(x=680,y=215,width=175,height=35)
      
      label10=Label(frame_input2,text="Year Level",font=("Goudy old style",18,"bold"),fg='white',bg='#1E90FF')
      label10.place(x=480,y=255)

      self.entry10=Entry(frame_input2,font=("times new roman",13,"bold"),bg='lightgray')
      self.entry10.place(x=480,y=295,width=175,height=35)


      label11=Label(frame_input2,text="Course",font=("Goudy old style",18,"bold"),fg='white',bg='#1E90FF')
      label11.place(x=680,y=255)

      self.entry11=Entry(frame_input2,font=("times new roman",13,"bold"),bg='lightgray')
      self.entry11.place(x=680,y=295,width=175,height=35)
      

      btn2=Button(frame_input2,command=self.register,text="Register",cursor="hand2",font=("times new roman",15),fg="white",
                  bg="#00008B",bd=0,width=15,height=1)
      btn2.place(x=330,y=460)
        
      btn3=Button(frame_input2,command=self.loginform,text="Already Registered?Login",cursor="hand2",
                  font=("calibri",10),bg='#DC143C',fg="white",bd=0)
      btn3.place(x=342,y=500)


   def register(self):
      if self.entry2.get()==""or self.entry3.get()==""or self.entry4.get()==""or self.entry5.get()=="" or self.entry6.get()==""or self.entry7.get()==""or self.entry8.get()==""or self.entry9.get()=="" or self.entry10.get()==""or self.entry11.get()=="":
         messagebox.showerror("Error","All Fields Are Required",parent=self.root)
      elif self.entry4.get()!=self.entry5.get():
         messagebox.showerror("Error","Password and Confirm Password Should Be Same"
                              ,parent=self.root)
      elif "@" not in self.entry3.get() or len(self.entry3.get()) <= 12:
          messagebox.showerror("Error","Invalid Email Address"
                              ,parent=self.root)
      elif len(self.entry9.get()) < 11:
          messagebox.showerror("Error","Invalid Phone Number"
                              ,parent=self.root)
      else:
         try:
            con=pymysql.connect(host="localhost",user="root",password="root",
                                database="portal")
            
            
         except:
            con=pymysql.connect(host="localhost",user="root",password="root")
            
            cur=con.cursor()
            cur.execute("CREATE DATABASE portal")
            
            try:
               con=pymysql.connect(host="localhost",user="root",password="root",
                                 database="portal")
               
               cur=con.cursor()
               cur.execute("CREATE TABLE register(firstname char(200), lastname char(200), username char(200), emailaddress char(200), password char(200), confirmpassword char(200), address char(255), phonenumber char(13), yearlevel char(50), course char(100))")
               
               
            except Exception as es:
               messagebox.showerror("Error",f"Error due to:{str(es)}"
                                    ,parent=self.root)
            
            
         
         try:
            con=pymysql.connect(host="localhost",user="root",password="root",
                                database="portal")
            cur=con.cursor()
            cur.execute("select * from register where emailaddress=%s"
                        ,self.entry3.get())
            
            row=cur.fetchone()
            
            cur2=con.cursor()
            cur2.execute("select * from register where username=%s"
                        ,self.entry2.get())
            
            row2=cur2.fetchone()
            
            if row!=None or row2!=None:
               messagebox.showerror("Error"
               ,"User already Exist,Please try with another Email / Username"
                                    ,parent=self.root)
               self.regclear()
               self.entry2.focus()
            else:
               cur.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                           ,(self.entry6.get(),self.entry7.get(),self.entry2.get(),self.entry3.get(),self.entry4.get(),self.entry5.get(),self.entry8.get(),self.entry9.get(),self.entry10.get(),self.entry11.get()))
               con.commit()
               con.close()
               messagebox.showinfo("Success","Register Succesfull"
                                   ,parent=self.root)
               self.regclear()
         except Exception as es:
            messagebox.showerror("Error",f"Error due to:{str(es)}"
                                 ,parent=self.root)


   def dashboard(self):
      Frame_login=Frame(self.root,bd = 10,relief = RIDGE, bg = "#1E90FF")
      Frame_login.place(x=0,y=0,height=700,width=1366)
      
      dashboardtop=Frame(Frame_login, bg = "white", height = 47, width = 1000, bd = 5)
      dashboardtop.pack(side = TOP, expand="yes")
      
      dashboard=Frame(Frame_login, bg = "white", height = 180, width = 1000, bd = 5, relief = RIDGE)
      dashboard.pack(side = TOP, expand="yes")
      
      dashboard2=Frame(Frame_login, bg = "white", height = 473, width = 1000, bd = 5)
      dashboard2.pack(side = BOTTOM, expand="yes")

      
      try:
         con=pymysql.connect(host="localhost",user="root",password="root",
                              database="portal")
         cur=con.cursor()
         cur.execute("select * from register where username=%s"
                        ,self.username.get())
         row=cur.fetchone()
         
         data = []
         for x in row:
            data.append(x)
            
         print(data)

      except Exception as es:
         messagebox.showerror("Error",f"Error due to:{str(es)}"
                              ,parent=self.root)
         
      year = datetime.datetime.today().year
      
      label1=Label(dashboard,text=(data[1].upper() + ", " + data[0].upper()),font=('times new roman',15,'bold'),fg="black",bg='white')
      label1.place(x = 40, y = 20)

      label2=Label(dashboard,text=(data[3]),font=('times new roman',15,'bold'),fg="black",bg='white')
      label2.place(x = 40, y = 50)
      
      label3=Label(dashboard,text=(data[7]),font=('times new roman',15,'bold'),fg="black",bg='white')
      label3.place(x = 40, y = 80)
      
      label4=Label(dashboard,text=(data[6]),font=('times new roman',15,'bold'),fg="black",bg='white')
      label4.place(x = 40, y = 110)
      
      label5=Label(dashboard,text=("Academic Year " + str(year) + " - " + str(year+1)),font=('times new roman',15,'bold'),fg="black",bg='white')
      label5.place(x = 540, y = 20)
      
      label6=Label(dashboard,text=("Allison International School - Main Campus"),font=('times new roman',15,'bold'),fg="black",bg='white')
      label6.place(x = 540, y = 50)
      
      label7=Label(dashboard,text=(data[9].upper() + " - " + data[8].upper()),font=('times new roman',15,'bold'),fg="black",bg='white')
      label7.place(x = 540, y = 80)
      
      label8=Label(dashboard,text=("Status: "),font=('times new roman',15,'bold'),fg="black",bg='white')
      label8.place(x = 540, y = 110)
      
      label9=Label(dashboard,text=("ENROLLED"),font=('times new roman',15,'bold'),fg="#008000",bg='white')
      label9.place(x = 630, y = 110)
      
      label10=Label(dashboardtop,text=("Welcome to Allison International School"),font=('times new roman',20,'bold'),fg="#00008B",bg='white')
      label10.place(x = 40, y = 0)

      btn2=Button(dashboardtop,text="Logout",command=self.loginform,cursor="hand2",font=("times new roman",15),fg="white",bg="#DC143C",bd=0,width=15,height=1)
      btn2.place(x = 816, y = 0)
      
      btn3=Button(dashboard2,command=self.COR,text="COR",cursor="hand2",font=("times new roman",15),fg="white",
                  bg="#00008B",bd=0,width=15,height=1)
      btn3.place(x=40,y=10)
      
      btn4=Button(dashboard2,command = self.Liabilities, text="Liabilities",cursor="hand2",font=("times new roman",15),fg="white",
                  bg="#00008B",bd=0,width=15,height=1)
      btn4.place(x=40,y=60)
      
      
      btnclub1=Button(dashboard2,command = self.Club,text="BasketBall \nClub",cursor="hand2",font=("times new roman",15),fg="white",
                  bg="#00008B",bd=0,width=15,height=3)
      btnclub1.place(x=290,y=10)
      
      btnclub2=Button(dashboard2,command = self.Club,text="VolleyBall \nClub",cursor="hand2",font=("times new roman",15),fg="white",
                  bg="#00008B",bd=0,width=15,height=3)
      btnclub2.place(x=290,y=95)
      
      btnclub3=Button(dashboard2,command = self.Club,text="Taekwondo \nClub",cursor="hand2",font=("times new roman",15),fg="white",
                  bg="#00008B",bd=0,width=15,height=3)
      btnclub3.place(x=290,y=180)
      
      btnclub4=Button(dashboard2,command = self.Club,text="Dancing \nClub",cursor="hand2",font=("times new roman",15),fg="white",
                  bg="#00008B",bd=0,width=15,height=3)
      btnclub4.place(x=290,y=265)
      
      btnclub5=Button(dashboard2,command = self.Club,text="Painting \nClub",cursor="hand2",font=("times new roman",15),fg="white",
                  bg="#00008B",bd=0,width=15,height=3)
      btnclub5.place(x=290,y=350)
      
      labelmission=Label(dashboard2,text=("MISSION"),font=('times new roman',20,'bold'),fg="#DC143C",bg='white')
      labelmission.place(x = 675, y = 0)
      
      labelmission1=Label(dashboard2,text=('''To create, share, and apply knowledge in Technologies and Informations, 
                                           \nincluding in interdisciplinary areas that benefit humanity and society; 
                                           \nto educate students from diverse backgrounds to be successful, ethical, 
                                           \nand effective problem-solvers and professional leaders who will contribute 
                                           \npositively to our school, state, nation and the world and to  
                                           \nprovide every student with a platform to refine his/ her skills and 
                                           \nmake a mark in the computer literate world.''')
                          ,font=('times new roman',10,'bold'),fg="#00008B",bg='white')
      labelmission1.place(x = 530, y = 35)
      
      labelvision=Label(dashboard2,text=("VISION"),font=('times new roman',20,'bold'),fg="#DC143C",bg='white')
      labelvision.place(x = 688, y = 255)
      
      labelvision1=Label(dashboard2,text=('''The School of Computing and Informatics' vision is to be among the 
                                          \nnation's premier research and teaching programs in Computing and 
                                          \nInformatics, with leadership and recognition in identified focus areas.''')
                          ,font=('times new roman',10,'bold'),fg="#00008B",bg='white')
      labelvision1.place(x = 545, y = 290)
      
      tuition = 0
      tuitionmonth = datetime.datetime.today().month
      
      if "1" in data[8]:
         if tuitionmonth >= 7 and tuitionmonth <=12:
            tuition += 15000
         elif tuitionmonth >= 1 and tuitionmonth <=6:
            tuition += 17000
      elif "2" in data[8]:
         if tuitionmonth >= 7 and tuitionmonth <=12:
            tuition += 13000
         elif tuitionmonth >= 1 and tuitionmonth <=6:
            tuition += 14000
      elif "3" in data[8]:
         if tuitionmonth >= 7 and tuitionmonth <=12:
            tuition += 10000
         elif tuitionmonth >= 1 and tuitionmonth <=6:
            tuition += 12000
      elif "4" in data[8]:
         if tuitionmonth >= 7 and tuitionmonth <=12:
            tuition += 8000
         elif tuitionmonth >= 1 and tuitionmonth <=6:
            tuition += 9000
      else:
         pass      
      
      labeltuition=Label(dashboard2,text=("TUITION: " + "   " + str(tuition)),font=('times new roman',12,'bold'),fg="white",bg='#00008B')
      labeltuition.place(x = 20, y = 415)

      
   def COR(self):
      Frame_cor=Frame(self.root,bd = 10,relief = RIDGE, bg = "#1E90FF")
      Frame_cor.place(x=0,y=0,height=700,width=1366)
      
      dashboardcor=Frame(Frame_cor, bg = "white", height = 473, width = 1000, bd = 5)
      dashboardcor.pack(side = BOTTOM, expand="yes")
      
      btn2=Button(dashboardcor,text="X",command=self.dashboard,cursor="hand2",font=("times new roman",15),fg="white",bg="#DC143C",bd=0,width=15,height=1)
      btn2.place(x = 816, y = 0)
      
      sem = datetime.datetime.today().month
      
      try:
         con=pymysql.connect(host="localhost",user="root",password="root",
                              database="portal")
         cur=con.cursor()
         cur.execute("select * from register where username=%s"
                        ,self.username.get())
         row=cur.fetchone()
         
         data = []
         for x in row:
            data.append(x)
            
         print(data)

      except Exception as es:
         messagebox.showerror("Error",f"Error due to:{str(es)}"
                              ,parent=self.root)
         
      year = datetime.datetime.today().year
      
      subject = []
      code = []
      unit = []
      totalsum = 0
      
      if "1" in data[8]:
         if sem >= 7 and sem <=12:
            subjects = ["Computer Programming 1", "Introduction to Computing (Computational Thinking and Problem Solving)", "Life and Works of Rizal", "Mathematics in the Modern World", "Movement Enhancement", "National Service Training Program 1", "Purposive Communication", "Understanding the self"]
            units = [3, 3, 3, 3, 2, 3, 3, 3]
            codes = ["ITE 260", "ITE 288", "HIS 007", "MAT 152", "PED 025", "NST 021", "GEN 001", "GEN 002"]
            
            for x in subjects:
               subject.append(x)
            for y in units:
               unit.append(y)
            for z in codes:
               code.append(z)
               
            totalsum = sum(units)
               
         elif sem >= 1 and sem <=6:
            subjects = ["Computer Programming 2", "Human Computer Interaction", "Fitness Exercices", "National Service Training Program 2", "Science, Techonology and Society", "Art Appreciation", "Readings in Philippine History", "The Contemporary World"]
            units = [3, 3, 2, 3, 3, 3, 3, 3]
            codes = ["ITE 186", "ITE 291", "PED 026", "NST 022", "GEN 003", "ART 002", "GEN 004", "GEN 005"]
            
            for x in subjects:
               subject.append(x)
            for y in units:
               unit.append(y)
            for z in codes:
               code.append(z)
               
            totalsum = sum(units)
         
      elif "2" in data[8]:
         if sem >= 7 and sem <=12:
            subjects = ["Data Structures and Algorithms 1 " , "Discrete Mathematics 1", "Networking 1", "Object Oriented Programming 1", "Business Communication 1", "Ethics 1", "Physical Activities Towards Health 1", "Student Success Program 1", "Great Books 1"]
            units = [3, 3, 3, 3, 3, 3, 2, 1, 3]
            codes = ["ITE 031", "ITE 048", "ITE 292", "ITE 300","GEN 006", "BAM 006", "PED 027", "SSP 005", "LIT 044"]
            
            for x in subjects:
               subject.append(x)
            for y in units:
               unit.append(y)
            for z in codes:
               code.append(z)
               
            totalsum = sum(units)
               
         elif sem >= 1 and sem <=6:
            subjects = ["Data Structures and Algorithms 2" , "Discrete Mathematics 2", "Networking 2", "Object Oriented Programming 2", "Business Communication 2", "Ethics 2", "Physical Activities Towards Health 2", "Student Success Program 2", "Great Books 2"]
            units = [3, 3, 3, 3, 3, 3, 2, 1, 3]
            codes = ["ITE 031", "ITE 048", "ITE 292", "ITE 300","GEN 006", "BAM 006", "PED 027", "SSP 006", "LIT 044"]
            
            for x in subjects:
               subject.append(x)
            for y in units:
               unit.append(y)
            for z in codes:
               code.append(z)
               
            totalsum = sum(units)
         
      elif "3" in data[8]:
         if sem >= 7 and sem <=12:
            subjects = ["Information Assurance and Securiy 1", "Information Management (Including Fundamentals of Database Systems)", "Living in the IT Era", "Networking 3", "Physical Activities Towards Health and Fitness II", "Social and Professional Issues", "Systems Integration and Architecture 1"]
            units = [3, 3, 3, 3, 2, 3, 3]
            codes = ["ITE 302", "ITE 298", "GEN 008", "ITE 304", "PED 028", "ITE 354", "ITE 303"]
            
            for x in subjects:
               subject.append(x)
            for y in units:
               unit.append(y)
            for z in codes:
               code.append(z)
               
            totalsum = sum(units)

         elif sem >= 1 and sem <=6:
            subjects = ["Application Development and Emerging Technologies", "Capstone Project and Research 1", "Information Technology Education Elective 1", "Integrative Programming and Technologies", "Quantitative Methods (Including Modeling and Simulation", "Student Success Program 3", "Web System and Technologies", "Advanced Database System"]
            units = [3, 3, 3, 3, 2, 1, 3, 3]
            codes = ["ITE 301", "ITE 309", "ITE ELEC1", "ITE 306", "ITE 307", "SSP 007", "ITE 308", "ITE 328"]
            
            for x in subjects:
               subject.append(x)
            for y in units:
               unit.append(y)
            for z in codes:
               code.append(z)
               
            totalsum = sum(units)
         
      elif "4" in data[8]:
         if sem >= 7 and sem <=12:
            subjects = ["Capstone Project and Research 2", "Informaton Assurance and Security 2", "Introduction to Natural Language Processing", "IT Project Management", "Platform Technologie 1 (Cloud)", "Student Success Program 4", "System Administration and Maintenance"]
            units = [3, 3, 3, 3, 3, 1, 3]
            codes = ["ITE 310", "ITE 305", "ITE 374", "ITE 083", "ITE 320", "SSP 008", "ITE 293"]
            
            for x in subjects:
               subject.append(x)
            for y in units:
               unit.append(y)
            for z in codes:
               code.append(z)
               
            totalsum = sum(units)
            
         elif sem >= 1 and sem <=6:
            subjects = ["Current Trend in IT", "Managing IT Resources", "New Venture Creation", "Student Success Program 5", "System Integration and Architecture 2"]
            units = [3, 3, 5, 1, 3]
            codes = ["ITE 193", "ITE 322", "ITE 351", "SSP 009", "ITE 317"]
            
            for x in subjects:
               subject.append(x)
            for y in units:
               unit.append(y)
            for z in codes:
               code.append(z)
               
            totalsum = sum(units)
      else:
         pass
      
      today = datetime.date.today()
         
      labelcourse=Label(dashboardcor,text=("Course: " + data[9]),font=('times new roman',12,'bold'),fg="#00008B",bg='white')
      labelcourse.place(x = 50, y = 70)
      labelname = Label(dashboardcor,text=(data[1].upper() + ", " + data[0].upper()),font=('times new roman',12,'bold'),fg="#00008B",bg='white')
      labelname.place(x = 50, y = 50)
      labelday=Label(dashboardcor,text=(today),font=('times new roman',12,'bold'),fg="#00008B",bg='white')
      labelday.place(x = 740, y = 50)
      labelyear=Label(dashboardcor,text=("Year Level:  " + " " + data[8]),font=('times new roman',12,'bold'),fg="#00008B",bg='white')
      labelyear.place(x = 740, y = 70)
      
      labelcode=Label(dashboardcor,text=("Subject Code"),font=('times new roman',12,'bold'),fg="#00008B",bg='white')
      labelcode.place(x = 50, y = 140)
      labelsub=Label(dashboardcor,text=("Descriptive Title"),font=('times new roman',12,'bold'),fg="#00008B",bg='white')
      labelsub.place(x = 380, y = 140)
      labelunit=Label(dashboardcor,text=("Units"),font=('times new roman',12,'bold'),fg="#00008B",bg='white')
      labelunit.place(x = 824, y = 140)
         
            
      label1=Label(dashboardcor,text=(code[0] + "\t\t" + subjects[0]),font=('times new roman',12,'bold'),fg="#00008B",bg='white')
      label1.place(x = 60, y = 160)
      label2=Label(dashboardcor,text=(units[0]),font=('times new roman',12,'bold'),fg="#00008B",bg='white')
      label2.place(x = 840, y = 160)
      
      label3=Label(dashboardcor,text=(code[1] + "\t\t" + subjects[1]),font=('times new roman',12,'bold'),fg="#00008B",bg='white')
      label3.place(x = 60, y = 180)
      label4=Label(dashboardcor,text=(units[1]),font=('times new roman',12,'bold'),fg="#00008B",bg='white')
      label4.place(x = 840, y = 180)
      
      label5=Label(dashboardcor,text=(code[2] + "\t\t" + subjects[2]),font=('times new roman',12,'bold'),fg="#00008B",bg='white')
      label5.place(x = 60, y = 200)
      label6=Label(dashboardcor,text=(units[2]),font=('times new roman',12,'bold'),fg="#00008B",bg='white')
      label6.place(x = 840, y = 200)
      
      label7=Label(dashboardcor,text=(code[3] + "\t\t" + subjects[3]),font=('times new roman',12,'bold'),fg="#00008B",bg='white')
      label7.place(x = 60, y = 220)
      label8=Label(dashboardcor,text=(units[3]),font=('times new roman',12,'bold'),fg="#00008B",bg='white')
      label8.place(x = 840, y = 220)
      
      label9=Label(dashboardcor,text=(code[4] + "\t\t" + subjects[4]),font=('times new roman',12,'bold'),fg="#00008B",bg='white')
      label9.place(x = 60, y = 240)
      label10=Label(dashboardcor,text=(units[4]),font=('times new roman',12,'bold'),fg="#00008B",bg='white')
      label10.place(x = 840, y = 240)
      
      label11=Label(dashboardcor,text=(code[5] + "\t\t" + subjects[5]),font=('times new roman',12,'bold'),fg="#00008B",bg='white')
      label11.place(x = 60, y = 260)
      label12=Label(dashboardcor,text=(units[5]),font=('times new roman',12,'bold'),fg="#00008B",bg='white')
      label12.place(x = 840, y = 260)
      
      label13=Label(dashboardcor,text=(code[6] + "\t\t" + subjects[6]),font=('times new roman',12,'bold'),fg="#00008B",bg='white')
      label13.place(x = 60, y = 280)
      label14=Label(dashboardcor,text=(units[6]),font=('times new roman',12,'bold'),fg="#00008B",bg='white')
      label14.place(x = 840, y = 280)
      
      if len(subjects) == 8:
         label15=Label(dashboardcor,text=(code[7] + "\t\t" + subjects[7]),font=('times new roman',12,'bold'),fg="#00008B",bg='white')
         label15.place(x = 60, y = 300)
         label16=Label(dashboardcor,text=(units[7]),font=('times new roman',12,'bold'),fg="#00008B",bg='white')
         label16.place(x = 840, y = 300)
      else:
         pass
      
      if len(subjects) == 9:
         label15=Label(dashboardcor,text=(code[7] + "\t\t" + subjects[7]),font=('times new roman',12,'bold'),fg="#00008B",bg='white')
         label15.place(x = 60, y = 300)
         label16=Label(dashboardcor,text=(units[7]),font=('times new roman',12,'bold'),fg="#00008B",bg='white')
         label16.place(x = 840, y = 300)
      
         label17=Label(dashboardcor,text=(code[8] + "\t\t" + subjects[8]),font=('times new roman',12,'bold'),fg="#00008B",bg='white')
         label17.place(x = 60, y = 320)
         label18=Label(dashboardcor,text=(units[8]),font=('times new roman',12,'bold'),fg="#00008B",bg='white')
         label18.place(x = 840, y = 320)

      else:
         pass
      
      
      label16=Label(dashboardcor,text=("Total Units: \t" + str(totalsum)),font=('times new roman',12,'bold'),fg="#00008B",bg='white')
      label16.place(x = 705, y = 340)
      

   def Club(self):
      Frame_lia=Frame(self.root,bd = 10,relief = RIDGE, bg = "#1E90FF")
      Frame_lia.place(x=0,y=0,height=700,width=1366)
      
      dashboardclub=Frame(Frame_lia, bg = "white", height = 300, width = 650, bd = 5,relief = RIDGE)
      dashboardclub.pack(side = BOTTOM, expand="yes")
      
      label1=Label(dashboardclub,text=("""Thank you for attempting to participate in this club.
                                       \nKindly go to registrar to the register for your desired club."""),font=('times new roman',18,'bold'),fg="#00008B",bg='white')
      label1.place(x = 15, y = 100)
      
      btn2=Button(dashboardclub,text="X",command=self.dashboard,cursor="hand2",font=("times new roman",15),fg="white",bg="#DC143C",bd=0,width=15,height=1)
      btn2.place(x = 467, y = 0)

   def Liabilities(self):
      Frame_lia=Frame(self.root,bd = 10,relief = RIDGE, bg = "#1E90FF")
      Frame_lia.place(x=0,y=0,height=700,width=1366)
      
      dashboardlia=Frame(Frame_lia, bg = "white", height = 300, width = 500, bd = 5,relief = RIDGE)
      dashboardlia.pack(side = BOTTOM, expand="yes")
      
      label1=Label(dashboardlia,text=("You don't have any liabilities. \nThank you."),font=('times new roman',23,'bold'),fg="#00008B",bg='white')
      label1.place(x = 48, y = 100)
      
      btn2=Button(dashboardlia,text="X",command=self.dashboard,cursor="hand2",font=("times new roman",15),fg="white",bg="#DC143C",bd=0,width=15,height=1)
      btn2.place(x = 317, y = 0)


   def regclear(self):
      self.entry2.delete(0,END)
      self.entry3.delete(0,END)
      self.entry4.delete(0,END)
      self.entry5.delete(0,END)
      self.entry6.delete(0,END)
      self.entry7.delete(0,END)
      self.entry8.delete(0,END)
      self.entry9.delete(0,END)
      self.entry10.delete(0,END)
      self.entry11.delete(0,END)


   def loginclear(self):
      self.username.delete(0,END)
      self.password.delete(0,END)
      self.confirmpassword.delete(0,END)


root=Tk()
ob=Login(root)
root.mainloop()