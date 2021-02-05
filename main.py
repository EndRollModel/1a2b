import random
import tkinter as tk
import os

ans = ''


# 事件

def create_num():
    global ans
    num = ''
    while len(num) < 4:
        temp = str(random.randint(0, 9))
        if num.find(temp) > -1:
            continue
        else:
            num += str(temp)

    # print('最終答案:' + num)
    ans = num


def calc_a_b(user_ans):
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
        list_recode.insert(list_recode.size(),
                           '第' + str(list_recode.size() + 1) + '次 : ' + user_ans + '  |  a : ' + str(
                               fin_ans['a']) + ' b : ' + str(fin_ans['b']))


def check_ans():
    text_hint.configure(text='')
    if not str.isdigit(str(input_user_ans.get())):
        text_hint.configure(text='非數字字元')
    elif len(input_user_ans.get()) < 4:
        text_hint.configure(text='數字不滿四位數')
    elif len(input_user_ans.get()) > 4:
        text_hint.configure(text='數字不能大於四位數')
    elif len(input_user_ans.get()) == 4:
        if str.isdigit(input_user_ans.get()):
            calc_a_b(input_user_ans.get())
            input_user_ans.delete(0, tk.END)


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def clean_ans():
    # 清除輸入框 清除內容 清除清單
    input_user_ans.delete(0, tk.END)
    text_hint.configure(text='')
    list_recode.delete(0, tk.END)
    create_num()


# 建立視窗
windows = tk.Tk()
windows.geometry('300x500')
windows.title('1A2B')
windows.resizable(0, 0)
# 圖片
if os.path.exists(resource_path('image.png')):
    image = tk.PhotoImage(file=resource_path('image.png'))
    icon_image = tk.Label(windows, image=image)
    icon_image.pack()
# 文字
title = tk.Label(windows, text='請輸入答案數字')
title.pack()
# 輸入框
input_user_ans = tk.Entry(windows)
input_user_ans.pack()
# 確認
btn_enter = tk.Button(windows, text='確認', command=check_ans)
btn_enter.pack()
# 提示文字框
text_hint = tk.Label(windows)
text_hint.pack()
# 紀錄List
list_recode = tk.Listbox(windows)
list_recode.pack()
# 按鈕
btn_clean = tk.Button(windows, text='重來', command=clean_ans)
btn_clean.pack()
# 啟動
create_num()

windows.mainloop()
