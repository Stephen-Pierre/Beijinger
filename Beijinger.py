import tkinter as tk

top = tk.Tk()
top.geometry("400x600")
top.title("北京口音翻译器")
label1 = tk.Label(top, text = "请输入要翻译的内容：", font = ("宋体", 18))
# 设置标签位置
label1.grid(row = 0, sticky = tk.W)

# 设置文本输入框
textarea = tk.Entry(top)
# 设置文本框的位置
textarea.grid(row = 1,sticky = tk.W, rowspan = 5)


# 定义翻译函数
def translate():
    # 获取文本框内容
    text = textarea.get()
    res = '儿'.join(text)
    res = res + "儿"
    textarea1.insert(tk.INSERT, res)



# 设置翻译按钮
button1 = tk.Button(top, text = "点我翻译", font = ("宋体", 18), command = translate)
# button1.configure(width = 580, height = 10)
# 设置标签位置
button1.grid(row = 7,sticky = tk.W)


# 用于显示翻译结果的文本框
textarea1 = tk.Text(top, font = ("宋体", 18))
textarea1.grid(row = 8,sticky = tk.W)

    
    
top.mainloop()
