import  tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
import random
try:
    class QuizeApp():  
        def __init__(self):
            self.hours=0
            self.minutes=0
            self.title="Quiz"
            self.student="XYZ"
            self.stdyear="xyz"
            self.file="questionlist.txt"
        def test_details(self):
            def entry_delete1(event):
                name_box.delete(0,"end")
            def entry_delete2(event):
               if event.widget.get().strip() == "00":
                    event.widget.delete(0, tk.END)
            def entry_delete3(event):
                if event.widget.get().strip() == "00":
                    event.widget.delete(0, tk.END) 

            self.test_root=tk.Tk()
            self.test_root.resizable(False,False)
            self.test_root.title("Test Details")
            try:
                self.test_root.iconbitmap("todo.ico")
            except  Exception as e:
                print(f"Error {e}")
            screen_width=self.test_root.winfo_screenwidth()
            x=int(screen_width/2)
            screen_height=self.test_root.winfo_screenheight()
            y=int(screen_height/2)
            adjusted_screen_width= (screen_width// 2) - (x// 2)
            adjusted_screen_height = (screen_height// 2) - (y// 2)

            self.test_root.geometry(f"{x}x{y}+{adjusted_screen_width}+{adjusted_screen_height}")
            self.test_root.iconbitmap("todo.ico")
            self.test_root.configure(bg="#EAECE8")
            name_label=tk.Label(self.test_root,text="Title  :",font=("Times New Roman",20))
            name_label.place(x=150,y=70)
            self.name=tk.StringVar()
            name_box=tk.Entry(self.test_root,textvariable=self.name,font=("Arial",13))
            name_box.place(x=275,y=75,height=25,width=300)
            name_box.insert(0,"DSA Quize, Aptitude Quize, Gk Ques")
            name_box.bind('<FocusIn>',entry_delete1)

            class_label=tk.Label(self.test_root,text="Duration:",font=("Times New Roman",20))
            class_label.place(x=150,y=150)
            hhlabel=tk.Label(self.test_root,text="HH",font=("Times New Roman",15))
            hhlabel.place(x=300,y=150)
            colonlabel=tk.Label(self.test_root,text=":",font=("Times New Roman",28))
            colonlabel.place(x=400,y=135)
            mmlabel=tk.Label(self.test_root,text="MM",font=("Times New Roman",15))
            mmlabel.place(x=418,y=150)
            self.hrs=tk.StringVar(value="00")
            hours_box=tk.Entry(self.test_root,textvariable=self.hrs,font=("Arial",15))
            hours_box.place(x=350,y=150,height=25,width=43)
            hours_box.bind('<FocusIn>',entry_delete2)
            # hours_box.insert(0,"00")
            self.min=tk.StringVar(value="00")
            minutes_box=tk.Entry(self.test_root,textvariable=self.min,font=("Arial",15))
            minutes_box.place(x=460,y=150,height=25,width=43)
            minutes_box.bind('<FocusIn>',entry_delete3)
            # minutes_box.insert(0,"00")
            import_box=tk.Label(self.test_root,text="Select Question File:",font=("Times New Roman",20))
            import_box.place(x=150,y=250)
            selectbtn=tk.Button(self.test_root,text="Select",command=lambda:self.loadquestionfile(),bg="light blue",font=("Times New Roman",20))
            selectbtn.place(x=400,y=250,height=40,width=90)
            self.test_root.mainloop()
        def loadquestionfile(self):
            try:
                self.file=fd.askopenfilename(title="Select the text file",filetypes=[("Text files", "*.txt"), ("All files", "*.*")],parent=self.test_root)
            except Exception as e:
                print(f"Error {e}")     
            self.student_details()
        def student_details(self):
            self.test_root.destroy()
            def entry_delete1(event):
                name_box.delete(0,"end")
            def entry_delete2(event):
                class_box.delete(0,"end")
            
            self.root=tk.Tk()
            self.root.resizable(False,False)
            self.root.title("Student")
            screen_width=self.root.winfo_screenwidth()
            x=int(screen_width/2)
            screen_height=self.root.winfo_screenheight()
            y=int(screen_height/2)
            adjusted_screen_width= (screen_width// 2) - (x// 2)
            adjusted_screen_height = (screen_height// 2) - (y// 2)

            self.root.geometry(f"{x}x{y}+{adjusted_screen_width}+{adjusted_screen_height}")
            try:
                self.root.iconbitmap("todo.ico")
            except Exception as e:
                print(f"Error {e}")
            self.root.configure(bg="#EAECE8")
            name_label=tk.Label(self.root,text="Name  :",font=("Times New Roman",20))
            name_label.place(x=150,y=70)
            self.stdname=tk.StringVar()
            name_box=tk.Entry(self.root,textvariable=self.stdname,font=("Arial",15))
            name_box.place(x=275,y=75,height=25,width=300)
            name_box.insert(0,"Vivek, Yash , Nitin etc.")
            name_box.bind('<FocusIn>',entry_delete1)
            class_label=tk.Label(self.root,text="Year  :",font=("Times New Roman",20))
            class_label.place(x=150,y=150)
            self.year=tk.StringVar()
            class_box=tk.Entry(self.root,textvariable=self.year,font=("Arial",15))
            class_box.place(x=275,y=150,height=25,width=300)
            class_box.insert(0,"1,2,3,4")
            class_box.bind('<FocusIn>',entry_delete2)
            startbtn=tk.Button(self.root,text="Start",width=7,command=lambda:self.check_details(),bg="light blue",font=("Times New Roman",20))
            startbtn.place(x=300,y=300)
            self.title = self.name.get().strip()
            self.root.mainloop()
        def check_details(self):
            self.title=self.name.get().strip()
            self.student=self.stdname.get().strip()
            self.stdyear=self.year.get().strip()
            self.hours= int(self.hrs.get().strip())  if self.hrs.get().strip().isdigit() else 0 
            self.minutes=int(self.min.get().strip()) if self.min.get().strip().isdigit() else 0
            l=("1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","^","&","*",'(',")",'/',"?")
            
            try:
                if self.stdname.get().startswith(l) or self.stdname.get().endswith(l):
                    messagebox.showerror(message="Invalid Name")
                elif (len(self.stdname.get())>20 or len(self.stdname.get())<4):
                    messagebox.showerror(message="Invalid Name")
                elif not self.year.get().isdigit():
                    messagebox.showerror(message="Invalid Entry: Please enter a number between 1 and 4")
                elif int(self.year.get()) not in range(1,5):
                    messagebox.showerror(message="Invalid Entry "+"Enter your current between 1 and 4") 
                else :  
                        if self.minutes==0 and self.hours!=0:
                            self.hours=self.hours-1
                            self.minutes=59
                        self.root.destroy()
                        self.start_Quize(self.title)        
            except Exception as e:
                print(f"An error occurred: {e}")
        def start_Quize(self,title):
            self.root=tk.Tk() 
            self.root.title(title)
            # self.root.configure(bg="#E0F5E2")
            # self.root.attributes("-fullscreen", True)       # Fullscreen
            # self.root.attributes("-topmost", True)           # Always on top
            # self.root.bind("<Escape>", lambda e: None)       # Disable ESC exit
            # self.root.protocol("WM_DELETE_WINDOW", lambda: None)  # Disable close button
            screen_width=self.root.winfo_screenwidth()  
            screen_height=self.root.winfo_screenheight()
            adjusted_screen_width= (screen_width // 2) - (screen_width // 2)
            adjusted_screen_height = (screen_height // 2) - (screen_height // 2)
            self.root.geometry(f"{screen_width}x{screen_height}+{adjusted_screen_width}+{adjusted_screen_height}")
            self.root.iconbitmap("todo.ico")
            self.time_label=tk.Label(self.root,font=("Times New Roman",30),width=5,background="light blue",borderwidth=2,relief="solid",fg="red")
            self.time_label.place(x=self.root.winfo_screenwidth()*.05,y=20)
            self.loader = QuestionLoading(self.file, self.root,self.student)  # pass file path here
            self.countdown(self.hours,self.minutes)
            self.loader.load_Questions()
            self.root.mainloop()
        def countdown(self,hours,minutes): 
            if hours == 0 and minutes == 0:
                self.time_label.config(text="0:00")
                messagebox.showinfo(title="Time's up",message="               Time over                ",parent=self.root)
                self.root.destroy()
                self.loader.permanentSave()
                return

            self.time_label.config(text=f"{hours} :{minutes:2d}")

            if minutes == 0:
                self.root.after(60000, self.countdown, hours - 1, 59)
            else:
                self.root.after(60000, self.countdown, hours, minutes - 1)
            
            
            
    class QuestionLoading():
        def __init__(self,filePath,root,name):
            self.root=root
            self.student=name
            try:
                with open(filePath, 'r') as file:
                    self.data = [line.strip() for line in file]
            except Exception as e:
                print(f"Error as {e}")
            self.current_question=0
            self.question={}
            self.l1=[] 
            self.answerList={}
            self.order = list(range(int(len(self.data)/6)))
            random.shuffle(self.order)
            j=0
            for i in range(0,int(len(self.data)/6)):
                l1=self.data[j:j+6]
                j=j+6
                self.question[i]=l1
            
        def load_Questions(self):
            ques = list(self.question[self.order[self.current_question]])      # "#F9FAF9"
            self.track_label=tk.Label(self.root,text=f"Completed 0/{int(len(self.data)/6)}",font=("Times New Roman",25),background="orange",fg="white",borderwidth=2,relief="solid")
            self.track_label.place(x=self.root.winfo_screenwidth()*.2,y=20,height=60,width=300)
            finish=tk.Button(self.root,text="Finish",font=("Times New Roman",25),command=lambda:self.end(),background="purple",fg="white",borderwidth=2,relief="solid")
            finish.place(x=self.root.winfo_screenwidth()*.85,y=20,height=50,width=180)
            self.quesLable=tk.Label(self.root,font=("Times New Roman",33),text=f"Q.{self.current_question+1} {ques[0]}",anchor="w",background="#C4DCF8",highlightthickness=2,relief="flat",highlightbackground="light gray",padx=65)
            self.quesLable.place(x=150,y=155,width=self.root.winfo_screenwidth()*.8,height=self.root.winfo_screenheight()*.2)
            self.optionLable=tk.Label(self.root,font=("Times New Roman",30),bg="#C4DCF8",highlightthickness=2,relief="flat",highlightbackground="light gray")
            self.optionLable.place(x=150,y=315,width=self.root.winfo_screenwidth()*.8,height=self.root.winfo_screenheight()*.4)
            self.answer=tk.StringVar()
            self.opt1=tk.Radiobutton(self.optionLable,text=ques[1],variable=self.answer,value=ques[1],font=("Times New Roman",25),background="#C4DCF8")
            self.opt1.place(x=100,y=50)
            self.opt2=tk.Radiobutton(self.optionLable,text=ques[2],variable=self.answer,value=ques[2],font=("Times New Roman",25),background="#C4DCF8")
            self.opt2.place(x=550,y=50)
            self.opt3=tk.Radiobutton(self.optionLable,text=ques[3],variable=self.answer,value=ques[3],font=("Times New Roman",25),background="#C4DCF8")
            self.opt3.place(x=100,y=225)
            self.opt4=tk.Radiobutton(self.optionLable,text=ques[4],variable=self.answer,value=ques[4],font=("Times New Roman",25),background="#C4DCF8")
            self.opt4.place(x=550,y=225)
            nextLable=tk.Button(self.root,text="Next",font=("Times New Roman",25),background="light blue",command=lambda:self.next_question())
            nextLable.place(x=self.root.winfo_screenwidth()*.837,y=self.root.winfo_screenheight()*0.139,width=100,height=50)
            previousLable=tk.Button(self.root,text="Previous",font=("Times New Roman",25),background="light blue",command=lambda:self.previous())
            previousLable.place(x=self.root.winfo_screenwidth()*.693,y=self.root.winfo_screenheight()*0.139,width=150,height=50)
            saveLable=tk.Button(self.root,text="Save & Next",font=("Times New Roman",20),background="red",fg="white",command=lambda:self.save(self.answer.get().strip()))
            saveLable.place(x=self.root.winfo_screenwidth()*.8,y=self.root.winfo_screenheight()*0.742,width=150,height=50)
            
        def next_question(self):
            if self.current_question>int(len(self.data)/6)-1:
                    # messagebox.showinfo(title="End of Question",message="NO more questions")
                    return     
            else:
                self.current_question += 1
                self.answer.set("")
                ques=list(self.question[self.order[self.current_question]])
                self.opt1.config(text=ques[1],value=ques[1])
                self.opt2.config(text=ques[2],value=ques[2])
                self.opt3.config(text=ques[3],value=ques[3])
                self.opt4.config(text=ques[4],value=ques[4]) 
                ques=ques[0]
                self.quesLable.config(text=f"Q.{self.current_question+1} {ques}")

        def previous(self):
            if self.current_question==0 :
                return
            else:
                self.current_question -= 1  
                ques=list(self.question[self.order[self.current_question]])
                self.opt1.config(text=ques[1],value=ques[1])
                self.opt2.config(text=ques[2],value=ques[2])
                self.opt3.config(text=ques[3],value=ques[3])
                self.opt4.config(text=ques[4],value=ques[4]) 
                ques=ques[0]
                self.quesLable.config(text=f"Q.{self.current_question+1} {ques}")
        def save(self,ans):
            if not ans:
                messagebox.showinfo("No Option Selected", "Please select an option before proceeding.")
                
            else:
                if self.current_question < len(self.order)-1:
                    self.answerList.update({self.order[self.current_question]:ans})
                    self.track_label.config(text=f"Completed {len(self.answerList)}/{int(len(self.data)/6)}")
                    ques=self.question[self.order[self.current_question]]
                    for i in range(1,5):
                        if "✔" in ques[i]:
                            ques[i] = ques[i].replace("✔", "").strip()
                    ques[ques.index(ans)]=f"{ques[ques.index(ans)].strip()} ✔"
                    self.next_question()
                    
        def permanentSave(self):     
            answers = self.answerList  
            answers=dict(sorted(answers.items()))
            try:
                with open("answer.txt", "w") as file:
                    file.write(f"Student Name :{self.student}\n")
                    for q, a in answers.items():
                        file.write(f"{q}: {a}\n") 
            except Exception as e:
                print(f"Error {e}")
        def end(self):
            s=messagebox.askquestion(title="Submit",message="Do you want to submit the quiz before the time")
            if s=="yes":
                self.permanentSave()
                messagebox.showinfo("Quiz Finished", "Your answers have been saved.")
                self.root.destroy()

    if __name__ == "__main__":
        quiz = QuizeApp()
        quiz.test_details()
except Exception as e:
    print(f" an error occured {e}")
