int a=10;
from tkinter import *
def rgb_mixer():
    def on_drag(e):

        color_hex=f'#{sc[0].get():02X}{sc[1].get():02X}{sc[2].get():02X}'
        tv_color.set(color_hex)
        lbl_color["bg"]= color_hex

    root =Tk()
    root.option_add("*Font","Consolas50")
    tv_color = StringVar()
    rgb = ['red','green','blue']
    sc = []
    photo1 = PhotoImage(file="1.png")
    
    for i, c in enumerate(rgb):
        Label(root, image=photo1,bg="skyblue").grid(row=5, columnspan=2, sticky="news")
    
        Label(root, text=c, fg=c,bg="skyblue").grid(row=i, column=0,sticky="SW")
        w = Scale(root, from_=0, to=255, orient=HORIZONTAL, length=500,width=30,fg=c,bg="skyblue")
        w.grid(row=i, column=1)
        w.set(128)
        w.bind('<B1-Motion>',on_drag)
        w.bind('<Button-1>',on_drag)
        sc.append(w)

    lbl_color = Label(root,textvariable=tv_color)
    lbl_color.grid(row=3, columnspan=2,sticky="news")
    root.mainloop()


def rating():
    def on_drag(e):
        total = 0
        for score in sc:
            total += score.get()
        rating_score.set(f'avg.={total/len(sc):.2f}')

    root = Tk()
    root.option_add("*Font","consolas 20")
    rating_score = StringVar()
    criteria = ['price','performance','design','service','reliability']
    sc = []
    for i, c in enumerate(criteria):
        Label(root, text=c).grid(row=i, column=0, sticky="sw")
        w = scale(root, from_=1, to=10, orient=HORIZONTAL, length=500, width=30)
        w.gid(row=i, column=1)
        w.set(5)
        w.bind('<B1-Motion>',on_drag)
        w.bind('<Button-1',on_drag)
        sc.append(w)
    lbl_color = Label(root, textvariable=rating_score, bg="gold")
    lbl_color.grid(columnspan=2, sticky="news")
    root.mainloop()

if __name__== '__main__':
    rgb_mixer()
