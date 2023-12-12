from tkinter import *
from tkinter import ttk,messagebox
from connection import *
#from PIL import Image, ImageTk #pip install pillow
class employeeClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Developed by Zehra")
        self.root.config(bg="white")
        self.root.focus_force()
        #====================== All Variables ================================
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_emp_id=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_utype=StringVar()
        self.var_salary=StringVar()






        #=======search frame========
        SearchFrame=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)
        #====== options======
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Email","Name","ID"),state='readonly',justify=CENTER,font=("times new roman",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="#f2d2bd").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)

        #=====title=====
        title=Label(self.root,text="Employee Details",bg="#0f4d7d",font=("times new roman",15),fg="white").place(x=50,y=100,width=1000)

        #====content=====
        #======== row 1 ========
        lbl_empid=Label(self.root,text="Emp Id",bg="white",font=("times new roman",15)).place(x=50,y=150)
        lbl_gender=Label(self.root,text="Gender",bg="white",font=("times new roman",15)).place(x=350,y=150)
        lbl_contact=Label(self.root,text="Contact",bg="white",font=("times new roman",15)).place(x=750,y=150)

        txt_empid=Entry(self.root,textvariable=self.var_emp_id,bg="#f2d2bd",font=("times new roman",15)).place(x=150,y=150,width=180)
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Other"),font=("times new roman",15),state='readonly',justify=CENTER)
        cmb_gender.place(x=500,y=150,width=180)
        cmb_gender.current(0)
        txt_contact=Entry(self.root,textvariable=self.var_contact,bg="#f2d2bd",font=("times new roman",15)).place(x=850,y=150,width=180)

        #========= row 2 ============
        lbl_name=Label(self.root,text="Name",bg="white",font=("times new roman",15)).place(x=50,y=190)
        lbl_dob=Label(self.root,text="D.O.B",bg="white",font=("times new roman",15)).place(x=350,y=190)
        lbl_doj=Label(self.root,text="D.O.J",bg="white",font=("times new roman",15)).place(x=750,y=190)

        txt_name=Entry(self.root,textvariable=self.var_name,bg="#f2d2bd",font=("times new roman",15)).place(x=150,y=190,width=180)
        txt_dob=Entry(self.root,textvariable=self.var_dob,bg="#f2d2bd",font=("times new roman",15)).place(x=500,y=190,width=180)
        txt_doj=Entry(self.root,textvariable=self.var_doj,bg="#f2d2bd",font=("times new roman",15)).place(x=850,y=190,width=180)

        #========= row 3 ============
        lbl_email=Label(self.root,text="Email",bg="white",font=("times new roman",15)).place(x=50,y=230)
        lbl_pass=Label(self.root,text="Password",bg="white",font=("times new roman",15)).place(x=350,y=230)
        lbl_utype=Label(self.root,text="User Type",bg="white",font=("times new roman",15)).place(x=750,y=230)

        txt_email=Entry(self.root,textvariable=self.var_email,bg="#f2d2bd",font=("times new roman",15)).place(x=150,y=230,width=180)
        txt_pass=Entry(self.root,textvariable=self.var_pass,bg="#f2d2bd",font=("times new roman",15)).place(x=500,y=230,width=180)
        cmb_utype=ttk.Combobox(self.root,textvariable=self.var_utype,values=("Admin","Employee"),font=("times new roman",15),state='readonly',justify=CENTER)
        cmb_utype.place(x=850,y=230,width=180)
        cmb_utype.current(0)

        #========= row 3 ============
        lbl_address=Label(self.root,text="Address",bg="white",font=("times new roman",15)).place(x=50,y=270)
        lbl_salary=Label(self.root,text="Salary",bg="white",font=("times new roman",15)).place(x=500,y=270)

        self.txt_address=Text(self.root,bg="#f2d2bd",font=("times new roman",15))
        self.txt_address.place(x=150,y=270,width=300,height=60)
        txt_salary=Entry(self.root,textvariable=self.var_salary,bg="#f2d2bd",font=("times new roman",15)).place(x=600,y=270,width=180)

        #======buttons==========
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=500,y=305,width=110,height=28)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=620,y=305,width=110,height=28)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=740,y=305,width=110,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=860,y=305,width=110,height=28)

        #=============employee details (tree view)=============
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=150)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.EmployeeTable=ttk.Treeview(emp_frame,columns=("eid","name","email","gender","contact","dob","doj","pass","utype","address","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        self.EmployeeTable.heading("eid",text="Emp Id")
        self.EmployeeTable.heading("name",text="Name")
        self.EmployeeTable.heading("email",text="Email")
        self.EmployeeTable.heading("gender",text="Gender")
        self.EmployeeTable.heading("contact",text="Contact")
        self.EmployeeTable.heading("dob",text="D.O.B")
        self.EmployeeTable.heading("doj",text="D.O.J")
        self.EmployeeTable.heading("pass",text="Password")
        self.EmployeeTable.heading("utype",text="User Type")
        self.EmployeeTable.heading("address",text="Address")
        self.EmployeeTable.heading("salary",text="Salary")

        self.EmployeeTable["show"]="headings"

        self.EmployeeTable.column("eid",width=90)
        self.EmployeeTable.column("name",width=100)
        self.EmployeeTable.column("email",width=100)
        self.EmployeeTable.column("gender",width=100)
        self.EmployeeTable.column("contact",width=100)
        self.EmployeeTable.column("dob",width=100)
        self.EmployeeTable.column("doj",width=100)
        self.EmployeeTable.column("pass",width=100)
        self.EmployeeTable.column("utype",width=100)
        self.EmployeeTable.column("address",width=100)
        self.EmployeeTable.column("salary",width=100)
        self.EmployeeTable.pack(fill=BOTH,expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()

#===============================================================================
    def add(self):
        try:
        # ... (existing code)

            db_cursor.execute(
            "INSERT INTO employee (eid, name, email, gender, contact, dob, doj, pass, utype, address, salary) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (
                self.var_emp_id.get(),
                self.var_name.get(),
                self.var_email.get(),
                self.var_gender.get(),
                self.var_contact.get(),
                self.var_dob.get(),
                self.var_doj.get(),
                self.var_pass.get(),
                self.var_utype.get(),
                self.txt_address.get("1.0", END),
                self.var_salary.get(),
            ),
            )

            

            db_connection.commit()
            messagebox.showinfo('Success', 'Record Inserted Successfully!', parent=self.root)
            self.show()
           
    
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)


    def show(self):
        
        try:
            db_cursor.execute("select * from employee")
            rows=db_cursor.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('',END,values=row)
        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(f))
        row=content['values']
        self.var_emp_id.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_contact.set(row[4]),
        self.var_dob.set(row[5]),
        self.var_doj.set(row[6]),
        self.var_pass.set(row[7]),
        self.var_utype.set(row[8]),
        self.txt_address.delete('1.0',END),
        self.txt_address.insert(END,row[9]),
        self.var_salary.set(row[10])

    def update(self):
        
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror('Error','Please enter Employee ID',parent=self.root)
            else:
                db_cursor.execute("Select * from employee where eid=%s",(self.var_emp_id.get(),))
                row=db_cursor.fetchone()
                if row==None:
                    messagebox.showerror('Error','Invalid Employee Id',parent=self.root)
                else:
                    db_cursor.execute("Update employee set name=%s,email=%s,gender=%s,contact=%s,dob=%s,doj=%s,pass=%s,utype=%s,address=%s,salary=%s where eid=%s",(
                        
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_contact.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_pass.get(),
                        self.var_utype.get(),
                        self.txt_address.get('1.0',END),
                        self.var_salary.get(),
                        self.var_emp_id.get(),
                
                    ))
                    db_connection.commit()
                    messagebox.showinfo('Success','Record Updated Successfully!',parent=self.root)
                    self.show()
                    # db_cursor.close()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def delete(self):
        
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror('Error','Please enter Employee ID',parent=self.root)
            else:
                db_cursor.execute("Select * from employee where eid=%s",(self.var_emp_id.get(),))
                row=db_cursor.fetchone()
                if row==None:
                    messagebox.showerror('Error','Invalid Employee Id',parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete ?",parent=self.root)
                    if op==True:
                        db_cursor.execute("delete from employee where eid=%s",(self.var_emp_id.get(),))
                        db_connection.commit()
                        messagebox.showinfo('Success','Record Deleted Successfully!',parent=self.root)
                        self.clear()
                        self.show()
                        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def clear(self):
        self.var_emp_id.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set("Select"),
        self.var_contact.set(""),
        self.var_dob.set(""),
        self.var_doj.set(""),
        self.var_pass.set(""),
        self.var_utype.set("Admin"),
        self.txt_address.delete('1.0',END),
        self.var_salary.set("")
        self.show()

    def search(self):
        
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select search by option", parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search text is required", parent=self.root)
            else:
                db_cursor.execute("select eid,name,email,gender,dob,doj,pass,utype,address,salary from employee where"+ self.var_searchby.get() +" LIKE '%"+ self.var_searchtxt.get() + "%'")
                rows=db_cursor.fetchall()
                if len(rows)!=0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record Found", parent=self.root)
        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)





if __name__=="__main__":
    root = Tk()
    obj=employeeClass(root)
    root.mainloop()