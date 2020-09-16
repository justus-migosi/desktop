import tkinter
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext as Tk

# Create a window .
window = tk.Tk()
window.title("Primary School Management System :")
# create menubar
Menubar = tk.Menu()
window.config(menu=Menubar)
# Create a filemenu.
Filemenu = tk.Menu(Menubar, tearoff=0)
Filemenu.add_command(label="New Record")
Filemenu.add_separator()
Filemenu.add_command(label="Save As")
Filemenu.add_separator()
Filemenu.add_command(label="Save ")
Filemenu.add_separator()
Filemenu.add_command(label="Print ")
Filemenu.add_separator()
Menubar.add_cascade(label="File", menu=Filemenu)

# Create a EditMenu.
Editmenu = tk.Menu(Menubar, tearoff=0)
Editmenu.add_command(label="Delete")
Editmenu.add_separator()
Editmenu.add_command(label="Update")
Menubar.add_cascade(label="Edit", menu=Editmenu)

# Create a viewmenu.
Viewmenu = tk.Menu(Menubar, tearoff=0)
Viewmenu.add_command(label="Show Database")
Viewmenu.add_separator()
Viewmenu.add_command(label="Show tables")
Menubar.add_cascade(label="View", menu=Viewmenu)

# Create TabControl.
TabControl = ttk.Notebook(window)
Students = tk.Frame(TabControl)
Teachers = tk.Frame(TabControl)
Parents = tk.Frame(TabControl)
TabControl.add(Students, text="Students")
TabControl.add(Teachers, text="Teachers")
TabControl.add(Parents, text="Parents")
TabControl.pack(expand=1, fill="both")

# Create a new tab for students.
TabControl = ttk.Notebook(Students)
Students_Personal_Details_Create = tk.Frame(TabControl, bg="pink")
Students_Personal_Details_Update = tk.Frame(TabControl, bg="pink")
Students_Personal_Details_Delete = tk.Frame(TabControl, bg="pink")
Students_Fee_Payment = tk.Frame(TabControl)
List_of_Students = tk.Frame(TabControl)
Students_Exams = tk.Frame(TabControl)
Update_Student_Records = tk.Frame(TabControl)
TabControl.add(Students_Personal_Details_Create, text="Create New Students Records ")
TabControl.add(Students_Personal_Details_Update,text="Update  Students Records ")
TabControl.add(Students_Personal_Details_Delete,text="Delete  Students Records ")
TabControl.add(Students_Fee_Payment, text="Students Fee Payment ")
TabControl.add(List_of_Students, text="List of Students ")
TabControl.add(Students_Exams, text="Students  Exams  ")
TabControl.pack(expand=1, fill="both")

# Create new Record for students.
Students_Personal_Details_Create_Labelframe = tk.LabelFrame(
    Students_Personal_Details_Create, bg="red", fg="yellow", text="Create New Student Records")
Students_Personal_Details_Create_Labelframe.pack(expand=1)
Student_first_name = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="First Name:", bg="blue", fg="yellow")
Student_first_name.grid(column=0, row=0, sticky="WE")
Student_First_name = tk.Entry(
    Students_Personal_Details_Create_Labelframe, width=100)
Student_First_name.grid(column=1, row=0)

Student_second_name = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="Second Name:", bg="blue", fg="yellow")
Student_second_name.grid(column=2, row=0, sticky="WE")
Student_Second_name = tk.Entry(
    Students_Personal_Details_Create_Labelframe, width=100)
Student_Second_name.grid(column=3, row=0)

# Filling up space.
Student_ = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="       ", bg="red")
Student_.grid(column=0, row=1)

Student_third_name = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="Third Name:", bg="blue", fg="yellow")
Student_third_name.grid(column=0, row=4, sticky="WE")
Student_Third_name = tk.Entry(Students_Personal_Details_Create_Labelframe)
Student_Third_name.grid(column=1, row=4, sticky="WE")

Student_admission_number = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="Admission No:", bg="blue", fg="yellow")
Student_admission_number.grid(column=2, row=4, sticky="WE")
Student_Admission_number = tk.Entry(
    Students_Personal_Details_Create_Labelframe)
Student_Admission_number.grid(column=3, row=4, sticky="WE")

# Filling up space.
Student_ = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="       ", bg="red")
Student_.grid(column=0, row=5)

Student_gender = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="Gender:", bg="blue", fg="yellow")
Student_gender.grid(column=0, row=6, sticky="WE")
Student_Gender = tk.Entry(Students_Personal_Details_Create_Labelframe)
Student_Gender.grid(column=1, row=6, sticky="WE")

Students_parent_phone_number = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="Parents Phone number:", bg="blue", fg="yellow")
Students_parent_phone_number.grid(column=2, row=6)
Students_Parent_phone_number = tk.Entry(
    Students_Personal_Details_Create_Labelframe)
Students_Parent_phone_number.grid(column=3, row=6, sticky="WE")

# Filling up space.
Student_ = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="       ", bg="red")
Student_.grid(column=0, row=7)

Student_location= tk.Label(
    Students_Personal_Details_Create_Labelframe, text="Location:", bg="blue", fg="yellow")
Student_location.grid(column=0, row=8, sticky="WE")
Student_Location = tk.Entry(Students_Personal_Details_Create_Labelframe)
Student_Location.grid(column=1, row=8, sticky="WE")

#Filling up space
Student_=tk.Label(
    Students_Personal_Details_Create_Labelframe,text="        ",bg="red")
Student_.grid(column=0,row=9)

Student_Create = tk.Button(Students_Personal_Details_Create_Labelframe,
                           text="Create Record", bg="yellow", fg="blue", height=6)
Student_Create.grid(column=0, row=9, sticky="WE")

