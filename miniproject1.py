#importing all required libraries
from tkinter import *
from tkinter import ttk
import tkinter as tk 
import time
from PIL import ImageTk,Image
import speech_recognition as sr
import pyttsx3 

#storing answers of questions of each level in lists
easy_ans = ['precedence','associativity','flowchart','binary tree','binary search tree','compiler','conditional operator','variable']
med_ans = ['pointer','dictionary','structure','lambda','abstraction','indentation','new','byte']
hard_ans = ['method overloading','module','jdb','lambda','strlen','abstract method']
easy = [1]
medium = [1]
hard = [1]
itr = [2]
name = ['']
level_selected = []
#creating a tkinter welcome window
window = tk.Tk()
width= window.winfo_screenwidth()               
height= window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))
window.title("Welcome")
title = Label(window, text = "Enter your Details and select the level",font =("Algerian", 15))
title.place(x= 400,y=160)
fname = Label(window, text = "First Name",font =("Times New Roman", 13))
fname.place(x = 400, y= 220)
lname = tk.Label(text = "Last Name",font = ("Times New Roman",13))
lname.place(x=400, y= 260)
fentry = tk.Entry()
lentry = tk.Entry()
fentry.place(x= 650, y=220)
lentry.place(x= 650, y=260)

#function for retrieving name entered in textbox
def getname():
    name[0] = fentry.get() +' '+ lentry.get()
    print(name[0])
getname()

#creating combobox to display a menu of levels
level=ttk.Combobox(window, width = 20,font=("Times New Roman",15))
level.insert(END,'Select level')
level['values']=('Easy','Medium','Hard')
level.place(x=500,y=300)

#function to get the level selected by the user
def getlevel(event):
    l = level.get()
    level_selected.append(l)
    print(l)
level.bind("<<ComboboxSelected>>",getlevel)

 
#list to store the score of the user
score = [0]

