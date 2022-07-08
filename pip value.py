# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 17:32:11 2022

@author: lorel
"""
## CALXULATE PIP Value
# get bank account
# set risk
# determine sl
import tkinter as tk
from tkinter import *
#risk = 2 #%
#balance = 500
#stop_rate = 10 #(sl distance)

def pip_value():
        
    
    
        risks = input(int())
        print('risk ' + str(risks))        
        balances = input(int())
        print('balance' + str(balances))
        stop_rates = input(int())
        print('stop_rate' + str(stop_rates))
        pip_value = int(balances) * int(risks) / int(stop_rates)
        print('pip value' + str(pip_value))
    

    
window = tk.Tk()

window.title("Welcome to Py App")
window.geometry('500x500')

lbl = tk.Label(window, text="Risk \n\n balance \n\n stop_rate \n\n pip value", font = ('helvetica', 12, 'bold'))
lbl.grid(column=0, row=0)

lblButton = tk.Label(window, text="")
lblButton.grid(column=2, row=0)    


                        
btn = tk.Button(window, text="Exit", bg="grey", fg="black", command=window.destroy)
btn.grid(column=1, row=1)

#button = tk.Button(window, text="risk", command = window)
#button.pack()

#button = tk.Button(window, text="balance", command=window)
#button.pack()

#button = tk.Button(window, text="stop_rate", command=window)
#button.pack()

#button = tk.Button(window, text="pip_value", command=window)
#button.pack()
text = Text(window)

txtBox = tk.Entry(window,width=10)
txtBox.grid(column=0, row=1)    

txtBox.focus()



window.mainloop()



## TO GET .exe file of the previous function code

### on command prompt type nome cartella
## cd C:\Users\lorel\Desktop\lore\Predictable\Nuova cartella

## pip install pyinstaller on python

## pyinstaller --onefile pip value.py

##go in the folder nuova cartella  C:\Users\lorel\Desktop\lore\Predictable\Nuova cartella
## open dist and then click on the .exe application file type