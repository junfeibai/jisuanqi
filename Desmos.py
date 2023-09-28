#102101117刘建鑫  科学计算器
import tkinter as tk
import math#调用math库进行三角函数的运算

root = tk.Tk()
root.title('102101117计算器')  # 计算器名称
root.geometry('295x360+640+180')  # 边距，位置
root.attributes("-alpha", 0.9)  # 设置透明度

font = ('楷书', 20)  # 设置字体
font_1 = ('宋体', 16)  # 设置按键字体

# 显示最新状态，就是结果栏
result_num = tk.StringVar()
result_num.set('')  # 初始结果为空

tk.Label(
    root,
    textvariable=result_num,
    font=font,
    height=2,
    width=20,
    justify=tk.LEFT,
    anchor=tk.SE
).grid(row=1, column=1, columnspan=4)  # 网格布局

# 接下来是按键，总第2行
button_clear = tk.Button(root, text='AC', width=5, font=font_1, relief=tk.FLAT, bg='#7FFF00')  # AC按键
button_back = tk.Button(root, text='<-', width=5, font=font_1, relief=tk.FLAT, bg='#7FFF00')  # 回退
button_pi = tk.Button(root, text='π', width=5, font=font_1, relief=tk.FLAT, bg='#7FFF00')  # pi
button_cheng = tk.Button(root, text='*', width=5, font=font_1, relief=tk.FLAT, bg='#7FFF00')  # 乘

# 设置按键类型，按键位置以及按键间隔，第2行
button_clear.grid(row=2, column=1, padx=4, pady=2)
button_back.grid(row=2, column=2, padx=4, pady=2)
button_pi.grid(row=2, column=3, padx=4, pady=2)
button_cheng.grid(row=2, column=4, padx=4, pady=2)

# 接下来是按键，总第3行
button_sin = tk.Button(root, text='sin', width=5, font=font_1, relief=tk.FLAT, bg='#7FFF00')  # sin
button_cos = tk.Button(root, text='cos', width=5, font=font_1, relief=tk.FLAT, bg='#7FFF00')  # cos
button_tan = tk.Button(root, text='tan', width=5, font=font_1, relief=tk.FLAT, bg='#7FFF00')  # tan
button_chu = tk.Button(root, text='/', width=5, font=font_1, relief=tk.FLAT, bg='#7FFF00')  # 除

# 设置按键类型，按键位置以及按键间隔，第3行
button_sin.grid(row=3, column=1, padx=4, pady=2)
button_cos.grid(row=3, column=2, padx=4, pady=2)
button_tan.grid(row=3, column=3, padx=4, pady=2)
button_chu.grid(row=3, column=4, padx=4, pady=2)

# 接下来是按键，总第4行
button_gen = tk.Button(root, text='√', width=12, font=font_1, relief=tk.FLAT, bg='#7FFF00')  # 开方根号
button_kai = tk.Button(root, text='平方', width=12, font=font_1, relief=tk.FLAT, bg='#7FFF00')  # 平方

# 设置按键类型，按键位置以及按键间隔，第4行
button_gen.grid(row=4, column=1, padx=4, pady=2, columnspan=2)
button_kai.grid(row=4, column=3, padx=4, pady=2, columnspan=2)

# 接下来是按键，总第5行
button_7 = tk.Button(root, text='7', width=5, font=font_1, relief=tk.FLAT, bg='#00FFFF')  # 7按键
button_8 = tk.Button(root, text='8', width=5, font=font_1, relief=tk.FLAT, bg='#00FFFF')  # 8
button_9 = tk.Button(root, text='9', width=5, font=font_1, relief=tk.FLAT, bg='#00FFFF')  # 9
button_jian = tk.Button(root, text='-', width=5, font=font_1, relief=tk.FLAT, bg='#7FFF00')  # -

# 设置按键类型，按键位置以及按键间隔，总第5行
button_7.grid(row=5, column=1, padx=4, pady=2)
button_8.grid(row=5, column=2, padx=4, pady=2)
button_9.grid(row=5, column=3, padx=4, pady=2)
button_jian.grid(row=5, column=4, padx=4, pady=2)

# 接下来是按键，总第6行
button_4 = tk.Button(root, text='4', width=5, font=font_1, relief=tk.FLAT, bg='#00FFFF')  # 4按键
button_5 = tk.Button(root, text='5', width=5, font=font_1, relief=tk.FLAT, bg='#00FFFF')  # 5
button_6 = tk.Button(root, text='6', width=5, font=font_1, relief=tk.FLAT, bg='#00FFFF')  # 6
button_jia = tk.Button(root, text='+', width=5, font=font_1, relief=tk.FLAT, bg='#7FFF00')  # +

