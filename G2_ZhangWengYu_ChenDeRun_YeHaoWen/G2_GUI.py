from tkinter import*
win = Tk()
win.title("Workshops Enrollment System - Group2")
width = 600
height = 600
screenwidth = win.winfo_screenwidth()
screenheight = win.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)
win.geometry(alignstr)
win.resizable(width=False, height=False)


# main login page
main_page = Canvas(win).place(x=0,y=0)

# title lable

main_title = Label(main_page,text="Welcome to use Workshops Enrollment System made by Group 2!\n\nZHANG Wengyu21098431d\nCHEN Derun21098424d\nYE Haowen21098829d",font=(CENTER,14)).place(x=85,y=50)
sub_title = Label(main_page,text="Please select your indentity to login or register",font=(CENTER,14)).place(x=150,y=200)

# user and password label
Label(main_page,text='User:').place(x=150,y=300)
Label(main_page,text='Password:').place(x=150,y=350)

# user entry
var_usr_name=StringVar()
entry_usr_name=Entry(main_page,textvariable=var_usr_name)
entry_usr_name.place(x=250,y=300)

# password entry
var_usr_pwd=StringVar()
entry_usr_pwd=Entry(main_page,textvariable=var_usr_pwd,show='*')
entry_usr_pwd.place(x=250,y=350)


def quit_linster():
    win.destroy()
    
def register_linster():
    #register page
    win_reg=Toplevel(main_page)
    screenwidth = win.winfo_screenwidth()
    screenheight = win.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (400, 250, (screenwidth-width)/2, (screenheight-height)/2)
    win_reg.geometry(alignstr)
    
    win_reg.title('Register New Account')
    # user
    new_name=StringVar()
    Label(win_reg,text='User:').place(x=10,y=10)
    Entry(win_reg,textvariable=new_name).place(x=150,y=10)
    #password
    new_pwd=StringVar()
    Label(win_reg,text='Enter Password').place(x=10,y=50)
    Entry(win_reg,textvariable=new_pwd,show='*').place(x=150,y=50)    
    #password confirm
    new_pwd_confirm=StringVar()
    Label(win_reg,text='Conform Password:').place(x=10,y=90)
    Entry(win_reg,textvariable=new_pwd_confirm,show='*').place(x=150,y=90)    
    #confirm button
    bt_confirm_sign_up=Button(win_reg,text='Confirm',)
    bt_confirm_sign_up.place(x=150,y=130)

# 3 buttons
bt_login=Button(main_page,text='Login')
bt_login.place(x=150,y=400)
bt_register=Button(main_page,text='Register',command = register_linster)
bt_register.place(x=250,y=400)
bt_quit=Button(main_page,text='Quit',command = quit_linster)
bt_quit.place(x=350,y=400)

x = IntVar()

def select_ID():
    if (x.get() == 1):
        bt_register.config(state=DISABLED)
    else:
        bt_register.config(state=NORMAL)
        
rbt_admin = Radiobutton(main_page,text="Admin",variable=x,value=1,command=select_ID).place(x=175,y=275)
rbt_stu = Radiobutton(main_page,text="Student",variable=x,value=2,command=select_ID).place(x=325,y=275)

win.mainloop()




# import tkinter

# # -*- coding: utf-8 -*-
# """
# Created on Sun Aug  5 10:34:10 2018
# @author: Administrator
# """
# import tkinter as tk
# import tkinter.messagebox
# import pickle
# #窗口
# window=tk.Tk()
# window.title('欢迎进入学习系统')
# window.geometry('450x300')
# #画布放置图片
# canvas=tk.Canvas(window,height=300,width=500)
# imagefile=tk.PhotoImage(file='Untitled Diagram.drawio.png')
# image=canvas.create_image(0,0,anchor='nw',image=imagefile)
# canvas.pack(side='top')
# #标签 用户名密码
# tk.Label(window,text='用户名:').place(x=100,y=150)
# tk.Label(window,text='密码:').place(x=100,y=190)
# #用户名输入框
# var_usr_name=tk.StringVar()
# entry_usr_name=tk.Entry(window,textvariable=var_usr_name)
# entry_usr_name.place(x=160,y=150)
# #密码输入框
# var_usr_pwd=tk.StringVar()
# entry_usr_pwd=tk.Entry(window,textvariable=var_usr_pwd,show='*')
# entry_usr_pwd.place(x=160,y=190)
 
