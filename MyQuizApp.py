import  tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
try:
    class QuizeApp():
        def __init__(self,inputfile,hour,minute):
                self.file=inputfile
                self.hour=hour
                self.minute=minute

        def student_details(self):
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
            self.root.iconbitmap("todo.ico")
            self.root.configure(bg="#EAECE8")
            name_label=tk.Label(self.root,text="Name  :",font=("Times New Roman",20))
            name_label.place(x=150,y=70)
            name=tk.StringVar()
            name_box=tk.Entry(self.root,textvariable=name,font=("Arial",15))
            name_box.place(x=275,y=75,height=25,width=300)
            name_box.insert(0,"Vivek, Yash , Nitin etc.")
            name_box.bind('<FocusIn>',entry_delete1)

            class_label=tk.Label(self.root,text="Year  :",font=("Times New Roman",20))
            class_label.place(x=150,y=150)
            year=tk.StringVar()
            class_box=tk.Entry(self.root,textvariable=year,font=("Arial",15))
            class_box.place(x=275,y=150,height=25,width=300)
            class_box.insert(0,"1,2,3,4")
            class_box.bind('<FocusIn>',entry_delete2)
            startbtn=tk.Button(self.root,text="Start",width=7,command=lambda:QuizeApp.check_details(self,self.root,name.get().strip(),year.get().strip()),bg="light blue",font=("Times New Roman",20))
            startbtn.place(x=300,y=300)
            self.root.mainloop()
            return(name.get().strip(),year.get().strip())
        def check_details(self,window,n,c):
            l=("1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","^","&","*",'(',")",'/',"?")
            try:
                if n.startswith(l) or n.endswith(l):
                    messagebox.showerror(message="Invalid Name")
                elif (len(n)>20 or len(n)<4):
                    messagebox.showerror(message="Invalid Name")
                elif not c.isdigit():
                    messagebox.showerror(message="Invalid Entry: Please enter a number between 1 and 4")
                elif int(c) not in range(1,5):
                    messagebox.showerror(message="Invalid Entry "+"Enter your current between 1 and 4") 
                else :
                    window.destroy()
                    QuizeApp.start_Quize(self,self.hour,self.minute) 
            except Exception as e:
                print(f"An error occurred: {e}")
        def start_Quize(self,h,m):
            self.root=tk.Tk() 
            self.root.title("Quiz App")
            # self.root.configure(bg="#E0F5E2")
            # self.root.attributes("-fullscreen", True)       # Fullscreen
            # self.root.attributes("-topmost", True)           # Always on top
            self.root.bind("<Escape>", lambda e: None)       # Disable ESC exit
            self.root.protocol("WM_DELETE_WINDOW", lambda: None)  # Disable close button
            screen_width=self.root.winfo_screenwidth()  
            screen_height=self.root.winfo_screenheight()
            adjusted_screen_width= (screen_width // 2) - (screen_width // 2)
            adjusted_screen_height = (screen_height // 2) - (screen_height // 2)
            self.root.geometry(f"{screen_width}x{screen_height}+{adjusted_screen_width}+{adjusted_screen_height}")
            self.root.iconbitmap("todo.ico")
            self.loader = QuestionLoading(self.file)  # pass file path here
            self.countdown(h,m,self.root)
            self.loader.load_Questions(self.root)
            # QuizeApp.countdown(h,m,self.root) 
            # QuestionLoading.load_Questions(self.root)
            self.root.mainloop()
        def countdown(self,hours,minutes,window):
            time_label=tk.Label(window,font=("Times New Roman",30),width=5,background="light blue",borderwidth=2,relief="solid",fg="red")
            time_label.place(x=window.winfo_screenwidth()*.05,y=20)
            if hours == 0 and minutes == 0:
                time_label.config(text="0:00")
                messagebox.showinfo(title="Time's up",message="               Time over                ",parent=window)
                window.destroy()
                self.loader.permanentSave()
                
                return

            time_label.config(text=f"{hours}:{minutes:2d}")

            if minutes == 0:
                window.after(60000, QuizeApp.countdown, self,hours - 1, 59,window)
            else:
                window.after(60000, QuizeApp.countdown, self,hours, minutes - 1,window)
        
            
    class QuestionLoading():
        def __init__(self,filePath):
            with open(filePath, 'r') as file:
                self.reader = file.readlines()
                self.data=list(self.reader)
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
            
        def load_Questions(self,window):
            ques = list(self.question[self.order[self.current_question]])      # "#F9FAF9"
            track_label=tk.Label(window,text=f"Completed 0/{int(len(self.data)/6)}",font=("Times New Roman",25),background="orange",fg="white",borderwidth=2,relief="solid")
            track_label.place(x=window.winfo_screenwidth()*.2,y=20,height=60,width=300)
            finish=tk.Button(window,text="Finish",font=("Times New Roman",25),command=lambda:QuestionLoading.end(self,window),background="purple",fg="white",borderwidth=2,relief="solid")
            finish.place(x=window.winfo_screenwidth()*.85,y=20,height=50,width=180)
            quesLable=tk.Label(window,font=("Times New Roman",33),text=f"Q.{self.current_question+1} {ques[0]}",anchor="w",background="#C4DCF8",highlightthickness=2,relief="flat",highlightbackground="light gray",padx=65)
            quesLable.place(x=150,y=155,width=window.winfo_screenwidth()*.8,height=window.winfo_screenheight()*.2)
            optionLable=tk.Label(window,font=("Times New Roman",30),bg="#C4DCF8",highlightthickness=2,relief="flat",highlightbackground="light gray")
            optionLable.place(x=150,y=315,width=window.winfo_screenwidth()*.8,height=window.winfo_screenheight()*.4)
            self.answer=tk.StringVar()
            opt1=tk.Radiobutton(optionLable,text=ques[1],variable=self.answer,value=ques[1],font=("Times New Roman",25),background="#C4DCF8")
            opt1.place(x=100,y=50)
            opt2=tk.Radiobutton(optionLable,text=ques[2],variable=self.answer,value=ques[2],font=("Times New Roman",25),background="#C4DCF8")
            opt2.place(x=550,y=50)
            opt3=tk.Radiobutton(optionLable,text=ques[3],variable=self.answer,value=ques[3],font=("Times New Roman",25),background="#C4DCF8")
            opt3.place(x=100,y=225)
            opt4=tk.Radiobutton(optionLable,text=ques[4],variable=self.answer,value=ques[4],font=("Times New Roman",25),background="#C4DCF8")
            opt4.place(x=550,y=225)
            nextLable=tk.Button(window,text="Next",font=("Times New Roman",25),background="light blue",command=lambda:QuestionLoading.next_question(self,quesLable,opt1,opt2,opt3,opt4))
            nextLable.place(x=window.winfo_screenwidth()*.837,y=window.winfo_screenheight()*0.139,width=100,height=50)
            previousLable=tk.Button(window,text="Previous",font=("Times New Roman",25),background="light blue",command=lambda:QuestionLoading.previous(self,quesLable,opt1,opt2,opt3,opt4))
            previousLable.place(x=window.winfo_screenwidth()*.693,y=window.winfo_screenheight()*0.139,width=150,height=50)
            saveLable=tk.Button(window,text="Save & Next",font=("Times New Roman",20),background="red",fg="white",command=lambda:QuestionLoading.save(self,self.answer.get(),quesLable,opt1,opt2,opt3,opt4,track_label))
            saveLable.place(x=window.winfo_screenwidth()*.8,y=window.winfo_screenheight()*0.742,width=150,height=50)
            
        def next_question(self,label,opt1,opt2,opt3,opt4):
            self.current_question += 1
            if self.current_question>int(len(self.data)/6)-1:
                    messagebox.showinfo(title="End of Question",message="NO more questions")     
        
            else:
                self.answer.set("")
                ques=list(self.question[self.order[self.current_question]])
        

                a=ques[1]
                
                b=ques[2]
                c=ques[3]
                d=ques[4]
                ques=ques[0]
                label.config(text=f"Q.{self.current_question+1} {ques}")
                opt1.config(text=a,value=a)
                opt2.config(text=b,value=b)
                opt3.config(text=c,value=c)
                opt4.config(text=d,value=d) 

        def previous(self,label,opt1,opt2,opt3,opt4):
            self.current_question
            if self.current_question!=0 :
                self.current_question -= 1
            if self.current_question>int(len(self.data)/6)-1:
                    messagebox.showinfo(title="End of Question",message="NO more questions")
            
            else:
                ques=list(self.question[self.order[self.current_question]])
                
                a=ques[1]
                b=ques[2]
                c=ques[3]
                d=ques[4]
                ques=ques[0]
                label.config(text=f"Q.{self.current_question+1} {ques}")
                opt1.config(text=a,value=a)
                opt2.config(text=b,value=b)
                opt3.config(text=c,value=c)
                opt4.config(text=d,value=d) 
        def save(self,ans,label,opt1,opt2,opt3,opt4,track):
            if not ans:
                messagebox.showinfo("No Option Selected", "Please select an option before proceeding.")
            else:
                if self.current_question < len(self.order):
                    self.answerList.update({self.order[self.current_question]:ans})
                    track.config(text=f"Completed {len(self.answerList)}/{int(len(self.data)/6)}")
                    ques=self.question[self.order[self.current_question]]
                    for i in range(1,5):
                        if "✔" in ques[i]:
                            ques[i] = ques[i].replace("✔", "").strip()
                    ques[ques.index(ans)]=f"{ques[ques.index(ans)].strip()} ✔"
                    QuestionLoading.next_question(self,label,opt1,opt2,opt3,opt4)
                    
        def permanentSave(self):     
            answers = self.answerList  
            answers=dict(sorted(answers.items()))
            with open("answer.txt", "w") as file:
                for q, a in answers.items():
                    file.write(f"{q}: {a}") 
        def end(self,window):
            s=messagebox.askquestion(title="Submit",message="Do you want to submit the quiz before the time")
            if s=="yes":
                QuestionLoading.permanentSave(self)
                messagebox.showinfo("Quiz Finished", "Your answers have been saved.")
                window.destroy()

    if __name__ == "__main__":
        quiz = QuizeApp("questionlist.txt", 0, 2)
        quiz.student_details()  
except Exception as e:
    print(f" an error occured {e}")
