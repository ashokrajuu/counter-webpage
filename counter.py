#import library
import tkinter as tk

# import pandas as pd
# import numpy as np
# cols = [0]
# df = pd.read_excel("D:\\training\\metrics.xlsx", usecols=cols)
# print(df)


#counting function
def charcount():
    output.delete(0.0,"end")
    w=inputUser.get(df,"end")
    sp=decision.get()
    c=0
#specifying conditions
    if sp==1:
#        for k in w:
        print(w)
        if "namespace=" in w:
            c=c+1
    elif sp==2:
#        for k in w:
#            print(k)
            if "configmap=" in w:
              c=c+1
    output.insert(tk.INSERT,c)
    output2.insert(tk.INSERT,"Updated soon")
#creating interface
window=tk.Tk()
window.title("Count Characters")
window.geometry("500x600")
label=tk.Label(window,text="Input")
#Formatting
inputUser=tk.Text(window,width=450,height=10,font=("Helvetica",16),wrap="word")
decision=tk.IntVar()
#Radio buttons for space counting
r1=tk.Radiobutton(window,text="namespace",value=1,variable=decision)
r2=tk.Radiobutton(window,text="configmap",value=2,variable=decision)
#BUtton to count 
button=tk.Button(window,text="Count the number of characters",command=charcount)
label2=tk.Label(window,text="number of characters")
#Output Block
output=tk.Text(window,width=20,height=2,font=("Helvetica",16),wrap="word")

#Display Findings
label3=tk.Label(window,text="Findings")
#Output Block
output2=tk.Text(window,width=20,height=2,font=("Helvetica",16),wrap="word")

#Function calling
label.pack()
inputUser.pack()
r1.pack()
r2.pack()
label2.pack()
output.pack()
label3.pack()
output2.pack()
button.pack()
window.mainloop()