# Update student Records

Students_Personal_Details_Create_Labelframe = tk.LabelFrame(
    Students_Personal_Details_Update, bg="red", fg="yellow", text="Update student Records")
Students_Personal_Details_Create_Labelframe.pack(expand=1)
Student_first_name = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="First Name:", bg="blue", fg="yellow")
Student_first_name.grid(column=0, row=0, sticky="WE")
Student_First_name = tk.Entry(
    Students_Personal_Details_Create_Labelframe, width=100)
Student_First_name.grid(column=1, row=0)

Student_second_name = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="Second Name:", bg="blue", fg="yellow")
Student_second_name.grid(column=2, row=0, sticky="WE")
Student_Second_name = tk.Entry(
    Students_Personal_Details_Create_Labelframe, width=100)
Student_Second_name.grid(column=3, row=0)

# Filling up space.
Student_ = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="       ", bg="red")
Student_.grid(column=0, row=1)

Student_third_name = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="Third Name:", bg="blue", fg="yellow")
Student_third_name.grid(column=0, row=4, sticky="WE")
Student_Third_name = tk.Entry(Students_Personal_Details_Create_Labelframe)
Student_Third_name.grid(column=1, row=4, sticky="WE")

Student_admission_number = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="Admission No:", bg="blue", fg="yellow")
Student_admission_number.grid(column=2, row=4, sticky="WE")
Student_Admission_number = tk.Entry(
    Students_Personal_Details_Create_Labelframe)
Student_Admission_number.grid(column=3, row=4, sticky="WE")

# Filling up space.
Student_ = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="       ", bg="red")
Student_.grid(column=0, row=5)

Student_gender = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="Gender:", bg="blue", fg="yellow")
Student_gender.grid(column=0, row=6, sticky="WE")
Student_Gender = tk.Entry(Students_Personal_Details_Create_Labelframe)
Student_Gender.grid(column=1, row=6, sticky="WE")

Students_parent_phone_number = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="Parents Phone number:", bg="blue", fg="yellow")
Students_parent_phone_number.grid(column=2, row=6)
Students_Parent_phone_number = tk.Entry(
    Students_Personal_Details_Create_Labelframe)
Students_Parent_phone_number.grid(column=3, row=6, sticky="WE")

# Filling up space.
Student_ = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="       ", bg="red")
Student_.grid(column=0, row=7)

Student_location= tk.Label(
    Students_Personal_Details_Create_Labelframe, text="Location:", bg="blue", fg="yellow")
Student_location.grid(column=0, row=8, sticky="WE")
Student_Location = tk.Entry(Students_Personal_Details_Create_Labelframe)
Student_Location.grid(column=1, row=8, sticky="WE")

#Filling up space
Student_=tk.Label(
    Students_Personal_Details_Create_Labelframe,text="        ",bg="red")
Student_.grid(column=0,row=9)



Student_Create = tk.Button(Students_Personal_Details_Create_Labelframe,
                           text="Update Record", bg="yellow", fg="blue", height=6)
Student_Create.grid(column=0, row=9, sticky="WE")

# Delete Student Record.
Students_Personal_Details_Create_Labelframe = tk.LabelFrame(
    Students_Personal_Details_Delete, bg="red", fg="yellow", text="Delete student Records")
Students_Personal_Details_Create_Labelframe.pack(expand=1)
Student_first_name = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="First Name:", bg="blue", fg="yellow")
Student_first_name.grid(column=0, row=0, sticky="WE")
Student_First_name = tk.Entry(
    Students_Personal_Details_Create_Labelframe, width=100)
Student_First_name.grid(column=1, row=0)

Student_second_name = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="Second Name:", bg="blue", fg="yellow")
Student_second_name.grid(column=2, row=0, sticky="WE")
Student_Second_name = tk.Entry(
    Students_Personal_Details_Create_Labelframe, width=100)
Student_Second_name.grid(column=3, row=0)

# Filling up space.
Student_ = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="bg=blue", fg="yellow")
Student_.grid(column=0, row=1)

Student_third_name = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="Third Name:", bg="blue", fg="yellow")
Student_third_name.grid(column=0, row=4, sticky="WE")
Student_Third_name = tk.Entry(Students_Personal_Details_Create_Labelframe)
Student_Third_name.grid(column=1, row=4, sticky="WE")

Student_admission_number = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="Admission No:", bg="blue", fg="yellow")
Student_admission_number.grid(column=2, row=4, sticky="WE")
Student_Admission_number = tk.Entry(
    Students_Personal_Details_Create_Labelframe)
Student_Admission_number.grid(column=3, row=4, sticky="WE")

# Filling up space.
Student_ = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="       ", bg="red")
Student_.grid(column=0, row=5)

Student_gender = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="Gender:", bg="blue", fg="yellow")
Student_gender.grid(column=0, row=6, sticky="WE")
Student_Gender = tk.Entry(Students_Personal_Details_Create_Labelframe)
Student_Gender.grid(column=1, row=6, sticky="WE")

Students_parent_phone_number = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="Parents Phone number:", bg="blue", fg="yellow")
Students_parent_phone_number.grid(column=2, row=6)
Students_Parent_phone_number = tk.Entry(
    Students_Personal_Details_Create_Labelframe)
Students_Parent_phone_number.grid(column=3, row=6, sticky="WE")

# Filling up space.
Student_ = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="       ", bg="red")
Student_.grid(column=0, row=7)

Student_location= tk.Label(
    Students_Personal_Details_Create_Labelframe, text="Location:", bg="blue", fg="yellow")
Student_location.grid(column=0, row=8, sticky="WE")
Student_Location = tk.Entry(Students_Personal_Details_Create_Labelframe)
Student_Location.grid(column=1, row=8, sticky="WE")

