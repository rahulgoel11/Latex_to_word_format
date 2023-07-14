import latex2mathml.converter
from tkinter import *
root = Tk()
root.title("Latex Converter")
window_width = 700
window_height = 450
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_left = int(screen_width / 2 - window_width / 2)
root.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")



canvas1 = Canvas(root, width=500, height=400, relief='raised')

canvas1.pack()
label1 = Label(root, text="Enter LATEX code:", font=('helvetica', 8, 'bold'))

canvas1.create_window(0, 35, window=label1)
# 
entry1 = Text(root,height=5, width=50) 
# entry1 = Entry(root) 
canvas1.create_window(300, 50, window=entry1)

# def copy_text_to_clipboard(event):
#     field_value = event.widget.get("1.0", 'end-1c')  # get field value from event, but remove line return at end
#     root.clipboard_clear()  # clear clipboard contents
#     root.clipboard_append(field_value)  # append new value to clipbaord

def copy_text_to_clipboard(event):
    root.clipboard_clear()  # clear clipboard contents
    root.clipboard_append(event)  # append new value to clipbaord    
    
    
def get_square_root():
#     x1 = entry1.get()
    x1 = entry1.get("1.0", "end-1c")  

    x1 = x1.lstrip('$').rstrip('$')
    label3 = Label(root, text='Converted Code is:', font=('helvetica', 8, 'bold'))
    canvas1.create_window(0, 300, window=label3)
    
    try:
        mathml_output = '<?xml version="1.0"?>' + latex2mathml.converter.convert(x1)
    except:
        mathml_output = "Latex not correct"

    label4 = Text(root,height=5, width=50)
    canvas1.create_window(300, 300, window=label4)
    
    label4.insert(END, mathml_output)
#     label4.bind("<Button-1>", copy_text_to_clipboard)
    
    button2 = Button(root,text='Copy', command=lambda: copy_text_to_clipboard(mathml_output), bg='red', fg='white', font=('helvetica', 9, 'bold'),height=2, width=20)
    canvas1.create_window(270, 400, window=button2)
    
button1 = Button(root,text='Convert LATEX', command=get_square_root, bg='red', fg='white', font=('helvetica', 9, 'bold'),height=2, width=20)
canvas1.create_window(270, 170, window=button1)

root.mainloop()