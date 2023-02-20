import tkinter as tk

def show_output():
    number = int(number_input.get())

    if number == 1:
        output_label.configure(text='ธงทอง หัสดี')
        return
    elif number == 2:
        output_label.configure(text='เฟื่องลดา กิติราช')
        return
    elif number == 3:
        output_label.configure(text='ดวงใจ จันทรไพดร')
        return
    else :
        output_label.configure(text='Error')
        return
    


    output_label.configure(text=output)
    
    
window = tk.Tk()
window.title('Search')
window.minsize(width=400,height=400)

title_label = tk.Label(master=window, text='Search')
title_label.pack(pady=10)

number_input=tk.Entry(master=window,width=15)
number_input.pack(pady=15)

go_button = tk.Button(master=window , text = 'Ok' ,
                      command=show_output,width=10,height=1)
go_button.pack()

output_label = tk.Label(master=window)
output_label.pack(pady=20)

window.mainloop() 
