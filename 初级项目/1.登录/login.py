# 使用控制台实现一个登陆系统
import time
import csv
from tqdm import trange


def read_data(dict):
    """从文本读取数据到dict"""
    with open(data_file, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict[row['username']] = row['password']


def append_data(new_data_dict):
    """追加字典到data_file中"""
    with open(data_file, 'a', newline='') as csvfile:
        fieldnames = ['username', 'password']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for k, v in new_data_dict.items():
            writer.writerow({'username': k, 'password': v})


def register():
    """注册"""
    print("正在注册...")
    username = input("请输入用户名：")
    while username in database:
        print("用户名已存在，请修改用户名")
        username = input("请输入用户名：")
    password = input("请输入密码：")
    database[username] = password
    append_data({username: password})
    print("注册成功")


def login():
    """
    登陆
    :return: 登陆状态：1：登陆成功； -1 ：用户不存在； -2 尝试次数过多
    """
    max_try_time = 3
    try_time = 0

    print("正在登陆...")
    username = input("请输入用户名：")
    password = input("请输入密码：")
    try_time += 1
    if username not in database:
        print("用户名不存在，请注册")
        return -1

    while database[username] != password and try_time < max_try_time:
        print("密码错误...请重试...")
        password = input("请输入密码：")
        try_time += 1
    if try_time == max_try_time:
        print("尝试错误过多，稍后重试")
        return -2
    else:
        print("登陆成功...")

        return 1


if __name__ == '__main__':
    data_file = "1_login.csv"
    database = {}
    read_data(database)

    choice = 0
    login_res = -9999
    while choice != "3" and login_res != 1:
        print("主页...")
        choice = input("请输入数字选择：\n 1.注册\n 2.登陆\n 3.退出\n")
        if choice == "1":
            register()
        elif choice == "2":
            if login_res == -2:
                print("尝试次数过多...\n等待10s...")
                for i in trange(10):
                    time.sleep(1)
            login_res = login()
        elif choice == "3":
            print("程序退出")