# #登录函数
# def usr_log_in():
#     #输入框获取用户名密码
#     usr_name=var_usr_name.get()
#     usr_pwd=var_usr_pwd.get()
#     #从本地字典获取用户信息，如果没有则新建本地数据库
#     try:
#         with open('usr_info.pickle','rb') as usr_file:
#             usrs_info=pickle.load(usr_file)
#     except FileNotFoundError:
#         with open('usr_info.pickle','wb') as usr_file:
#             usrs_info={'admin':'admin'}
#             pickle.dump(usrs_info,usr_file)
#     #判断用户名和密码是否匹配
#     if usr_name in usrs_info:
#         if usr_pwd == usrs_info[usr_name]:
#             tk.messagebox.showinfo(title='welcome',
#                                    message='欢迎您：'+usr_name)
#         else:
#             tk.messagebox.showerror(message='密码错误')
#     #用户名密码不能为空
#     elif usr_name=='' or usr_pwd=='' :
#         tk.messagebox.showerror(message='用户名或密码为空')
#     #不在数据库中弹出是否注册的框
#     else:
#         is_signup=tk.messagebox.askyesno('欢迎','您还没有注册，是否现在注册')
#         if is_signup:
#             usr_sign_up()
# #注册函数
# def usr_sign_up():
#     #确认注册时的相应函数
#     def signtowcg():
#         #获取输入框内的内容
#         nn=new_name.get()
#         np=new_pwd.get()
#         npf=new_pwd_confirm.get()
 
#         #本地加载已有用户信息,如果没有则已有用户信息为空
#         try:
#             with open('usr_info.pickle','rb') as usr_file:
#                 exist_usr_info=pickle.load(usr_file)
#         except FileNotFoundError:
#             exist_usr_info={}           
            
#         #检查用户名存在、密码为空、密码前后不一致
#         if nn in exist_usr_info:
#             tk.messagebox.showerror('错误','用户名已存在')
#         elif np =='' or nn=='':
#             tk.messagebox.showerror('错误','用户名或密码为空')
#         elif np !=npf:
#             tk.messagebox.showerror('错误','密码前后不一致')
#         #注册信息没有问题则将用户名密码写入数据库
#         else:
#             exist_usr_info[nn]=np
#             with open('usr_info.pickle','wb') as usr_file:
#                 pickle.dump(exist_usr_info,usr_file)
#             tk.messagebox.showinfo('欢迎','注册成功')
#             #注册成功关闭注册框
#             window_sign_up.destroy()
#     #新建注册界面
#     window_sign_up=tk.Toplevel(window)
#     window_sign_up.geometry('350x200')
#     window_sign_up.title('注册')
#     #用户名变量及标签、输入框
#     new_name=tk.StringVar()
#     tk.Label(window_sign_up,text='用户名：').place(x=10,y=10)
#     tk.Entry(window_sign_up,textvariable=new_name).place(x=150,y=10)
#     #密码变量及标签、输入框
#     new_pwd=tk.StringVar()
#     tk.Label(window_sign_up,text='请输入密码：').place(x=10,y=50)
#     tk.Entry(window_sign_up,textvariable=new_pwd,show='*').place(x=150,y=50)    
#     #重复密码变量及标签、输入框
#     new_pwd_confirm=tk.StringVar()
#     tk.Label(window_sign_up,text='请再次输入密码：').place(x=10,y=90)
#     tk.Entry(window_sign_up,textvariable=new_pwd_confirm,show='*').place(x=150,y=90)    
#     #确认注册按钮及位置
#     bt_confirm_sign_up=tk.Button(window_sign_up,text='确认注册',
#                                  command=signtowcg)
#     bt_confirm_sign_up.place(x=150,y=130)
# #退出的函数
# def usr_sign_quit():
#     window.destroy()
# #登录 注册按钮
# bt_login=tk.Button(window,text='登录',command=usr_log_in)
# bt_login.place(x=140,y=230)
# bt_logup=tk.Button(window,text='注册',command=usr_sign_up)
# bt_logup.place(x=210,y=230)
# bt_logquit=tk.Button(window,text='退出',command=usr_sign_quit)
# bt_logquit.place(x=280,y=230)
# #主循环
# window.mainloop()