#Filling up space
Student_=tk.Label(
    Students_Personal_Details_Create_Labelframe,text="        ",bg="red")
Student_.grid(column=0,row=9)

Student_Create = tk.Button(Students_Personal_Details_Create_Labelframe,
                           text="Delete Record", bg="yellow", fg="blue", height=6)
Student_Create.grid(column=0, row=9, sticky="WE") 


 #Students Fee Payment

Students_Personal_Details_Create_Labelframe = tk.LabelFrame(
    Students_Fee_Payment, bg="red", fg="yellow", text="Student Fee Payment")
Students_Personal_Details_Create_Labelframe.pack(expand=1)
Student_first_name = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="First Name:", bg="blue", fg="yellow")
Student_first_name.grid(column=0, row=0, sticky="WE")
Student_First_name = tk.Entry(
    Students_Personal_Details_Create_Labelframe, width=100)
Student_First_name.grid(column=1, row=0)

Student_second_name = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="Second Name:", bg="blue", fg="yellow")
Student_second_name.grid(column=2, row=0, sticky="WE")
Student_Second_name = tk.Entry(
    Students_Personal_Details_Create_Labelframe, width=100)
Student_Second_name.grid(column=3, row=0)

# Filling up space.
Student_ = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="       ", bg="red")
Student_.grid(column=0, row=1)

Student_third_name = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="Third Name:", bg="blue", fg="yellow")
Student_third_name.grid(column=0, row=4, sticky="WE")
Student_Third_name = tk.Entry(Students_Personal_Details_Create_Labelframe)
Student_Third_name.grid(column=1, row=4, sticky="WE")

Student_admission_number = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="Admission No:", bg="blue", fg="yellow")
Student_admission_number.grid(column=2, row=4, sticky="WE")
Student_Admission_number = tk.Entry(
    Students_Personal_Details_Create_Labelframe)
Student_Admission_number.grid(column=3, row=4, sticky="WE")

# Filling up space.
Student_ = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="       ", bg="red")
Student_.grid(column=0, row=5)

Student_gender = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="Gender:", bg="blue", fg="yellow")
Student_gender.grid(column=0, row=6, sticky="WE")
Student_Gender = tk.Entry(Students_Personal_Details_Create_Labelframe)
Student_Gender.grid(column=1, row=6, sticky="WE")

Students_parent_phone_number = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="Parents Phone number:", bg="blue", fg="yellow")
Students_parent_phone_number.grid(column=2, row=6)
Students_Parent_phone_number = tk.Entry(
    Students_Personal_Details_Create_Labelframe)
Students_Parent_phone_number.grid(column=3, row=6, sticky="WE")

# Filling up space.
Student_ = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="       ", bg="red")
Student_.grid(column=0, row=7)

Student_amout_payable = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="Amount payable:", bg="blue", fg="yellow")
Student_amout_payable.grid(column=0, row=8, sticky="WE")
Student_Amout_payable = tk.Entry(Students_Personal_Details_Create_Labelframe)
Student_Amout_payable.grid(column=1, row=8, sticky="WE")

Students_means_of_payment = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="Means of payment:", bg="blue", fg="yellow")
Students_means_of_payment.grid(column=2, row=8)
Students_Means_of_payment = tk.Entry(
    Students_Personal_Details_Create_Labelframe)
Students_Means_of_payment.grid(column=3, row=8, sticky="WE")

#filling up space
Student_ = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="       ", bg="red")
Student_.grid(column=0, row=9)

Student_Create = tk.Button(Students_Personal_Details_Create_Labelframe,
                           text="Students Fee Payment", bg="yellow", fg="blue", height=6)
Student_Create.grid(column=0, row=9, sticky="WE")
 #Students Exams

Students_Personal_Details_Create_Labelframe = tk.LabelFrame(
    Students_Exams, bg="red", fg="yellow", text="Students Exams")
Students_Personal_Details_Create_Labelframe.pack(expand=1)
Student_first_name = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="First Name:", bg="blue", fg="yellow")
Student_first_name.grid(column=0, row=0, sticky="WE")
Student_First_name = tk.Entry(
    Students_Personal_Details_Create_Labelframe, width=100)
Student_First_name.grid(column=1, row=0)

Student_second_name = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="Second Name:", bg="blue", fg="yellow")
Student_second_name.grid(column=2, row=0, sticky="WE")
Student_Second_name = tk.Entry(
    Students_Personal_Details_Create_Labelframe, width=100)
Student_Second_name.grid(column=3, row=0)

# Filling up space.
Student_ = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="       ", bg="red")
Student_.grid(column=0, row=1)

Student_third_name = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="Third Name:", bg="blue", fg="yellow")
Student_third_name.grid(column=0, row=4, sticky="WE")
Student_Third_name = tk.Entry(Students_Personal_Details_Create_Labelframe)
Student_Third_name.grid(column=1, row=4, sticky="WE")

Student_admission_number = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="Admission No:", bg="blue", fg="yellow")
Student_admission_number.grid(column=2, row=4, sticky="WE")
Student_Admission_number = tk.Entry(
    Students_Personal_Details_Create_Labelframe)
Student_Admission_number.grid(column=3, row=4, sticky="WE")

# Filling up space.
Student_ = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="       ", bg="red")
Student_.grid(column=0, row=5)

Student_gender = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="Gender:", bg="blue", fg="yellow")
Student_gender.grid(column=0, row=6, sticky="WE")
Student_Gender = tk.Entry(Students_Personal_Details_Create_Labelframe)
Student_Gender.grid(column=1, row=6, sticky="WE")

