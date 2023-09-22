from tkinter import * 
import qrcode  
from tkinter import ttk, filedialog 
from tkinter.filedialog import askopenfile 
import os 
import cv2 
import customtkinter 
 
 
customtkinter.set_appearance_mode("Light") 
cp = Tk() 
cp.title('QRCode Generator & Scanner ') 
cp.geometry('350x350') 
cp.config(bg='#0D5F5F') 

def generate(): 
    img = qrcode.make(msg.get()) 
    type(img) 
    img.save(f'{save_name.get()}.png') 
    Label(cp, text='File Saved!', bg='#052A2A' , fg='white', font=('Louis George Cafe Bold Italic', 8)).pack() 
 
def show(): 
    img = qrcode.make(msg.get()) 
    type(img) 
    img.show() 
 
 
def open_file(): 
   file = filedialog.askopenfile(mode='r+', filetypes=[('png', '*.png')]) 
   filepath = os.path.abspath(file.name)  
    
   # read the QRCODE image 
   image = cv2.imread(filepath) 
   detector = cv2.QRCodeDetector() 
   data, vertices_array, binary_qrcode = detector.detectAndDecode(image) 


   if vertices_array is not None: 
        print("QRCode data:") 
        print(data) 
   else: 
        print("There was some error") 


frame = Frame(cp, bg='#0D5F5F') 
frame.pack(expand=True) 
 
#------------------ENTER THE TEXT OR URL------------------ 
 
Label(frame, text='URL: ', font=('Louis George Cafe Bold', 16), 
      bg='#0D5F5F').grid(row=0, column=0, sticky='w') 
 
msg = Entry(frame) 
msg.grid(row=0, column=1) 
 
#------------------ENTER THE FILE NAME------------------ 
 
Label(frame, text='Save As: ', font=('Louis George Cafe Bold', 16), 
      bg='#0D5F5F').grid(row=1, column=0, sticky='w') 
 
save_name = Entry(frame) 
save_name.grid(row=1, column=1) 
 
#------------------BUTTONS TO SHOW AND SAVE AND SCAN QRCODE------------------ 
 
btn = customtkinter.CTkButton(cp, text='Show QRCode', bd='6', command=show, width=20,fg_color=("white","black")) 
btn.pack() 

btn = customtkinter.CTkButton(cp, text='Save QRCode', command=generate, bd='6', width=20,fg_color=("white","black")) 
btn.pack() 
  
btn1= customtkinter.CTkButton(cp,text='Scan QRCode',bd='6',command=open_file,width=20,fg_color=("white","black")) 
btn1.pack() 
 
cp.mainloop()