#function for new window(game window)
def level_implementation():
    window.destroy()
    root = tk.Tk()
    global ren
    root.title("Game")
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry("%dx%d"%(width,height))
    root.configure(bg = 'LightSkyBlue2')
    msg = Label(root, text="Word world", font=("Algerian", 60), bg='LightSkyBlue2')
    msg.place(x=390, y=10)
    w = Canvas(root, width=1325, height=30, bg='LightSkyBlue2', highlightthickness=0)
    w.create_line(15, 25, 10000, 25, width=2)
    w.place(x=0, y=120)
    path = R"C:\Users\HP\Downloads\logo.png"
    load = Image.open(path)
    rload = load.resize((200, 125))
    ren = ImageTk.PhotoImage(rload)
    img = Label(root, image=ren)
    img.place(x=0, y=0)
    ans =  Label(root,text = "Enter answer",font = ("Times New Roman",13),bg = 'LightSkyBlue2')
    ans.place(x=400, y= 550)
    answer = tk.Entry()
    answer.place(x=500,y=550)

    
    #Function to get the current score of the player
    def get_score():
        sc =  Label(root,text = "Current score:"+str(score[0]),font = ("Times New Roman",13),bg = 'LightSkyBlue2')
        sc.place(x = 500, y= 600)
        root.after(3000,sc.destroy)

    
    #Function to display the final window
    def final_root():
        final = Toplevel(root)
        final.title("END")
        width = final.winfo_screenwidth()
        height = final.winfo_screenheight()
        final.geometry("%dx%d"%(width,height))
        my_canvas = Canvas(final, bg="MistyRose2")
        my_canvas.pack(fill="both", expand=True)
        my_canvas.create_line(200,200,250,250, fill="navy", width=2)
        my_canvas.create_line(1050, 200, 1000,250, fill="navy", width=2)
        my_canvas.create_line(200, 550, 250, 500, fill="navy", width=2)
        my_canvas.create_line(1050, 550, 1000, 500, fill="navy", width=2)
        my_canvas.create_rectangle(200,200,1050,550, outline="navy", width=2)
        my_canvas.create_rectangle(250,250,1000,500, outline="navy", width=2)
        my_canvas.create_text(width/2,height/2, text="Thanks for playing "+name[0]+"\nYour final score is "+str(score[0]), font=("Helvetica", 30), fill="black")

    
    #Function for saving the player response and going to the next question
    def Sandn():
            if(easy[0] == itr[0]):
                itr[0]+=1
            while(easy[0]<itr[0]):
                if(itr[0] == 2 ):
                    itr[0]+=1
                easy[0]+=1
                print("easy:"+str(easy[0]))
                #time.sleep(2.4)
                #get_val()
                print("itr :"+str(itr[0]))
                if(easy[0]<10):
                    display_easy() #calling display easy function for displaying the next image
                else:
                    final_root()


    
    #Function for displaying an image of level easy
    def display_easy():
        global render
        print(easy[0])
        

        
        #Function for evaluating user response
        def get_val():
            ans = answer.get()
            print(ans.lower())
            if(ans.lower() == easy_ans[easy[0]-3]):
                correct = Label(root,text = "Correct Answer",font = ("Times new Roman",13),bg = 'LightSkyBlue2')
                correct.place(x = 400, y= 600)
                root.after(2000,correct.destroy) #after 2 seconds it will remove the label
                score[0]+=10
                answer.delete(0,END)
            
            else:
                wrong = Label(root,text = "Wrong Answer",font = ("Times new Roman",13),bg = 'LightSkyBlue2')
                wrong.place(x = 400, y= 600)
                root.after(2000,wrong.destroy)
                answer.delete(0,END)
                
            score1 = Label(root,text = "Score:"+str(score[0]),font = ("Times new Roman",13),bg = 'LightSkyBlue2')  
            score1.place(x=530, y = 600)
            root.after(2000,score1.destroy)
            print(score[0])
        
        path = R"C:\Users\HP\OneDrive\Desktop\easy_im\ "
        path = path[:-1] 
        path = path +str(easy[0])+".jpeg"
        load= Image.open(path)
        rload=load.resize((300,250))
        render = ImageTk.PhotoImage(rload)
        img = Label(root, image = render)
        img.place(x=400, y=250)
        #time.sleep(2.4)
        n = Button(root,text  = "Save and Next",command =lambda:[Sandn(),get_val()],bg = "orange" ) #calling Sandn function using the button
        n.place(x=800, y = 600)
        b4 = Button(root,text  = "Exit", command = final_root,bg = "yellow" )
        b4.place(x = 100, y = 600)
   
    
    #save and next function for medium level
    def Sandn2():
            if(medium[0] == itr[0]):
                itr[0]+=1
            while(medium[0]<itr[0]):
                if(itr[0] == 2 ):
                    itr[0]+=1
                medium[0]+=1
                print("med:"+str(medium[0]))
                #time.sleep(2.4)
                #get_val()
                print("itr :"+str(itr[0]))
                if(medium[0]<10):
                    display_med() #calling display easy function for displaying the next image
                else:
                    final_root()
    
    #Function for displaying image of level medium
    def display_med():
        global render
        print(medium[0])
        ans =  Label(root,text = "Enter answer",font = ("Times New Roman",13),bg = 'LightSkyBlue2')
        

        #Function for evaluating user response
        def get_val2():
            ans = answer.get()
            print(ans.lower())
            if(ans.lower() == med_ans[medium[0]-3]):
                correct = Label(root,text = "Correct Answer",font = ("Times new Roman",13),bg = 'LightSkyBlue2')
                correct.place(x = 400, y= 600)
                root.after(2000,correct.destroy) #after 2 seconds it will remove the label
                score[0]+=10
                answer.delete(0,END)
            else:
                print("Your answer is "+ans.lower()+" Actual answer is "+med_ans[medium[0]-3])
                wrong = Label(root,text = "Wrong Answer",font = ("Times new Roman",13),bg = 'LightSkyBlue2')
                wrong.place(x = 400, y= 600)
                root.after(2000,wrong.destroy)
                answer.delete(0,END)
            score1 = Label(root,text = "Score:"+str(score[0]),font = ("Times new Roman",13),bg = 'LightSkyBlue2')  
            score1.place(x=530, y = 600)
            root.after(2000,score1.destroy)
            print(score[0])
        
        path = R"C:\Users\HP\OneDrive\Desktop\med_im\ "
        path = path[:-1] 
        path = path +str(medium[0])+".jpeg"
        load= Image.open(path)
        rload=load.resize((350,250))
        render = ImageTk.PhotoImage(rload)
        img = Label(root, image = render)
        img.place(x=400, y=250)
        #time.sleep(2.4)
        n = Button(root,text  = "Save and Next",command =lambda:[Sandn2(),get_val2()],bg = "orange" ) #calling Sandn function using the button
        n.place(x=800, y = 600)
        b4 = Button(root,text  = "Exit", command = final_root,bg = "yellow" )
        b4.place(x = 100, y = 600)

        
    #save and next function for level hard
    def Sandn3():
            if(hard[0] == itr[0]):
                itr[0]+=1
            while(hard[0]<itr[0]):
                if(itr[0] == 2 ):
                    itr[0]+=1
                hard[0]+=1
                print("hard:"+str(hard[0]))
                #time.sleep(2.4)
                #get_val()
                print("itr :"+str(itr[0]))
                if(hard[0]<8):
                    display_hard() #calling display easy function for displaying the next image
                else:
                    final_root()

    
    
    #function for displaying image of level hard
    def display_hard():
        global render
        print(hard[0])
        

        #Function for evaluating user response
        def get_val3():
            ans = answer.get()
            print(ans.lower())
            if(ans.lower() == hard_ans[hard[0]-3]):
                correct = Label(root,text = "Correct Answer",font = ("Times new Roman",13),bg = 'LightSkyBlue2')
                correct.place(x = 400, y= 600)
                root.after(2000,correct.destroy) #after 2 seconds it will remove the label
                score[0]+=10
                answer.delete(0,END)
                
            else:
                wrong = Label(root,text = "Wrong Answer",font = ("Times new Roman",13),bg = 'LightSkyBlue2')
                wrong.place(x = 400, y= 600)
                root.after(2000,wrong.destroy)
                answer.delete(0,END)
            score1 = Label(root,text = "Score:"+str(score[0]),font = ("Times new Roman",13),bg = 'LightSkyBlue2')  
            score1.place(x=530, y = 600)
            root.after(2000,score1.destroy)
            print(score[0])
        
        path = R"C:\Users\HP\OneDrive\Desktop\hard_im\ "
        path = path[:-1] 
        path = path +str(hard[0])+".jpeg"
        load= Image.open(path) 
        rload=load.resize((350,250))
        render = ImageTk.PhotoImage(rload)
        img = Label(root, image = render)
        img.place(x=400, y=250)
        #time.sleep(2.4)
        n = Button(root,text  = "Save and Next",command =lambda:[Sandn3(),get_val3()],bg = "orange" ) #calling Sandn function using the button
        n.place(x=800, y = 600)
        b4 = Button(root,text  = "Exit", command = final_root,bg = "yellow" )
        b4.place(x = 100, y = 600)
    if(level_selected[-1] == 'Easy'):
        display_easy()
    elif(level_selected[-1]=='Medium'):
        display_med()
    elif(level_selected[-1]=='Hard'):
        display_hard()
    voiceans = ['']
    
    #function for inserting the user's answer recieved through voice into textbox
    def a():
            answer.insert(0,voiceans[0])
            
    
    #Function for recognizing the user's voice i.e. for converting voice to text
    def voice_recognizer():  
    # Initialize the recognizer 
            r = sr.Recognizer()
            
        # Loop infinitely for user to speak
            while(1):
                try:    
                    # use the microphone as source for input.
                    with sr.Microphone() as source2:

                        # wait for a second to let the recognizer adjust the energy threshold based on the surrounding noise level
                        r.adjust_for_ambient_noise(source2, duration=0.2)

                        #listens for the user's input 
                        audio2 = r.listen(source2)

                        # Using google to recognize audio
                        MyText = r.recognize_google(audio2)
                        
                        voiceans[0] = str(MyText)
                        print(voiceans[0])
                        a()
                        return MyText
                        


                #exceptional handling
                except sr.RequestError as e:
                    print("Could not request results; {0}".format(e))

                except sr.UnknownValueError:
                    print("unknown error occured")

    #button for calling voice_recognizer function
    b5 = Button(root,text = "Voice",command = voice_recognizer)
    b5.place(x = 200,y = 600)
    


#button for calling level_implementation function    
b3 = tk.Button(window,text  = "Start", command = level_implementation,bg = "yellow" )
b3.place(x = 500, y = 340)



window.mainloop()



root.mainloop()