Students_parent_phone_number = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="Parents Phone number:", bg="blue", fg="yellow")
Students_parent_phone_number.grid(column=2, row=6)
Students_Parent_phone_number = tk.Entry(
    Students_Personal_Details_Create_Labelframe)
Students_Parent_phone_number.grid(column=3, row=6, sticky="WE")

#fillig up space
Student_ = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="       ", bg="red")
Student_.grid(column=0, row=7)

Student_subject = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="Subject:", bg="blue", fg="yellow")
Student_subject.grid(column=0, row=8, sticky="WE")
Student_Subject = tk.Entry(Students_Personal_Details_Create_Labelframe)
Student_Subject.grid(column=1, row=8, sticky="WE")

Students_marks_scored = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="Marks scored:", bg="blue", fg="yellow")
Students_marks_scored.grid(column=2, row=8)
Students_Marks_scored = tk.Entry(
    Students_Personal_Details_Create_Labelframe)
Students_Marks_scored.grid(column=3, row=8, sticky="WE")
# Filling up space.
Student_ = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="       ", bg="red")
Student_.grid(column=0, row=9)

Student_Create = tk.Button(Students_Personal_Details_Create_Labelframe,
                           text="Students Exams", bg="yellow", fg="blue", height=6)
Student_Create.grid(column=0, row=9, sticky="WE")

#List of Teachers.
Students_Personal_Details_Create_Labelframe = tk.LabelFrame(
    List_of_Students, bg="red", fg="yellow", text="List of  Students Records")
Students_Personal_Details_Create_Labelframe.pack(expand=1, fill="both")
Students_phone_number = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="Search using ADM Number", bg="blue", fg="yellow")
Students_phone_number.grid(column=0, row=0)
Students_Parent_phone_number = tk.Entry(
    Students_Personal_Details_Create_Labelframe)
Students_Parent_phone_number.grid(column=1, row=0, sticky="WE")
Students_Create = tk.Button(Students_Personal_Details_Create_Labelframe,
                            text="Search using ADM Number", bg="yellow", fg="blue", height=4)
Students_Create.grid(column=0, row=1, sticky="WE")

# Filling up space.
Students_ = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="       ", bg="red")
Students_.grid(column=0, row=2)

Students_list = tk.scrolledtext.ScrolledText(Students_Personal_Details_Create_Labelframe, width=150)
Students_list.grid(column=0, row=3)

# Filling up space.
students_ = tk.Label(
    Students_Personal_Details_Create_Labelframe, text="       ", bg="red")
Students_.grid(column=0, row=7)

Students_Create = tk.Button(Students_Personal_Details_Create_Labelframe,
                            text="List Students Records", bg="yellow", fg="blue", height=3)
Students_Create.grid(column=0, row=8, sticky="WE")

# Create a new tab for Teachers
TabControl = ttk.Notebook(Teachers)
Create_New_Teachers_Records = tk.Frame(TabControl, bg="pink")
Update_Teachers_Records = tk.Frame(TabControl, bg="pink")
Delete_Teachers_Records = tk.Frame(TabControl, bg="pink")
List_of_Teachers = tk.Frame(TabControl, bg="pink")
TabControl.add(Create_New_Teachers_Records,text="Create New Teachers Records ")
TabControl.add(Update_Teachers_Records, text="Update Teachers Records ")
TabControl.add(Delete_Teachers_Records, text="Delete Teachers Records ")
TabControl.add(List_of_Teachers, text="List of Teachers")
TabControl.pack(expand=1, fill="both")


# Create a new tab for Parents.
TabControl = ttk.Notebook(Parents)
Parents_Personal_Details_Create = tk.Frame(TabControl, bg="pink")
Parents_Personal_Details_Update = tk.Frame(TabControl, bg="pink")
Parents_Personal_Details_Delete = tk.Frame(TabControl, bg="pink")
Parents_Fee_Payment = tk.Frame(TabControl)
List_of_Parents = tk.Frame(TabControl)
Update_Parent_Records = tk.Frame(TabControl)
TabControl.add(Parents_Personal_Details_Create, text="Create New Parents Records ")
TabControl.add(Parents_Personal_Details_Update,text="Update  Parents Records ")
TabControl.add(Parents_Personal_Details_Delete,text="Delete  Parents Records ")
TabControl.add(List_of_Parents, text="List of Parents ")
TabControl.pack(expand=1, fill="both")

#create new parents records
Parents_Personal_Details_Create_Labelframe = tk.LabelFrame(
    Parents_Personal_Details_Create, bg="red", fg="yellow", text="Create New Parent Records")
Parents_Personal_Details_Create_Labelframe.pack(expand=1)
Parent_first_name = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="First Name:", bg="blue", fg="yellow")
Parent_first_name.grid(column=0, row=0, sticky="WE")
Parent_First_name = tk.Entry(
    Parents_Personal_Details_Create_Labelframe, width=100)
Parent_First_name.grid(column=1, row=0)

Parent_second_name = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="Second Name:", bg="blue", fg="yellow")
Parent_second_name.grid(column=2, row=0, sticky="WE")
Parent_Second_name = tk.Entry(
    Parents_Personal_Details_Create_Labelframe, width=100)
Parent_Second_name.grid(column=3, row=0)

# Filling up space.
Parent_ = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="       ", bg="red")
Parent_.grid(column=0, row=1)

Parent_third_name = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="Third Name:", bg="blue", fg="yellow")
Parent_third_name.grid(column=0, row=4, sticky="WE")
Parent_Third_name = tk.Entry(Parents_Personal_Details_Create_Labelframe)
Parent_Third_name.grid(column=1, row=4, sticky="WE")

Parent_admission_number = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="Admission No:", bg="blue", fg="yellow")
Parent_admission_number.grid(column=2, row=4, sticky="WE")
Parent_Admission_number = tk.Entry(
    Parents_Personal_Details_Create_Labelframe)
