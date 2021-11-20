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

from os import write

class searchEngine():
    
    def getWorkshopDataDict():
        file = open('workshop.txt',mode='r')
        readLine = file.readlines()
        outList = []
        
        for i in readLine:
            lineList = i.strip("\n").split(":")
            lineList[1] = lineList[1].split(" ")
            outList.append(lineList)
        outDict = dict(outList)
        file.close()
        return outDict
    
    def findBywID(inwID):
        """
        function to find a workshop according to its ID, and print out

        parameter:
            - inwID: a String of the workshop's ID
        """
        
        outDict = searchEngine.getWorkshopDataDict()
        
        if (inwID not in outDict):
            print("NO workshop with ID: "+inwID)
        else:
            print("--------Found:--------s\n----------------------")
            print("workshop ID: "+inwID
                      +"\nTitle:       "+outDict[inwID][0]
                      +"\nLocation:    "+outDict[inwID][1]
                      +"\nDate:        "+outDict[inwID][2]
                      +"\nTime:        "+outDict[inwID][3]
                      +"\nQuotas:      "+outDict[inwID][4]
                      +"\nRemaining:   "+outDict[inwID][5]
                      +"\n----------------------")
    
    def findByName(inName):
        """
        function to find workshops according to thier name , and print out

        parameter:
            - inName: a String of the workshop's name
        """
        
        outDict = searchEngine.getWorkshopDataDict()
        
        flag = False
        print("--------Found:--------\n----------------------")
        for d in outDict:
            if (outDict[d][0] == inName):
                flag = True
                print("workshop ID: "+d
                      +"\nTitle:       "+outDict[d][0]
                      +"\nLocation:    "+outDict[d][1]
                      +"\nDate:        "+outDict[d][2]
                      +"\nTime:        "+outDict[d][3]
                      +"\nQuotas:      "+outDict[d][4]
                      +"\nRemaining:   "+outDict[d][5]
                      +"\n----------------------")
        if (flag == False):
            print("NOT FOUND!")
            
    def findByLocation(inLocatin):
        """
        function to find workshops according to thier location , and print out

        parameter:
            - inName: a String of the workshop's location
        """
        
        outDict = searchEngine.getWorkshopDataDict()
        
        flag = False
        print("--------Found:--------\n----------------------")
        for d in outDict:
            if (outDict[d][1] == inLocatin):
                flag = True
                print("workshop ID: "+d
                      +"\nTitle:       "+outDict[d][0]
                      +"\nLocation:    "+outDict[d][1]
                      +"\nDate:        "+outDict[d][2]
                      +"\nTime:        "+outDict[d][3]
                      +"\nQuotas:      "+outDict[d][4]
                      +"\nRemaining:   "+outDict[d][5]
                      +"\n----------------------")
        if (flag == False):
            print("NOT FOUND!")
            
    def findByDate(inD):
        """
        function to find workshops according to thier date , and print out

        parameter:
            - inName: a String of the workshop's date
        """

        outDict = searchEngine.getWorkshopDataDict()
        
        flag = False
        print("--------Found:--------\n----------------------")
        for d in outDict:
            if (outDict[d][2] == inD):
                flag = True
                print("workshop ID: "+d
                      +"\nTitle:       "+outDict[d][0]
                      +"\nLocation:    "+outDict[d][1]
                      +"\nDate:        "+outDict[d][2]
                      +"\nTime:        "+outDict[d][3]
                      +"\nQuotas:      "+outDict[d][4]
                      +"\nRemaining:   "+outDict[d][5]
                      +"\n----------------------")
        if (flag == False):
            print("NOT FOUND!")
            
    def findByTime(inT):
        """
        function to find workshops according to thier time , and print out

        parameter:
            - inName: a String of the workshop's time
        """

        outDict = searchEngine.getWorkshopDataDict()
        
        flag = False
        print("--------Found:--------\n----------------------")
        for d in outDict:
            if (outDict[d][3] == inT):
                flag = True
                print("workshop ID: "+d
                      +"\nTitle:       "+outDict[d][0]
                      +"\nLocation:    "+outDict[d][1]
                      +"\nDate:        "+outDict[d][2]
                      +"\nTime:        "+outDict[d][3]
                      +"\nQuotas:      "+outDict[d][4]
                      +"\nRemaining:   "+outDict[d][5]
                      +"\n----------------------")
        if (flag == False):
            print("NOT FOUND!")
                
    def findByQuota(inQuota):
        """
        function to find workshops according to thier quotas , and print out

        parameter:
            - inName: a String of the workshop's quotas
        """
        
        outDict = searchEngine.getWorkshopDataDict()
        
        flag = False
        print("--------Found:--------\n----------------------")
        for d in outDict:
            if (outDict[d][3] == inQuota):
                flag = True
                print("workshop ID: "+d
                      +"\nTitle:       "+outDict[d][0]
                      +"\nLocation:    "+outDict[d][1]
                      +"\nDate:        "+outDict[d][2]
                      +"\nTime:        "+outDict[d][3]
                      +"\nQuotas:      "+outDict[d][4]
                      +"\nRemaining:   "+outDict[d][5]
                      +"\n----------------------")
        if (flag == False):
            print("NOT FOUND!")
            
    def findByRemaining(inRemaining):
        """
        function to find workshops according to thier remaining quotas , and print out

        parameter:
            - inName: a String of the workshop's remaining quotas
        """
        
        outDict = searchEngine.getWorkshopDataDict()
        
        flag = False
        print("--------Found:--------\n----------------------")
        for d in outDict:
            if (outDict[d][4] == inRemaining):
                flag = True
                print("workshop ID: "+d
                      +"\nTitle:       "+outDict[d][0]
                      +"\nLocation:    "+outDict[d][1]
                      +"\nDate:        "+outDict[d][2]
                      +"\nTime:        "+outDict[d][3]
                      +"\nQuotas:      "+outDict[d][4]
                      +"\nRemaining:   "+outDict[d][5]
                      +"\n----------------------")
        if (flag == False):
            print("NOT FOUND!")

