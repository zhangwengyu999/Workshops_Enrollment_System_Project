## 1.先到先得原则：管理员可以设置对应事件参与的人数报名上限，每有一名学生选择活动后，人员名单都会减少一个，当人员上限为0时，则不可以再继续报名
## 2.学生选择活动成功和失败的结果都要输出出来给学生
# file = open("administrator.txt")
# readFile=file.readlines()
# print(readFile)
# list = []
# for line in readFile:
#     num = line.strip("\n").split()
#     list.append(num)
#     print(list)
# dictList = dict(list)
# print(dictList)

class administrator():
    def __init__(self, users, passwd):
        self.users =users
        self.passwd = passwd

    def txtToDict():
        file = open("administrator.txt")
        readFile=file.readlines()
        list = []
        for line in readFile:
            num = line.strip("\n").split()
            list.append(num)
        dictList = dict(list)
        return dictList

    def login():
        users = input("Please input users: ")
        dictList = administrator.txtToDict()
        if users in dictList.keys():
            passwd = input("Please input passwd: ")
            if passwd == dictList[users]:
                print("Successfully login! Welcome, administration!")
            else:
                print("Fail to login! Password is not correct!")
        else:
            print("Fail to login! User is not exist!")
    

class student():
    def __init__(self, users, passwd):
        self.users =users
        self.passwd = passwd

    def txtToDict():
        file = open("student.txt")
        readFile=file.readlines()
        list = []
        for line in readFile:
            num = line.strip("\n").split()
            list.append(num)
        dictList = dict(list)
        return dictList

    def login():
        users = input("Please input users: ")
        dictList = student.txtToDict()
        if users in dictList.keys():
            passwd = input("Please input passwd: ")
            if passwd == dictList[users]:
                print("Successfully login! Welcome, student",users,"!")
            else:
                print("Fail to login! Password is not correct!")
        else:
            print("Fail to login! User is not exist!")

def main():
    print("Welcome to use Workshops Enrollment System!".center(100))
    print("Choose your identity, administrator or student?".center(100),"\n","(a/s)".center(100))
    identity = input()
    if identity == "a":
        administrator.login()
    elif identity == "s":
        student.login()

main()