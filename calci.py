
# CALCULATOR

 import tkinter as tk

 mainWindow = tk.Tk()                        # defining a window
 mainWindow.title('CALCULATOR')              # setting the title of the window

 label1= tk.Label(mainWindow,text = 'ENTER FIRST NUMBER',pady=10 ,padx=10)          
 label1.pack()
 text1= tk.Entry(mainWindow)
 text1.pack()

 label2= tk.Label(mainWindow,text = 'ENTER SECOND NUMBER',pady=10,padx=10)
 label2.pack()
 text2= tk.Entry(mainWindow)
 text2.pack()
 def sumIt():                                                     # defining summation
     first= int(text1.get())
     second= int(text2.get())
     result.config(text='result : '+str(first+second))

 def subIt():                                                     # defining subtraction
     first = int(text1.get())
     second= int(text2.get())
     result.config(text='result : '+str(first-second))

 def mulIt():                                                     # defining multiplication
     first = int(text1.get())
     second = int(text2.get())
     result.config(text=first*second)

 def divIt():                                                     # defining division
     first = int(text1.get())
     second = int(text2.get())
     result.config(text = 'result :'+ str(first/second))

 button1 = tk.Button(mainWindow,text='+',command=lambda:sumIt())
 button2 = tk.Button(mainWindow,text='-',command=lambda:subIt())
 button3 = tk.Button(mainWindow,text='*',command=lambda:mulIt())
 button4 = tk.Button(mainWindow,text='/',command=lambda:divIt())

 button1.pack()
 button2.pack()
 button3.pack()
 button4.pack()

 result =tk.Label(mainWindow)
 result.pack()

 mainWindow.mainloop()
