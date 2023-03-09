users = {'admin': '123456', 'user2': 'password2', 'user3': 'password3'}


def login():
    while True:
        username = input("请输入用户名: ")
        password = input("请输入密码: ")
        if username in users and users[username] == password:
            print("登陆成功")
            break
        else:
            print("用户名或密码错误，请重新输入")

def register():
    username = input("请输入用户名：")
    while username in users:
        print("用户名已存在，请修改用户名")
        username = input("请输入用户名：")
    password = input("请输入密码：")
    users[username] = password
    print("注册成功")


if __name__ == '__main__':
    choice = 0
    while choice != "3" :
        choice = input("请输入数字选择：\n 1.注册\n 2.登陆\n 3.退出\n")
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("程序退出")