Parent_Admission_number.grid(column=3, row=4, sticky="WE")

# Filling up space.
Parent_ = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="       ", bg="red")
Parent_.grid(column=0, row=5)

Parent_gender = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="Gender:", bg="blue", fg="yellow")
Parent_gender.grid(column=0, row=6, sticky="WE")
Parent_Gender = tk.Entry(Parents_Personal_Details_Create_Labelframe)
Parent_Gender.grid(column=1, row=6, sticky="WE")

Parents_parent_phone_number = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="Parents Phone number:", bg="blue", fg="yellow")
Parents_parent_phone_number.grid(column=2, row=6)
Parents_Parent_phone_number = tk.Entry(
    Parents_Personal_Details_Create_Labelframe)
Parents_Parent_phone_number.grid(column=3, row=6, sticky="WE")

# Filling up space.
Parent_ = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="       ", bg="red")
Parent_.grid(column=0, row=7)

Parent_location= tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="Location:", bg="blue", fg="yellow")
Parent_location.grid(column=0, row=8, sticky="WE")
Parent_Location = tk.Entry(Parents_Personal_Details_Create_Labelframe)
Parent_Location.grid(column=1, row=8, sticky="WE")

#Filling up space
Parent_=tk.Label(
    Parents_Personal_Details_Create_Labelframe,text="          ",bg="red")
Parent_.grid(column=0,row=9)

Parent_Create = tk.Button(Parents_Personal_Details_Create_Labelframe,
                           text="Create Record", bg="yellow", fg="blue", height=6)
Parent_Create.grid(column=0, row=9, sticky="WE")


# Update Parents Records.
Parents_Personal_Details_Create_Labelframe = tk.LabelFrame(
    Parents_Personal_Details_Update, bg="red", fg="yellow", text="Update Parents Records")
Parents_Personal_Details_Create_Labelframe.pack(expand=1)
Parents_first_name = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="First Name:", bg="blue", fg="yellow")
Parents_first_name.grid(column=0, row=0, sticky="WE")
Parents_First_name = tk.Entry(
    Parents_Personal_Details_Create_Labelframe, width=100)
Parents_First_name.grid(column=1, row=0)

Parents_second_name = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="Second Name:", bg="blue", fg="yellow")
Parents_second_name.grid(column=2, row=0, sticky="WE")
Parents_Second_name = tk.Entry(
    Parents_Personal_Details_Create_Labelframe, width=100)
Parents_Second_name.grid(column=3, row=0)

# Filling up space.
Parents_ = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="       ", bg="red")
Parents_.grid(column=0, row=1)

Parents_third_name = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="Third Name:", bg="blue", fg="yellow")
Parents_third_name.grid(column=0, row=4, sticky="WE")
Parents_Third_name = tk.Entry(Parents_Personal_Details_Create_Labelframe)
Parents_Third_name.grid(column=1, row=4, sticky="WE")

Parents_admission_number = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="ADM No:", bg="blue", fg="yellow")
Parents_admission_number.grid(column=2, row=4, sticky="WE")
Parents_Admission_number = tk.Entry(
    Parents_Personal_Details_Create_Labelframe)
Parents_Admission_number.grid(column=3, row=4, sticky="WE")

# Filling up space.
Parents_ = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="       ", bg="red")
Parents_.grid(column=0, row=5)

Parents_gender = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="Gender:", bg="blue", fg="yellow")
Parents_gender.grid(column=0, row=6, sticky="WE")
Parents_Gender = tk.Entry(Parents_Personal_Details_Create_Labelframe)
Parents_Gender.grid(column=1, row=6, sticky="WE")

Parents_phone_number = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="Phone number:", bg="blue", fg="yellow")
Parents_phone_number.grid(column=2, row=6)
Parents_Teacher_phone_number = tk.Entry(
    Parents_Personal_Details_Create_Labelframe)
Parents_Teacher_phone_number.grid(column=3, row=6, sticky="WE")

# Filling up space.
Parents_ = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="       ", bg="red")
Parents_.grid(column=0, row=7)

Parent_location= tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="Location:", bg="blue", fg="yellow")
Parent_location.grid(column=0, row=8, sticky="WE")
Parent_Location = tk.Entry(Parents_Personal_Details_Create_Labelframe)
Parent_Location.grid(column=1, row=8, sticky="WE")

#Filling up space
Parents_=tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="       ", bg="red")
Parents_.grid(column=0, row=9)

Parents_Create = tk.Button(Parents_Personal_Details_Create_Labelframe,
                            text="Update Record", bg="yellow", fg="blue", height=6)
Parents_Create.grid(column=0, row=9, sticky="WE")

#List of Parents.
Parents_Personal_Details_Create_Labelframe = tk.LabelFrame(
List_of_Parents, bg="red", fg="yellow", text="List of  Parents Records")
Parents_Personal_Details_Create_Labelframe.pack(expand=1, fill="both")
Parents_phone_number = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="Search using ADM Number", bg="blue", fg="yellow")
Parents_phone_number.grid(column=0, row=0)
Parents_Parent_phone_number = tk.Entry(
    Parents_Personal_Details_Create_Labelframe)
Parents_Parent_phone_number.grid(column=1, row=0, sticky="WE")
Parents_Create = tk.Button(Parents_Personal_Details_Create_Labelframe,
                            text="Search using ADM Number", bg="yellow", fg="blue", height=4)
Parents_Create.grid(column=0, row=1, sticky="WE")

# Filling up space.
Parents_ = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="       ", bg="red")
Parents_.grid(column=0, row=2)

