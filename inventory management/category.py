from tkinter import *
from PIL import Image,ImageTk 
from tkinter import ttk,messagebox
from connection import *
from tkinter import scrolledtext
import PIL.Image
#from PIL import Image, ImageTk #pip install pillow
class categoryClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Developed by PVPIT Team")
        self.root.config(bg="white")
        self.root.focus_force()
        
        self.var_cat_id=StringVar()
        self.var_name=StringVar()
        
        lbl_title=Label(self.root,text="Manage Product Category", font=("goudy old style",30),bg="#184a45",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)
        
        lbl_name=Label(self.root,text="Enter Category Name", font=("goudy old style",30),bg="white").place(x=50,y=100)
        
        txt_name=Entry(self.root,textvariable=self.var_name, font=("goudy old style",25),bg="lightyellow").place(x=50,y=170,width=300)
        
        txt_name=Entry(self.root,textvariable=self.var_name, font=("goudy old style",25),bg="lightyellow").place(x=50,y=170,width=300)
        
        btn_add=Button(self.root,text="ADD",command= self.add, font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=360,y=170,width=150,height=30)
        btn_delete=Button(self.root,text="DELETE",command= self.delete, font=("goudy old style",15),bg="red",fg="white",cursor="hand2").place(x=520,y=170,width=150,height=30)
        
        
        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=700,y=100,width=380,height=100)
        
        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)
        
        self.category_table=ttk.Treeview(cat_frame,columns=("cid","name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.category_table.xview)
        scrolly.config(command=self.category_table.yview)
        
        self.category_table.heading("cid",text="C ID:")
        self.category_table.heading("name",text="Name:")
        self.category_table["show"]="headings"
        self.category_table.column("cid",width=90)
        self.category_table.column("name",width=100)
        self.category_table.pack(fill=BOTH,expand=1)
        self.category_table.bind("<ButtonRelease-1>",self.get_data)
        
        
        self.im1=Image.open("E:/inventory management/image/cats.png")
        self.im1=self.im1.resize((500,250),Image.ANTIALIAS)
        self.im1=ImageTk.PhotoImage(self.im1)
        
        self.lbl_im1=Label(self.root,image=self.im1,bd=2,relief=RAISED)
        self.lbl_im1.place(x=50,y=220)
        
        self.im2=Image.open("E:/inventory management/image/cata.jpg")
        self.im2=self.im2.resize((500,250),Image.ANTIALIAS)
        self.im2=ImageTk.PhotoImage(self.im2)
        
        self.lbl_im2=Label(self.root,image=self.im2,bd=2,relief=RAISED)
        self.lbl_im2.place(x=580,y=220)
        self.show()
        
        
        
    def add(self):
        
        try:
            if self.var_name.get()=="":
                messagebox.showerror('Error','Category name required',parent=self.root)
            else:
                db_cursor.execute("Select * from category where name=%s",(self.var_name.get(),))
                row=db_cursor.fetchone()
                if row!=None:
                    messagebox.showerror('Error','Category already exist',parent=self.root)
                else:
                    db_cursor.execute("Insert into category(name) values(%s)",(
                        self.var_name.get(),                
                    ))
                    db_connection.commit()
                    messagebox.showinfo('Success','Category Added Successfully!',parent=self.root)
                    self.show()
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def show(self):
        
        try:
            db_cursor.execute("select * from category")
            rows=db_cursor.fetchall()
            self.category_table.delete(*self.category_table.get_children())
            for row in rows:
                self.category_table.insert('',END,values=row)
        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
            
            
    def get_data(self,ev):
        f=self.category_table.focus()
        content=(self.category_table.item(f))
        row=content['values']
        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])
        
        
        
    def delete(self):
       
        try:
            if self.var_cat_id.get()=="":
                messagebox.showerror('Error','Please enter or select category name from the list',parent=self.root)
            else:
                db_cursor.execute("Select * from category where cid=%s",(self.var_cat_id.get(),))
                row=db_cursor.fetchone()
                if row==None:
                    messagebox.showerror('Error','Error,please try again',parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete ?",parent=self.root)
                    if op==True:
                        db_cursor.execute("delete from category where cid=%s",(self.var_cat_id.get(),))
                        db_connection.commit()
                        messagebox.showinfo('Success','Category Deleted Successfully!',parent=self.root)
                        self.show()
                        self.var_cat_id.set("")
                        self.var_name.set("")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

        
if __name__=="__main__":
    root = Tk()
    obj=categoryClass(root)
    root.mainloop()