class administrator():
    
    def getWorkshopDataDict():
        file = open('workshop.txt',mode='r')
        readLine = file.readlines()
        outList = []
        
        for i in readLine:
            lineList = i.strip("\n").split(":")
            lineList[1] = lineList[1].split(" ")
            outList.append(lineList)
        outDict = dict(outList)
        file.close()
        return outDict
    
    workshopID = len(getWorkshopDataDict())
    
    def inID():
        administrator.workshopID +=1
        return f'{administrator.workshopID:0>6d}'
    
    def getNowID():
        return f'{administrator.workshopID:0>6d}'
    
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
                    administrator.adminInterface() # enter the main interface
                    main()
                else:
                    print("Password is not correct! Please input the correct password again! You still have",2-times,"times to try")
                    times+=1
            else:
                print("You have already input password for three times! Please input from the start")
        else:
            print("The user is not exist!")
            
    

    def writeWorkshopData(inDict):
        file = open('workshop.txt',mode='w+')
        for d in inDict:
            writeStr = d+":"+inDict[d][0]+" "+inDict[d][1]+" "+inDict[d][2]+" "+inDict[d][3]+" "+inDict[d][4]+" "+inDict[d][5]+"\n"
            file.write(writeStr)
        file.close()

    def addWs(infoString):
        wID = administrator.inID()
        
        outDict = administrator.getWorkshopDataDict()
        outDict[wID] = infoString
        
        administrator.writeWorkshopData(outDict)
        
    def updateName(wID,inName):
        """
        function to update a workshop's name by the adminnistator

        parameter:
            - wID: a String of the number of workshop's ID
            - inName: the name to update to that workshop
        """
        outDict = administrator.getWorkshopDataDict()

        if (wID in outDict):
            outDict[wID][0] = inName
        else:
            print("Workshop ID:{0} not found! Please try again!".format(wID))
            
        administrator.writeWorkshopData(outDict)

    def updateLocation(wID,inLocation):
        """
        function to update a workshop's location by the adminnistator

        parameter:
            - wID: a String of the number of workshop's ID
            - inLocation: the location to update to that workshop
        """
        
        outDict = administrator.getWorkshopDataDict()

        if (wID in outDict):
            outDict[wID][1] = inLocation
        else:
            print("Workshop ID:{0} not found! Please try again!".format(wID))

        administrator.writeWorkshopData(outDict)

    def updateDate(wID,inDate):
        """
        function to update a workshop's date by the adminnistator

        parameter:
            - wID: a String of the number of workshop's ID
            - inTime: the date to update to that workshop
        """
        outDict = administrator.getWorkshopDataDict()
        
        if (wID in outDict):
            outDict[wID][2] = inDate
        else:
            print("Workshop ID:{0} not found! Please try again!".format(wID))

        administrator.writeWorkshopData(outDict)
        
    def updateTime(wID,inTime):
        """
        function to update a workshop's time by the adminnistator

        parameter:
            - wID: a String of the number of workshop's ID
            - inTime: the time to update to that workshop
        """
        outDict = administrator.getWorkshopDataDict()
        
        if (wID in outDict):
            outDict[wID][3] = inTime
        else:
            print("Workshop ID:{0} not found! Please try again!".format(wID))

        administrator.writeWorkshopData(outDict)
        
    def updateQuota(wID,inQuota):
        """
        function to update a workshop's quotas by the adminnistator

        parameter:
            - wID: a String of the number of workshop's ID
            - inQuota: the quotas to update to taht workshop
        """
        outDict = administrator.getWorkshopDataDict()
        

        if (wID in outDict):
            enrolledNum = eval(outDict[wID][4]) - eval(outDict[wID][5])
            outDict[wID][4] = inQuota
            if (eval(inQuota)<enrolledNum):
                outDict[wID][5] = "0"
            else:
                outDict[wID][5] = (str)(eval(outDict[wID][4]) - enrolledNum)
        else:
            print("Workshop ID:{0} not found! Please try again!".format(wID))

        administrator.writeWorkshopData(outDict)
        
    def updateRemaining(wID,inRemaining):
        """
        function to update a workshop's Remaining quotas by the adminnistator

        parameter:
            - wID: a String of the number of workshop's ID
            - inRemaining: the remianing quotas to update to taht workshop
        """
        outDict = administrator.getWorkshopDataDict()

        if (wID in outDict):
            if (eval(inRemaining)>eval(outDict[wID][4])):
                print("Illegal input! Remaining CAN NOT be greater than quota!")
            else:
                outDict[wID][5] = inRemaining
        else:
            print("Workshop ID:{0} not found! Please try again!".format(wID))

        administrator.writeWorkshopData(outDict)

        
    def adminInterface():
        print("Please select function: (a)Add a workshop; (u)Update a workshop; (f)Find a workshop; (q)Quit".center(100),"\n","(a/u/f/q)".center(100,"*"))
        choose = input().lower()
        
        if (choose == "a"):
            print("New workshop creation")
            print("Please enter Workshop Name:")
            name = input()
            
            print("Please enter Workshop Location:")
            location = input()
            
            print("Please enter Workshop Date:")
            date = input()
            
            print("Please enter Workshop Time:")
            time = input()
            
            print("Please enter Workshop Quota:")
            quota = input()
            
            remainder = quota
            
            infoList = [name,location,date,time,quota,remainder]
        
            administrator.addWs(infoList)
            print("Create workshop successfully!")
            
            administrator.adminInterface()
            
        elif(choose == "u"):
            print("Update workshop information:")
            print("Here is all the event: \n")
            student.listAll()
            eventChoose = input("Enter the ID of event for updating:")
            print("Update based on (l):Location; (n):Name; (d)Date; (t)Time; (quo)Quota; (r)Remaining".center(100),"\n","(l/n/d/t/quo/r)".center(100,"*"))
            choose = input().lower()
            print("Please choose the information for updating: ")
            data = input().lower()
            if(choose == "d"):
                administrator.updateDate(eventChoose,data)

            elif(choose == "t"):
                administrator.updateTime(eventChoose,data)

            elif(choose == "l"):
                administrator.updateLocation(eventChoose,data)

            elif(choose == "n"):
                administrator.updateName(eventChoose,data)

            elif(choose == "quo"):
                administrator.updateQuota(eventChoose,data)
                
            elif(choose == "r"):
                administrator.updateRemaining(eventChoose,data)
                
            administrator.adminInterface()

        elif(choose == "f"):
            print("Search workshop information:")
            print("Search based on (i)workshopID; (n):Name; (l)Location; (d)Date; (t)Time; (quo)Quota; (r)Remaining;  else back to main page".center(100),"\n","(i/n/d/t/quo/r)".center(100,"*"))
            choose = input().lower()
            print("Please enter the data to search:".center(100))
            data = input()
            if(choose == "i"):
                searchEngine.findBywID(data)
            elif(choose == "n"):
                searchEngine.findByName(data)
            elif(choose == "d"):
                searchEngine.findByDate(data)
            elif(choose == "t"):
                searchEngine.findByTime(data)
            elif(choose == "quo"):
                searchEngine.findByQuota(data)
            elif(choose == "r"):
                searchEngine.findByRemaining(data)
            elif(choose == "l"):
                searchEngine.findByLocation(data)
            else:
                print("Empty or Illegal input, back to main page!")
            
            administrator.adminInterface()
                
        elif(choose == "q"):
            return 0
        else:
            print("Illegal input, please try again!")
            administrator.adminInterface()
    

                    
        