Parents_list = tk.scrolledtext.ScrolledText(Parents_Personal_Details_Create_Labelframe, width=150)
Parents_list.grid(column=0, row=3)

# Filling up space.
Parents_ = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="       ", bg="red")
Parents_.grid(column=0, row=7)

Parents_Create = tk.Button(Parents_Personal_Details_Create_Labelframe,
                            text="List Parents Records", bg="yellow", fg="blue", height=3)
Parents_Create.grid(column=0, row=8, sticky="WE")

#Delete Teachers Records.
Parents_Personal_Details_Create_Labelframe = tk.LabelFrame(
    Parents_Personal_Details_Delete, bg="red", fg="yellow", text="Delete Parents Records")
Parents_Personal_Details_Create_Labelframe.pack(expand=1)
Parents_first_name = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="First Name:", bg="blue", fg="yellow")
Parents_first_name.grid(column=0, row=0, sticky="WE")
Parents_First_name = tk.Entry(
    Parents_Personal_Details_Create_Labelframe, width=100)
Parents_First_name.grid(column=1, row=0)

Parents_second_name = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="Second Name:", bg="blue", fg="yellow")
Parents_second_name.grid(column=2, row=0, sticky="WE")
Parents_Second_name = tk.Entry(
    Parents_Personal_Details_Create_Labelframe, width=100)
Parents_Second_name.grid(column=3, row=0)

# Filling up space.
Parents_ = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="       ", bg="red")
Parents_.grid(column=0, row=1)

Parents_third_name = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="Third Name:", bg="blue", fg="yellow")
Parents_third_name.grid(column=0, row=4, sticky="WE")
Parents_Third_name = tk.Entry(Parents_Personal_Details_Create_Labelframe)
Parents_Third_name.grid(column=1, row=4, sticky="WE")

Parents_admission_number = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="ADM No:", bg="blue", fg="yellow")
Parents_admission_number.grid(column=2, row=4, sticky="WE")
Parents_Admission_number = tk.Entry(
    Parents_Personal_Details_Create_Labelframe)
Parents_Admission_number.grid(column=3, row=4, sticky="WE")

# Filling up space.
Parents_ = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="       ", bg="red")
Parents_.grid(column=0, row=5)

Parents_gender = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="Gender:", bg="blue", fg="yellow")
Parents_gender.grid(column=0, row=6,sticky="WE" )
Parents_Gender = tk.Entry(Parents_Personal_Details_Create_Labelframe)
Parents_Gender.grid(column=1, row=6, sticky="WE")

Parents_phone_number = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="Phone number:", bg="blue", fg="yellow")
Parents_phone_number.grid(column=2, row=6)
Parents_Parent_phone_number = tk.Entry(
    Parents_Personal_Details_Create_Labelframe)
Parents_Parent_phone_number.grid(column=3, row=6, sticky="WE")

#Filling up space
Parents_ = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="       ", bg="red")
Parents_.grid(column=0, row=7)

Parent_location= tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="Location:", bg="blue", fg="yellow")
Parent_location.grid(column=0, row=8, sticky="WE") 
Parent_Location = tk.Entry(Students_Personal_Details_Create_Labelframe)
Parent_Location.grid(column=1, row=8, sticky="WE")

#Filling up space
Parents_ = tk.Label(
    Parents_Personal_Details_Create_Labelframe, text="       ", bg="red")
Parents_.grid(column=0, row=9)

Parents_Create = tk.Button(Parents_Personal_Details_Create_Labelframe,
                            text="Delete Record", bg="yellow", fg="blue", height=6)
Parents_Create.grid(column=0, row=9, sticky="WE")

# Create New Teachers Records.

Teachers_Personal_Details_Create_Labelframe = tk.LabelFrame(
    Create_New_Teachers_Records, bg="red", fg="yellow", text="Create New  Teachers Records")
Teachers_Personal_Details_Create_Labelframe.pack(expand=1)
Teachers_first_name = tk.Label(
    Teachers_Personal_Details_Create_Labelframe, text="First Name:", bg="blue", fg="yellow")
Teachers_first_name.grid(column=0, row=0, sticky="WE")
Teachers_First_name = tk.Entry(
    Teachers_Personal_Details_Create_Labelframe, width=100)
Teachers_First_name.grid(column=1, row=0)

Teachers_second_name = tk.Label(
    Teachers_Personal_Details_Create_Labelframe, text="Second Name:", bg="blue", fg="yellow")
Teachers_second_name.grid(column=2, row=0, sticky="WE")
Teachers_Second_name = tk.Entry(
    Teachers_Personal_Details_Create_Labelframe, width=100)
Teachers_Second_name.grid(column=3, row=0)

# Filling up space.
Teachers_ = tk.Label(
    Teachers_Personal_Details_Create_Labelframe, text="       ", bg="red")
Teachers_.grid(column=0, row=1)

Teachers_third_name = tk.Label(
    Teachers_Personal_Details_Create_Labelframe, text="Third Name:", bg="blue", fg="yellow")
Teachers_third_name.grid(column=0, row=4, sticky="WE")
Teachers_Third_name = tk.Entry(Teachers_Personal_Details_Create_Labelframe)
Teachers_Third_name.grid(column=1, row=4, sticky="WE")

Teachers_admission_number = tk.Label(
    Teachers_Personal_Details_Create_Labelframe, text="TSC No:", bg="blue", fg="yellow")
Teachers_admission_number.grid(column=2, row=4, sticky="WE")
Teachers_Admission_number = tk.Entry(
    Teachers_Personal_Details_Create_Labelframe)
Teachers_Admission_number.grid(column=3, row=4, sticky="WE")

# Filling up space.
Teachers_ = tk.Label(
    Teachers_Personal_Details_Create_Labelframe, text="       ", bg="red")
