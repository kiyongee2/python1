# 사전 만들기
from tkinter import *

def select():
    word = entry.get()
    definition = dic[word]
    output.delete(0.0, END)
    output.insert(END, definition)

# 딕셔너리
dic = {
    "알고리즘": "어떤 문제를 해결하기 위한 절차나 방법을 설명해 놓은 것",
    "인공지능": "인공적으로 만든 지능으로 지능이란 지적 작업에 필요한 능력",
    "이진수:": "2진법으로 나타낸 숫자, 0과 1로 구성됨"
}

root = Tk()
root.title("용어 사전")

lbl = Label(root)
lbl.config(text="단어를 입력하고 엔터 키를 누르세요")
lbl.grid(row=0, column=0, sticky=W)

entry = Entry(root, width=20, bg="yellowgreen")
entry.grid(row=1, column=0, sticky=W)

btn = Button(root, command=select)
btn.config(text="제출")
btn.grid(row=2, column=0, sticky=W)

Label(root, text="정의").grid(row=3, column=0, sticky=W)
output = Text(root, width=80, height=10, bg="yellowgreen")
output.grid(row=4, column=0, sticky=W)


root.mainloop()