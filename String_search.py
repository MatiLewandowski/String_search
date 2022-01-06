import tkinter as tk
from tkinter.filedialog import askdirectory
import os

def select_file_func():
    global file_name
    file_name=askdirectory()
    if file_name:
        tk.Label(main_window,text=f'You have chosen: {file_name}').pack()
    

def register_search_phrase():
    global searchfor
    searchfor=phrase.get()
    if searchfor:
        tk.Label(main_window,text=f'You are looking for: {searchfor}').pack()
    return searchfor

def search_func():
    found=0
    for root, dirs, files in os.walk(file_name):
        for file in files:
            if file.endswith(".txt"):
                path=os.path.join(root,file)           
                my_pdf=open(path,mode='r')
                if searchfor in my_pdf.read():
                    found=1
                    tk.Label(main_window,text=f'found it in {path}').pack()
    if found==0:                
        tk.Label(main_window, text='Not found').pack()    
    

main_window = tk.Tk(className='String search')
main_window.geometry('500x300')

phrase=tk.Entry(main_window)
phrase.pack()

tk.Button(main_window,text='register your word',command=register_search_phrase).pack()



tk.Button(main_window,text='Choose File',command=select_file_func).pack()

search_button=tk.Button(main_window,text='Search!',command=search_func).pack()





main_window.mainloop()