class student():
    users = ""
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

    def setUsers():
        student.users = input("Please input users: ")
        return student.users

    def getUsers():
        return student.users

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
            users = student.setUsers()
            if student.isContainUsers(users):
                for times2 in range(3):
                    passwd = student.getPasswd()
                    if student.isCorrectPasswd(users,passwd)==True:
                        print("Successfully login! Welcome, student {0}!".format(users))
                        student.studentInterface()
                        main()
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

    def isfindBywIDforEroll(sID,inwID):
        """
        function to find whether the workshop is erolled or not 
        parameter
        - sID: the student ID
        - inwID: the input workshop ID
        """
        file = open(sID +".txt",mode='r')
        readLine = file.readlines()
        #print(readLine)
        outList = []
        
        if readLine == ['\n']:
            return False
        else:
            return student.isfindBywIDforCancel(sID,inwID)

    def isfindBywIDforCancel(sID,inwID):
        """
        function to find whether the workshop is erolled or not 

        parameter
            - sID: the student ID
            - inwID: the input workshop ID
        """
        file = open(sID +".txt",mode='r')
        readLine = file.readlines()
        outList = []
        
        for i in readLine:
            lineList = i.strip("\n").split(":")
            lineList[1] = lineList[1].split(" ")
            outList.append(lineList)
        outDict = dict(outList)
        file.close()
        
        if (inwID in outDict):
            return True
        else:
            return False


    def eroll(sID,wID):
        """
        function to ecroll workshop by student

        parameter:
            - sID: the student ID
            - wID: the workshop ID which the student want to enroll
        """
        workshopRemainder = open("workshop.txt")
        readLine = workshopRemainder.readlines()
        outList = []
        
        for i in readLine:
            lineList = i.strip("\n").split(":")
            lineList[1] = lineList[1].split(" ")
            outList.append(lineList)
        outDict = dict(outList)
        workshopRemainder.close()

        if student.isfindBywIDforEroll(sID,wID) == False:    
            for d in outDict:
                #print(d)
                if d == wID:
                    if int(outDict[d][5]) <= 0:
                        print("Sorry you can not eroll the workshop! No remaining quota!")
                    else: 
                        outDict[d][5] = str(int(outDict[d][5]) - 1)
                        file = open("workshop.txt",mode="w+")
                        erollWorkshop = open(sID+".txt","a+")
                        for d in outDict:
                            writeStr = d+":"+outDict[d][0]+" "+outDict[d][1]+" "+outDict[d][2]+" "+outDict[d][3]+" "+outDict[d][4]+" "+outDict[d][5]+"\n"
                            file.write(writeStr)
                            if d == wID:
                                erollWorkshop.write(writeStr)
                        file.close()                
                        erollWorkshop.close()
                        print("Successful erollment!")
        else:
            print("Sorry you can not eroll this workshop more than once!")

    def cancel(sID,wID):
        """
        function to cancle workshop which has been erolled by student

        parameter:
            - sID: the student ID
            - wID: the workshop ID which the student want to cancel
        """
        workshopRemainder = open("workshop.txt")
        readLine = workshopRemainder.readlines()
        outList = []

        for i in readLine:
            lineList = i.strip("\n").split(":")
            lineList[1] = lineList[1].split(" ")
            outList.append(lineList)
        outDict = dict(outList)
        workshopRemainder.close()

        workshopBysID = open(sID + ".txt")
        readLine = workshopBysID.readlines()
        outList = []

        for i in readLine:
            lineList = i.strip("\n").split(":")
            lineList[1] = lineList[1].split(" ")
            outList.append(lineList)
        outDictsID = dict(outList)
        workshopBysID.close()

        if student.isfindBywIDforCancel(sID,wID) == True:
            for d in outDict:
                #print(d)
                if d == wID: 
                    outDict[d][5] = str(int(outDict[d][5]) + 1)
                    file = open("workshop.txt",mode="w+")
                    cancelWorkshop = open(sID+".txt","w+")
                    for d in outDict:
                        writeStr = d+":"+outDict[d][0]+" "+outDict[d][1]+" "+outDict[d][2]+" "+outDict[d][3]+" "+outDict[d][4]+" "+outDict[d][5]+"\n"
                        file.write(writeStr)
                    for i in outDictsID:
                        if i != wID:
                            writeStr = i+":"+outDict[i][0]+" "+outDict[i][1]+" "+outDict[i][2]+" "+outDict[i][3]+" "+outDict[i][4]+" "+outDict[i][5]+"\n"
                            cancelWorkshop.write(writeStr)
                    file.close()                
                    cancelWorkshop.close()
                    print("Successful cancllation!")

    def listAll():
        """
        function to print all workshops to studnets
        """
        file = open('workshop.txt',mode='r')
        readLine = file.readlines()
        outList = []
        student.listEnrolledWs("workshop")
        
    def listEnrolledWs(sID):
        """
        function to list all workshops enrolled by a studnet

        parameter:
            - sID: a String of the number of student's ID
        """
        sIDfile = sID+".txt"
        file = open(sIDfile,mode='r')
        readLine = file.readlines()
        outList = []
        
        for i in readLine:
            lineList = i.strip("\n").split(":")
            lineList[1] = lineList[1].split(" ")
            outList.append(lineList)
        outDict = dict(outList)
        file.close()
        for d in outDict:
            print("workshop ID: "+d
                      +"\nTitle:       "+outDict[d][0]
                      +"\nLocation:    "+outDict[d][1]
                      +"\nDate:        "+outDict[d][2]
                      +"\nTime:        "+outDict[d][3]
                      +"\nQuotas:      "+outDict[d][4]
                      +"\nRemaining:   "+outDict[d][5]
                      +"\n----------------------")

    def getWID():
        """""
        function to get workshop ID
        """""
        return 0
            
    def studentInterface():
    # enrollWorkshop
    # cancelWorkshop
    # listAll
    # listEnrolledWorkshop
        print("Please select function: (e)Enroll a workshop; (c)Cancel a workshop; (la)ListAll; (l)list an enrolled workshop; (q)Quit".center(100),"\n","(e/c/la/l/q)".center(100,"*"))
        choose = input().lower()
        if(choose == "e"):
            wID = input("Please input the ID of which workshop you want to eroll:")
            student.eroll(student.getUsers(),wID)
        elif(choose == "c"):
            wID = input("Please input the ID of which workshop you want to cancel:")
            student.cancel(student.getUsers(),wID)
        elif(choose == "la"):
            print("---All workshops---\n----------------------")
            student.listAll()
        elif(choose == "l"):
            print("---Your Enrollments---\n----------------------")
            student.listEnrolledWs(student.getUsers())
        elif(choose == "q"):
            return 0
        else:
            print("Empty or illegal input, please try again!")
        student.studentInterface()
    
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
        users = student.setUsers()
        if student.isContainUsers(users):
            print("The users have already register before, do you want to back to login or continue registering?".center(100),"\n","(l/r)".center(100,"*"))
            choose = input().lower()
            if choose=="l":
                student.login()
            elif choose =="r":
                users = student.setUsers()
                student.strToTxt(users)
        else:
            student.strToTxt(users)

def main():
    print("Welcome to use Workshops Enrollment System!".center(100))
    print("Choose your identity, administrator or student? q for quit".center(100),"\n","(a/s/q)".center(100,"*"))
    identity = input()
    if identity == "a":
        administrator.login()
    elif identity == "s":
        print("Do you want to login or register for a new account? q for quit".center(100),"\n","(l/r/q)".center(100,"*"))
        choose = input().lower()
        if choose =="l":
            student.login()
        elif choose =="r":
            student.addusers()
        elif choose =="q":
            exit()
        else:
            print("Illegal input! Try again!")
            main()
    elif identity == "q":
        exit()
    else:
        print("Illegal input! Try again!")
        main()
main()
