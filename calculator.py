#102101117刘建鑫  简单计算器
import tkinter as tk

root=tk.Tk()
root.title('102101117计算器')#计算器名称
root.geometry('295x280+640+180')#边距，位置

root.attributes("-alpha",0.9)#设置透明度

font=('楷书',20)#设置字体
font_1=('宋体',16)#设置按键字体


#显示最新状态，就是结果栏
result_num=tk.StringVar()
result_num.set('')#初始结果为空

tk.Label(root,
         textvariable=result_num, font=font, height=2,
         width=20,justify=tk.LEFT,anchor=tk.SE
         ).grid(row=1,column=1,columnspan=4
                )#网格布局

#接下来是按键，总第二行
button_clear=tk.Button(root,text='AC',width=5,font=font_1,relief=tk.FLAT,bg='#7FFF00')#AC按键
button_back=tk.Button(root,text='<-',width=5,font=font_1,relief=tk.FLAT,bg='#7FFF00')#回退
button_chu=tk.Button(root,text='/',width=5,font=font_1,relief=tk.FLAT,bg='#7FFF00')#除
button_cheng=tk.Button(root,text='*',width=5,font=font_1,relief=tk.FLAT,bg='#7FFF00')#乘

#设置按键类型，按键位置以及按键间隔，第二行
button_clear.grid(row=2,column=1,padx=4,pady=2)
button_back.grid(row=2,column=2,padx=4,pady=2)
button_chu.grid(row=2,column=3,padx=4,pady=2)
button_cheng.grid(row=2,column=4,padx=4,pady=2)


#接下来是按键，总第三行
button_7=tk.Button(root,text='7',width=5,font=font_1,relief=tk.FLAT,bg='#00FFFF')#7按键
button_8=tk.Button(root,text='8',width=5,font=font_1,relief=tk.FLAT,bg='#00FFFF')#8
button_9=tk.Button(root,text='9',width=5,font=font_1,relief=tk.FLAT,bg='#00FFFF')#9
button_jian=tk.Button(root,text='-',width=5,font=font_1,relief=tk.FLAT,bg='#7FFF00')#-

#设置按键类型，按键位置以及按键间隔，总第三行
button_7.grid(row=3,column=1,padx=4,pady=2)
button_8.grid(row=3,column=2,padx=4,pady=2)
button_9.grid(row=3,column=3,padx=4,pady=2)
button_jian.grid(row=3,column=4,padx=4,pady=2)

#接下来是按键，总第四行
button_4=tk.Button(root,text='4',width=5,font=font_1,relief=tk.FLAT,bg='#00FFFF')#4按键
button_5=tk.Button(root,text='5',width=5,font=font_1,relief=tk.FLAT,bg='#00FFFF')#5
button_6=tk.Button(root,text='6',width=5,font=font_1,relief=tk.FLAT,bg='#00FFFF')#6
button_jia=tk.Button(root,text='+',width=5,font=font_1,relief=tk.FLAT,bg='#7FFF00')#+

#设置按键类型，按键位置以及按键间隔，总第四行
button_4.grid(row=4,column=1,padx=4,pady=2)
button_5.grid(row=4,column=2,padx=4,pady=2)
button_6.grid(row=4,column=3,padx=4,pady=2)
button_jia.grid(row=4,column=4,padx=4,pady=2)

#接下来是按键，总第五行
button_1=tk.Button(root,text='1',width=5,font=font_1,relief=tk.FLAT,bg='#00FFFF')#1按键
button_2=tk.Button(root,text='2',width=5,font=font_1,relief=tk.FLAT,bg='#00FFFF')#2
button_3=tk.Button(root,text='3',width=5,font=font_1,relief=tk.FLAT,bg='#00FFFF')#3
button_deng=tk.Button(root,text='=',width=5,height=3,font=font_1,relief=tk.FLAT,bg='#7FFF00')#=

#设置按键类型，按键位置以及按键间隔，总第五行
button_1.grid(row=5,column=1,padx=4,pady=2)
button_2.grid(row=5,column=2,padx=4,pady=2)
button_3.grid(row=5,column=3,padx=4,pady=2)
button_deng.grid(row=5,column=4,padx=4,pady=2,rowspan=2)

#接下来是按键，总第6行
button_0=tk.Button(root,text='0',width=12,font=font_1,relief=tk.FLAT,bg='#00FFFF')#0按键
button_dian=tk.Button(root,text='.',width=5,font=font_1,relief=tk.FLAT,bg='#00FFFF')#.

#设置按键类型，按键位置以及按键间隔，总第6行
button_0.grid(row=6,column=1,padx=4,pady=2,columnspan=2)
button_dian.grid(row=6,column=3,padx=4,pady=2)

#添加按键函数
def click_button(x):
    print('x:\t',x)
    result_num.set(result_num.get()+x)#方便输入数据

#添加等函数
def deng():
    opt_str=result_num.get()
    result = eval(opt_str)
    result_num.set(str(result))

#添加全部清除函数
def clear():
    result_num.set('')

#添加清除一位函数
def back():
    current_text = result_num.get()
    result_num.set(current_text[:-1])


#设置按键响应
button_1.config(command=lambda:click_button('1'))
button_2.config(command=lambda:click_button('2'))
button_3.config(command=lambda:click_button('3'))
button_4.config(command=lambda:click_button('4'))
button_5.config(command=lambda:click_button('5'))
button_6.config(command=lambda:click_button('6'))
button_7.config(command=lambda:click_button('7'))
button_8.config(command=lambda:click_button('8'))
button_9.config(command=lambda:click_button('9'))
button_0.config(command=lambda:click_button('0'))
button_dian.config(command=lambda:click_button('.'))
button_jia.config(command=lambda:click_button('+'))
button_jian.config(command=lambda:click_button('-'))
button_cheng.config(command=lambda:click_button('*'))
button_chu.config(command=lambda:click_button('/'))


#进行计算反馈
button_deng.config(command=deng)
button_clear.config(command=clear)
button_back.config(command=back)


root.mainloop()