# 设置按键类型，按键位置以及按键间隔，总第6行
button_4.grid(row=6, column=1, padx=4, pady=2)
button_5.grid(row=6, column=2, padx=4, pady=2)
button_6.grid(row=6, column=3, padx=4, pady=2)
button_jia.grid(row=6, column=4, padx=4, pady=2)

# 接下来是按键，总第7行
button_1 = tk.Button(root, text='1', width=5, font=font_1, relief=tk.FLAT, bg='#00FFFF')  # 1按键
button_2 = tk.Button(root, text='2', width=5, font=font_1, relief=tk.FLAT, bg='#00FFFF')  # 2
button_3 = tk.Button(root, text='3', width=5, font=font_1, relief=tk.FLAT, bg='#00FFFF')  # 3
button_deng = tk.Button(root, text='=', width=5, height=3, font=font_1, relief=tk.FLAT, bg='#7FFF00')  # =

# 设置按键类型，按键位置以及按键间隔，总第7行
button_1.grid(row=7, column=1, padx=4, pady=2)
button_2.grid(row=7, column=2, padx=4, pady=2)
button_3.grid(row=7, column=3, padx=4, pady=2)
button_deng.grid(row=7, column=4, padx=4, pady=2, rowspan=2)

# 接下来是按键，总第8行
button_0 = tk.Button(root, text='0', width=12, font=font_1, relief=tk.FLAT, bg='#00FFFF')  # 0按键
button_dian = tk.Button(root, text='.', width=5, font=font_1, relief=tk.FLAT, bg='#00FFFF')  # .

# 设置按键类型，按键位置以及按键间隔，总第8行
button_0.grid(row=8, column=1, padx=4, pady=2, columnspan=2)
button_dian.grid(row=8, column=3, padx=4, pady=2)

# 添加按键函数
def click_button(x):
    current_text = result_num.get()
    # 对三角函数和π进行特殊处理
    #检查是否为三角函数，并且将输入值转换为弧度
    if x in ['sin', 'cos', 'tan']:
        try:
            angle = float(current_text)
            if x == 'sin':
                result_num.set(math.sin(math.radians(angle)))
            elif x == 'cos':
                result_num.set(math.cos(math.radians(angle)))
            elif x == 'tan':
                result_num.set(math.tan(math.radians(angle)))
        except ValueError:
            result_num.set('Error')
    elif x == 'π':
        result_num.set(math.pi)#对pi进行处理，使pi为π
    elif x == '√':
        result_num.set(math.sqrt(float(current_text)))
    elif x == '平方':
        result_num.set(float(current_text) ** 2)
    else:
        result_num.set(current_text + str(x))  # 方便输入数据

# 添加等函数
def deng():
    opt_str = result_num.get()
    try:
        result = eval(opt_str)
        result_num.set(str(result))
    except Exception:#数据错误会输出error
        result_num.set('Error')

# 添加全部清除函数
def clear():
    result_num.set('')

# 添加清除一位函数
def back():
    current_text = result_num.get()
    result_num.set(current_text[:-1])

# 设置按键响应
button_1.config(command=lambda: click_button('1'))
button_2.config(command=lambda: click_button('2'))
button_3.config(command=lambda: click_button('3'))
button_4.config(command=lambda: click_button('4'))
button_5.config(command=lambda: click_button('5'))
button_6.config(command=lambda: click_button('6'))
button_7.config(command=lambda: click_button('7'))
button_8.config(command=lambda: click_button('8'))
button_9.config(command=lambda: click_button('9'))
button_0.config(command=lambda: click_button('0'))
button_dian.config(command=lambda: click_button('.'))
button_jia.config(command=lambda: click_button('+'))
button_jian.config(command=lambda: click_button('-'))
button_cheng.config(command=lambda: click_button('*'))
button_chu.config(command=lambda: click_button('/'))
button_sin.config(command=lambda: click_button('sin'))
button_cos.config(command=lambda: click_button('cos'))
button_tan.config(command=lambda: click_button('tan'))
button_pi.config(command=lambda: click_button('π'))
button_gen.config(command=lambda: click_button('√'))
button_kai.config(command=lambda: click_button('平方'))

# 进行计算反馈
button_deng.config(command=deng)
button_clear.config(command=clear)
button_back.config(command=back)

root.mainloop()
