import random
import tkinter as tk
import os

ans = ''
while len(ans) < 4:
    num = str(random.randint(0, 9))
    if ans.find(num) > -1:
        continue
    else:
        ans += str(num)


# 事件
def calcAB(user_ans):
    fin_ans = {'a': 0, 'b': 0}
    for i in range(len(ans)):
        for j in range(len(user_ans)):
            if ans[i] == user_ans[i]:
                fin_ans['a'] += 1
                break
            if ans[i] == user_ans[j]:
                fin_ans['b'] += 1
                break

    # print('a :' + str(fin_ans['a']) + ' b :' + str(fin_ans['b']))
    if fin_ans['a'] == 4:
        text_hint.configure(text='正確答案:' + ans)
    else:
        recode_list.insert(recode_list.size(), user_ans + '  |  a : ' + str(fin_ans['a']) + ' b : ' + str(fin_ans['b']))


def check_ans():
    if len(ans_input.get()) < 4:
        text_hint.configure(text='數字不滿四位數')
    else:
        # print(type(ans_input.get()))
        calcAB(ans_input.get())


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# 建立視窗
windows = tk.Tk()
windows.geometry('300x500')
windows.title('1A2B')
windows.resizable(0, 0)
# 圖片
print(resource_path('image.png'))
if os.path.exists(resource_path('image.png')):
    image = tk.PhotoImage(file=resource_path('image.png'))
    icon_image = tk.Label(windows, image=image)
    icon_image.pack()
# 文字
title = tk.Label(windows, text='請輸入答案數字', )
title.pack()
# 輸入框
ans_input = tk.Entry(windows)
ans_input.pack()
# 確認
enter_num = tk.Button(windows, text='確認', command=check_ans)
enter_num.pack()
# 提示文字框
text_hint = tk.Label(windows)
text_hint.pack()
# 紀錄List
recode_list = tk.Listbox(windows)
recode_list.pack()

windows.mainloop()
