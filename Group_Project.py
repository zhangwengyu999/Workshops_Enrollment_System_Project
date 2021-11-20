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

    def getUsers():
        users = input("Please input users: ")
        return users

    def getPasswd():
        passwd = input("Please input password: ")
        return passwd

    def isContainUsers(users):
            dictList = administrator.txtToDict()
            if users in dictList.keys():
                return True
            else:
                return False

    def isCorrectPasswd(users,passwd):
        dictList = administrator.txtToDict()
        if passwd == dictList[users]:
            return True
        else:
            return False

    def login():
        users = administrator.getUsers()
        if administrator.isContainUsers(users):
            for times in range(3):
                passwd = administrator.getPasswd()
                if administrator.isCorrectPasswd(users,passwd)==True:
                    print("Successfully login! Welcome, administration!")
                    break
                else:
                    print("Password is not correct! Please input the correct password again! You still have",2-times,"times to try")
                    times+=1
            else:
                print("You have already input password for three times! Please input from the start")
        else:
            print("users is not exist!")
                    
        

class student():

    # def usersJudge():
    #     users = student.login().users
    #     dictList = student.login().users
    #     if users in dictList.keys():
    #         return True
    #     else:
    #         return False

    # def passwdJudge():
    #     users = student.login().users
    #     dictList = student.login().users
    #     passwd = input("Please input your password: ")
    #     if passwd == dictList[users]:
    #         return True
    #     else:
    #         return False


    # def alreadyContainUsers():
    #     users = input("Please input your users name:")
    #     dictList = student.txtToDict()
    #     if users not in dictList.keys():
    #         print("This users haven't been register before".center(100))
    #         print("Do you want to register?".center(100),"\n","(y/n)".center(100,"*"))
    #         yn = input().lower()
    #         if yn=="y":
    #                 student.addusers()
    #         elif yn=="n":
    #             print("Thanks for your using!")
            
    # def isContainUsers():
    #     users = student.addusers().users
    #     dictList = student.txtToDict()
    #     if users in dictList.keys():
    #         return True
    #     else:
    #         return False

     # def login():
    #     users = input("Please input your users name:")
    #     passwd = input("Please input your password: ")
    #     dictList = student.txtToDict()
    #     if student.usersJudge()==True:
    #         for times in range(0,3):
    #             if student.passwdJudge() is False:
    #                 if times<=2:
    #                     print("Password is not correct! Please input again!")
    #                     times+=1
    #                 else:
    #                     print("Already try three times! You have to start from begin!")
    #             else:
    #                 print("Successfully login! Welcome, student",users,"!")
                
    #     else:
    #         print("Fail to login! User is not exist!")

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

    def getUsers():
        users = input("Please input users: ")
        return users

    def getPasswd():
        passwd = input("Please input password: ")
        return passwd

    def isContainUsers(users):
            dictList = student.txtToDict()
            if users in dictList.keys():
                return True
            else:
                return False

    def isCorrectPasswd(users,passwd):
        dictList = student.txtToDict()
        if passwd == dictList[users]:
            return True
        else:
            return False

    def login():
        for times in range(100):
            users = student.getUsers()
            if student.isContainUsers(users):
                for times2 in range(3):
                    passwd = student.getPasswd()
                    if student.isCorrectPasswd(users,passwd)==True:
                        print("Successfully login! Welcome, administration!")
                        return 0
                    else:
                        print("Password is not correct! Please input the correct password again! You have",2-times2,"times to try")
                        times2+=1
                else:
                    print("You have already input password for three times! Please input from the start")
                    times = 0
            else:
                times+=1
                choose = input("Users is not correct or not exist! if want to create new account, please input ‘q'; or input other to back the login!").lower()
                if choose =="q":
                    student.addusers()
                    break
                else:
                    continue
        else:
            print("")


    def strToTxt(users):
        # users = student.getUsers()
        if student.isContainUsers(users)==False:   
            passwd = student.getPasswd()
            str = "\n"+users+" "+passwd
            with open('student.txt','a')as file:
                file.write(str)
            print("Seccessfully register a new account as student!")
        else:
            print("Unseccessfully register a new account as student because already has the same users!")
            student.addusers()

            
    def addusers():
        users = student.getUsers()
        if student.isContainUsers(users):
            print("The users have already register before, do you want to back to login or continue registering?".center(100),"\n","(l/r)".center(100,"*"))
            choose = input().lower()
            if choose=="l":
                student.login()
            elif choose =="r":
                users = student.getUsers()
                student.strToTxt(users)
        else:
            student.strToTxt(users)

def main():
    print("Welcome to use Workshops Enrollment System!".center(100))
    print("Choose your identity, administrator or student?".center(100),"\n","(a/s)".center(100,"*"))
    identity = input()
    if identity == "a":
        administrator.login()                 
    elif identity == "s":
        print("Do you want to login or register for a new account?".center(100),"\n","(l/r)".center(100,"*"))
        choose = input().lower()
        if choose =="l":
            student.login()
        elif choose =="r":
            student.addusers()

main()