Teachers_.grid(column=0, row=5)

Teachers_gender = tk.Label(
    Teachers_Personal_Details_Create_Labelframe, text="Gender:", bg="blue", fg="yellow")
Teachers_gender.grid(column=0, row=6, sticky="WE")
Teachers_Gender = tk.Entry(Teachers_Personal_Details_Create_Labelframe)
Teachers_Gender.grid(column=1, row=6, sticky="WE")

Teachers_phone_number = tk.Label(
    Teachers_Personal_Details_Create_Labelframe, text="Phone number:", bg="blue", fg="yellow")
Teachers_phone_number.grid(column=2, row=6)
Teachers_Parent_phone_number = tk.Entry(
    Teachers_Personal_Details_Create_Labelframe)
Teachers_Parent_phone_number.grid(column=3, row=6, sticky="WE")

# Filling up space.
Teachers_ = tk.Label(
    Teachers_Personal_Details_Create_Labelframe, text="       ", bg="red")
Teachers_.grid(column=0, row=7)

Teacher_location= tk.Label(
    Teachers_Personal_Details_Create_Labelframe, text="Location:", bg="blue", fg="yellow")
Teacher_location.grid(column=0, row=8, sticky="WE")
Teacher_Location = tk.Entry(Teachers_Personal_Details_Create_Labelframe)
Teacher_Location.grid(column=1, row=8, sticky="WE")

#Filling up space
Teachers_ = tk.Label(
    Teachers_Personal_Details_Create_Labelframe, text="       ", bg="red")
Teachers_.grid(column=0, row=9)



Teachers_Create = tk.Button(Teachers_Personal_Details_Create_Labelframe,
                            text="Create Record", bg="yellow", fg="blue", height=6)
Teachers_Create.grid(column=0, row=9, sticky="WE")


# Update Teachers Records.


Teachers_Personal_Details_Create_Labelframe = tk.LabelFrame(
    Update_Teachers_Records, bg="red", fg="yellow", text="Update Teachers Records")
Teachers_Personal_Details_Create_Labelframe.pack(expand=1)
Teachers_first_name = tk.Label(
    Teachers_Personal_Details_Create_Labelframe, text="First Name:", bg="blue", fg="yellow")
Teachers_first_name.grid(column=0, row=0, sticky="WE")
Teachers_First_name = tk.Entry(
    Teachers_Personal_Details_Create_Labelframe, width=100)
Teachers_First_name.grid(column=1, row=0)

Teachers_second_name = tk.Label(
    Teachers_Personal_Details_Create_Labelframe, text="Second Name:", bg="blue", fg="yellow")
Teachers_second_name.grid(column=2, row=0, sticky="WE")
Teachers_Second_name = tk.Entry(
    Teachers_Personal_Details_Create_Labelframe, width=100)
Teachers_Second_name.grid(column=3, row=0)

# Filling up space.
Teachers_ = tk.Label(
    Teachers_Personal_Details_Create_Labelframe, text="       ", bg="red")
Teachers_.grid(column=0, row=1)

Teachers_third_name = tk.Label(
    Teachers_Personal_Details_Create_Labelframe, text="Third Name:", bg="blue", fg="yellow")
Teachers_third_name.grid(column=0, row=4, sticky="WE")
Teachers_Third_name = tk.Entry(Teachers_Personal_Details_Create_Labelframe)
Teachers_Third_name.grid(column=1, row=4, sticky="WE")

Teachers_admission_number = tk.Label(
    Teachers_Personal_Details_Create_Labelframe, text="TSC No:", bg="blue", fg="yellow")
Teachers_admission_number.grid(column=2, row=4, sticky="WE")
Teachers_Admission_number = tk.Entry(
    Teachers_Personal_Details_Create_Labelframe)
Teachers_Admission_number.grid(column=3, row=4, sticky="WE")

# Filling up space.
Teachers_ = tk.Label(
    Teachers_Personal_Details_Create_Labelframe, text="       ", bg="red")
Teachers_.grid(column=0, row=5)

Teachers_gender = tk.Label(
    Teachers_Personal_Details_Create_Labelframe, text="Gender:", bg="blue", fg="yellow")
Teachers_gender.grid(column=0, row=6, sticky="WE")
Teachers_Gender = tk.Entry(Teachers_Personal_Details_Create_Labelframe)
Teachers_Gender.grid(column=1, row=6, sticky="WE")

Teachers_phone_number = tk.Label(
    Teachers_Personal_Details_Create_Labelframe, text="Phone number:", bg="blue", fg="yellow")
Teachers_phone_number.grid(column=2, row=6)
Teachers_Parent_phone_number = tk.Entry(
    Teachers_Personal_Details_Create_Labelframe)
Teachers_Parent_phone_number.grid(column=3, row=6, sticky="WE")

# Filling up space.
Teachers_ = tk.Label(
    Teachers_Personal_Details_Create_Labelframe, text="       ", bg="red")
Teachers_.grid(column=0, row=7)

Teacher_location= tk.Label(
    Teachers_Personal_Details_Create_Labelframe, text="Location:", bg="blue", fg="yellow")
Teacher_location.grid(column=0, row=8, sticky="WE")
Teacher_Location = tk.Entry(Teachers_Personal_Details_Create_Labelframe)
Teacher_Location.grid(column=1, row=8, sticky="WE")

#Filling up space
Teachers_ = tk.Label(
    Teachers_Personal_Details_Create_Labelframe, text="       ", bg="red")
Teachers_.grid(column=0, row=9)


Teachers_Create = tk.Button(Teachers_Personal_Details_Create_Labelframe,
                            text="Update Record", bg="yellow", fg="blue", height=6)
