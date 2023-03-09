# 使用控制台实现一个登陆系统， 使用类实现
import time
import csv
from tqdm import trange


class Login:
    def __init__(self, data_path):
        """
        Args:
            data_path: 保存账号密码的csv文件位置
        """
        self.data_path = data_path
        self.database = {}
        self.read_data()

    def read_data(self):
        """
        从self.data_path读取csv文件到字典self.database中
        """
        with open(self.data_path, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.database[row['username']] = row['password']

    def append_data(self, new_data_dict):
        """
        追加字典new_data_dict到 self.data_file中
        Args:
            new_data_dict: 需要追加的数据 dict
        """
        with open(self.data_path, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ['username', 'password']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            for k, v in new_data_dict.items():
                writer.writerow({'username': k, 'password': v})

    def register(self):
        """
        注册
        """
        print("正在注册...")
        username = input("请输入用户名：")
        while username in self.database:
            print("用户名已存在，请修改用户名")
            username = input("请输入用户名：")
        password = input("请输入密码：")
        self.database[username] = password
        self.append_data({username: password})
        print("注册成功")

    def login(self):
        """
        登陆
        """
        max_try_time = 3
        try_time = 0

        print("正在登陆...")
        username = input("请输入用户名：")
        password = input("请输入密码：")
        try_time += 1
        if username not in self.database:
            print("用户名不存在，请注册")
            return -1

        while self.database[username] != password and try_time < max_try_time:
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
    login_sys = Login(data_file="1_login.csv")
    choice = 0  # 1.注册 2.登陆 3.退出
    login_res = -9999
    while choice != "3" and login_res != 1:
        print("主页...")
        choice = input("请输入数字选择：\n 1.注册\n 2.登陆\n 3.退出\n")
        if choice == "1":
            login_sys.register()
        elif choice == "2":
            if login_res == -2:
                print("尝试次数过多...\n等待10s...")
                for i in trange(10):
                    time.sleep(1)
            login_res = login_sys.login()
        elif choice == "3":
            print("程序退出")
