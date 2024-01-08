import tkinter
import qrcode  
import os 
import cv2 
import customtkinter 

# Start implementing the GUI 
customtkinter.set_appearance_mode("Light") 
cp = tkinter.Tk() 
cp.title('QRCode Generator & Scanner ') 
cp.geometry('350x350') 
cp.config(bg='#0D5F5F') 

# Generate QR_code function
def generate(): 
    img = qrcode.make(msg.get()) 
    type(img) 
    img.save(f'{save_name.get()}.png') 
    tkinter.Label(cp, text='File Saved!', bg='#052A2A' , fg='white', font=('Louis George Cafe Bold Italic', 8)).pack() 

# Display QR_code function
def show(): 
    img = qrcode.make(msg.get()) 
    type(img) 
    img.show() 
 
# Open any QR_code image and scan it 
def open_file(): 
   file = tkinter.filedialog.askopenfile(mode='r+', filetypes=[('png', '*.png')]) 
   filepath = os.path.abspath(file.name)  
    
   # scan the QRCODE image 
   image = cv2.imread(filepath) 
   detector = cv2.QRCodeDetector() 
   data, vertices_array, binary_qrcode = detector.detectAndDecode(image) 


   if vertices_array is not None: 
        print("QRCode data:") 
        print(data) 
   else: 
        print("There was some error") 


frame = tkinter.Frame(cp, bg='#0D5F5F') 
frame.pack(expand=True) 
 
# Enter the text or URL
 
tkinter.Label(frame, text='URL: ', font=('Louis George Cafe Bold', 16), 
      bg='#0D5F5F').grid(row=0, column=0, sticky='w') 
 
msg = tkinter.Entry(frame) 
msg.grid(row=0, column=1) 
 
# Enter the file name 
 
tkinter.Label(frame, text='Save As: ', font=('Louis George Cafe Bold', 16), 
      bg='#0D5F5F').grid(row=1, column=0, sticky='w') 
 
save_name = tkinter.Entry(frame) 
save_name.grid(row=1, column=1) 
 
# Buttons to (Show, Scan, Save) 
 
btn = customtkinter.CTkButton(cp, text='Show QRCode', bd='6', command=show, width=20,fg_color=("white","black")) 
btn.pack() 

btn = customtkinter.CTkButton(cp, text='Save QRCode', command=generate, bd='6', width=20,fg_color=("white","black")) 
btn.pack() 
  
btn1= customtkinter.CTkButton(cp,text='Scan QRCode',bd='6',command=open_file,width=20,fg_color=("white","black")) 
btn1.pack() 
 
cp.mainloop()