Teachers_Create.grid(column=0, row=9, sticky="WE")

# Delete Teachers Records.

Teachers_Personal_Details_Create_Labelframe = tk.LabelFrame(
    Delete_Teachers_Records, bg="red", fg="yellow", text="Delete Teachers Records")
Teachers_Personal_Details_Create_Labelframe.pack(expand=1)
Teachers_first_name = tk.Label(
    Teachers_Personal_Details_Create_Labelframe, text="First Name:", bg="blue", fg="yellow")
Teachers_first_name.grid(column=0, row=0, sticky="WE")
Teachers_First_name = tk.Entry(
    Teachers_Personal_Details_Create_Labelframe, width=100)
Teachers_First_name.grid(column=1, row=0)

Teachers_second_name = tk.Label(
    Teachers_Personal_Details_Create_Labelframe, text="Second Name:", bg="blue", fg="yellow")
Teachers_second_name.grid(column=2, row=0, sticky="WE")
Teachers_Second_name = tk.Entry(
    Teachers_Personal_Details_Create_Labelframe, width=100)
Teachers_Second_name.grid(column=3, row=0)

# Filling up space.
Teachers_ = tk.Label(
    Teachers_Personal_Details_Create_Labelframe, text="       ", bg="red")
Teachers_.grid(column=0, row=1)

Teachers_third_name = tk.Label(
    Teachers_Personal_Details_Create_Labelframe, text="Third Name:", bg="blue", fg="yellow")
Teachers_third_name.grid(column=0, row=4, sticky="WE")
Teachers_Third_name = tk.Entry(Teachers_Personal_Details_Create_Labelframe)
Teachers_Third_name.grid(column=1, row=4, sticky="WE")

Teachers_admission_number = tk.Label(
    Teachers_Personal_Details_Create_Labelframe, text="TSC No:", bg="blue", fg="yellow")
Teachers_admission_number.grid(column=2, row=4, sticky="WE")
Teachers_Admission_number = tk.Entry(
    Teachers_Personal_Details_Create_Labelframe)
Teachers_Admission_number.grid(column=3, row=4, sticky="WE")

# Filling up space.
Teachers_ = tk.Label(
    Teachers_Personal_Details_Create_Labelframe, text="       ", bg="red")
Teachers_.grid(column=0, row=5)

Teachers_gender = tk.Label(
    Teachers_Personal_Details_Create_Labelframe, text="Gender:", bg="blue", fg="yellow")
Teachers_gender.grid(column=0, row=6, sticky="WE")
Teachers_Gender = tk.Entry(Teachers_Personal_Details_Create_Labelframe)
Teachers_Gender.grid(column=1, row=6, sticky="WE")

Teachers_phone_number = tk.Label(
    Teachers_Personal_Details_Create_Labelframe, text="Phone number:", bg="blue", fg="yellow")
Teachers_phone_number.grid(column=2, row=6)
Teachers_Parent_phone_number = tk.Entry(
    Teachers_Personal_Details_Create_Labelframe)
Teachers_Parent_phone_number.grid(column=3, row=6, sticky="WE")

# Filling up space.
Teachers_= tk.Label(
    Teachers_Personal_Details_Create_Labelframe, text="       ", bg="red")
Teachers_.grid(column=0, row=7)

Teacher_location= tk.Label(
    Teachers_Personal_Details_Create_Labelframe, text="Location:", bg="blue", fg="yellow")
Teacher_location.grid(column=0, row=8, sticky="WE")
Teacher_Location = tk.Entry(Teachers_Personal_Details_Create_Labelframe)
Teacher_Location.grid(column=1, row=8, sticky="WE")

#Filling up space
Teachers_= tk.Label(
    Teachers_Personal_Details_Create_Labelframe, text="       ", bg="red")
Teachers_.grid(column=0, row=9)

Teachers_Create = tk.Button(Teachers_Personal_Details_Create_Labelframe,
                            text="Delete Record", bg="yellow", fg="blue", height=6)
Teachers_Create.grid(column=0, row=9, sticky="WE")

# List of Teachers.
Teachers_Personal_Details_Create_Labelframe = tk.LabelFrame(
    List_of_Teachers, bg="red", fg="yellow", text="List of  Teachers Records")
Teachers_Personal_Details_Create_Labelframe.pack(expand=1, fill="both")
Teachers_phone_number = tk.Label(
    Teachers_Personal_Details_Create_Labelframe, text="Search using TSC Number", bg="blue", fg="yellow")
Teachers_phone_number.grid(column=0, row=0)
Teachers_Parent_phone_number = tk.Entry(
    Teachers_Personal_Details_Create_Labelframe)
Teachers_Parent_phone_number.grid(column=1, row=0, sticky="WE")
Teachers_Create = tk.Button(Teachers_Personal_Details_Create_Labelframe,
                            text="Search using TSC Number", bg="yellow", fg="blue", height=4)
Teachers_Create.grid(column=0, row=1, sticky="WE")

# Filling up space.
Teachers_ = tk.Label(
    Teachers_Personal_Details_Create_Labelframe, text="       ", bg="red")
Teachers_.grid(column=0, row=2)

Teachers_list = tk.scrolledtext.ScrolledText(Teachers_Personal_Details_Create_Labelframe, width=150)
Teachers_list.grid(column=0, row=3)

# Filling up space.
Teachers_ = tk.Label(
    Teachers_Personal_Details_Create_Labelframe, text="       ", bg="red")
Teachers_.grid(column=0, row=7)

Teachers_Create = tk.Button(Teachers_Personal_Details_Create_Labelframe,
                            text="List Teachers Records", bg="yellow", fg="blue", height=3)
Teachers_Create.grid(column=0, row=7, sticky="WE")


window.mainloop()
