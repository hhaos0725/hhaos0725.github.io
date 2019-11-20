from tkinter import *

root = Tk()

textLabel = Label(root,text="返回结果",relief="groove",font="宋体 20",
        height=2,width=19,pady=10)
textLabel.grid()

but = Button(root,text="导入视频")
but.grid(row=1,column=0,padx=5,pady=5)

mainloop()