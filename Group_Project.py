from os import write
import os

class searchEngine():
    """a search engine class to implement search
    """
    isStudent = False
    
    def setStudnet():
        searchEngine.isStudent = True
    def setAdmin():
        searchEngine.isStudent = False
    
    def getWorkshopDataDict():
        """a function to get a dictionary from workshop text file

        Returns:
            dictionary: a dictionary from workshop text file (key: wID; value:[name,location,date,time,quota,remaining])

        """
    
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
            if (searchEngine.isStudent):
                print("workshop ID: "+inwID
                        +"\nTitle:       "+outDict[inwID][0]
                        +"\nLocation:    "+outDict[inwID][1]
                        +"\nDate:        "+outDict[inwID][2]
                        +"\nTime:        "+outDict[inwID][3]
                        +"\nRemaining:   "+outDict[inwID][5]
                        +"\n----------------------")
            else:
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
                if (searchEngine.isStudent):
                    print("workshop ID: "+d
                        +"\nTitle:       "+outDict[d][0]
                        +"\nLocation:    "+outDict[d][1]
                        +"\nDate:        "+outDict[d][2]
                        +"\nTime:        "+outDict[d][3]
                        +"\nRemaining:   "+outDict[d][5]
                        +"\n----------------------")
                else:
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
                if (searchEngine.isStudent):
                    print("workshop ID: "+d
                        +"\nTitle:       "+outDict[d][0]
                        +"\nLocation:    "+outDict[d][1]
                        +"\nDate:        "+outDict[d][2]
                        +"\nTime:        "+outDict[d][3]
                        +"\nRemaining:   "+outDict[d][5]
                        +"\n----------------------")
                else:
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
                if (searchEngine.isStudent):
                    print("workshop ID: "+d
                        +"\nTitle:       "+outDict[d][0]
                        +"\nLocation:    "+outDict[d][1]
                        +"\nDate:        "+outDict[d][2]
                        +"\nTime:        "+outDict[d][3]
                        +"\nRemaining:   "+outDict[d][5]
                        +"\n----------------------")
                else:
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
                if (searchEngine.isStudent):
                    print("workshop ID: "+d
                        +"\nTitle:       "+outDict[d][0]
                        +"\nLocation:    "+outDict[d][1]
                        +"\nDate:        "+outDict[d][2]
                        +"\nTime:        "+outDict[d][3]
                        +"\nRemaining:   "+outDict[d][5]
                        +"\n----------------------")
                else:
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
            if (outDict[d][4] == inQuota):
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
            if (outDict[d][5] == inRemaining):
                flag = True
                if (searchEngine.isStudent):
                    print("workshop ID: "+d
                        +"\nTitle:       "+outDict[d][0]
                        +"\nLocation:    "+outDict[d][1]
                        +"\nDate:        "+outDict[d][2]
                        +"\nTime:        "+outDict[d][3]
                        +"\nRemaining:   "+outDict[d][5]
                        +"\n----------------------")
                else:
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
    """a class for administrator implementation
    """

    users = ""
    passwd = ""
    workshopID = 0
    
    def __init__(self, users, passwd):
        """
        constructor for administrator class
        """
        self.users =users
        self.passwd = passwd
        
    #-------------------functions for administractor login -------------------
    def setUsers():
        """
        function to get user ID
        return: 
            - users as user ID
        """
        users = input("Please input users: ")
        return users

    def setPasswd():
        """
        function to get ueser password
        retunrn: passwd
        """
        passwd = input("Please input password: ")
        return passwd

    def isContainUsers(users):
        """
        function to identify whether the user is contained
        retrun:
            - True for contained 
            - False for not
        """
        dictList = administrator.txtToDict()
        if users in dictList.keys():
            return True
        else:
            return False

    def isCorrectPasswd(users,passwd):
        """
        function to identify whether the password is correct
        retrun:
            - True for correct 
            - False for wrong
        """
        dictList = administrator.txtToDict()
        if passwd == dictList[users]:
            return True
        else:
            return False 
        
    #-------------------functions for workshop information process by administractor-------------------
    
    def getWorkshopDataDict():
        """
        function to get the workshop dictionary
        return: outDitc
        """

        file = open('workshop.txt',mode='a+')
        readLine = file.readlines()
        outList = []

        for i in readLine:
            lineList = i.strip("\n").split(":")
            lineList[1] = lineList[1].split(" ")
            outList.append(lineList)
        outDict = dict(outList)
        file.close()
        return outDict
    
    # get the max workshop ID
    inDict = getWorkshopDataDict()
    maxID = 0
    for i in inDict:
        inNum = eval(i.strip("0"))
        if (inNum > maxID):
            maxID = inNum
    workshopID = maxID
    
    def inID():
        """
        function to generate the workshop ID
        returm: workshop ID
        """
        administrator.workshopID +=1
        return f'{administrator.workshopID:0>6d}'
    
    def getNowID():
        """
        return the current workshop ID
        """
        return f'{administrator.workshopID:0>6d}'
    
    
    def txtToDict():
        """
        function to convert txt file to dictionary
        return: dictList
        """
        file = open("administrator.txt")
        readFile=file.readlines()
        list = []
        for line in readFile:
            num = line.strip("\n").split()
            list.append(num)
        dictList = dict(list)
        return dictList
    
    def writeWorkshopData(inDict):
        """a function to write a dictionary to a txt file

        Args:
            inDict (String): a dictionary to be worte into the txt file
        """
        file = open('workshop.txt',mode='w+')
        for d in inDict:
            writeStr = d+":"+inDict[d][0]+" "+inDict[d][1]+" "+inDict[d][2]+" "+inDict[d][3]+" "+inDict[d][4]+" "+inDict[d][5]+"\n"
            file.write(writeStr)
        file.close()

    def addWs(infoString):
        """a function to add a workshop into the storage 

        Args:
            infoString ([type]): [description]
        """
        wID = administrator.inID()
        
        outDict = administrator.getWorkshopDataDict()
        outDict[wID] = infoString
        
        administrator.writeWorkshopData(outDict)
    
    def updateWorkShop(wID,inData,Index):
        outDict = administrator.getWorkshopDataDict()

        if (wID in outDict):
            outDict[wID][eval(Index)] = inData
        else:
            print("Workshop ID:{0} not found! Please try again!".format(wID))
            
        administrator.writeWorkshopData(outDict)
        
    def updateName(wID,inName):
        """
        function to update a workshop's name by the adminnistator

        parameter:
            - wID: a String of the number of workshop's ID
            - inName: the name to update to that workshop
        """
        administrator.updateWorkShop(wID,inName,0)

    def updateLocation(wID,inLocation):
        """
        function to update a workshop's location by the adminnistator

        parameter:
            - wID: a String of the number of workshop's ID
            - inLocation: the location to update to that workshop
        """
        administrator.updateWorkShop(wID,inLocation,1)

    def updateDate(wID,inDate):
        """
        function to update a workshop's date by the adminnistator

        parameter:
            - wID: a String of the number of workshop's ID
            - inTime: the date to update to that workshop
        """
        administrator.updateWorkShop(wID,inDate,2)
        
    def updateTime(wID,inTime):
        """
        function to update a workshop's time by the adminnistator

        parameter:
            - wID: a String of the number of workshop's ID
            - inTime: the time to update to that workshop
        """
        administrator.updateWorkShop(wID,inTime,3)
        
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

    def listAll():
        """
        function to print all workshops to admin
        """
        file = open('workshop.txt',mode='r')
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
                      +"\nQuota:       "+outDict[d][4]
                      +"\nRemaining:   "+outDict[d][5]
                      +"\n----------------------")
    
    #-------------------login interface for administractor-------------------
    def login():
        """
        login function for administrator
        """
        inUsers = administrator.setUsers()
        if administrator.isContainUsers(inUsers):
            for times in range(3):
                inPasswd = administrator.setPasswd()
                if administrator.isCorrectPasswd(inUsers,inPasswd)==True:
                    print("Successfully login! Welcome, administration!")
                    inAdmin = administrator(inUsers,inPasswd)
                    inAdmin.adminInterface() # enter the main interface
                    main()
                else:
                    print("Password is not correct! Please input the correct password again! You still have",2-times,"times to try")
                    times+=1
            else:
                print("You have already input password for three times! Please input from the start")
        else:
            print("The user is not exist!")    
      
    #-------------------function interface for administractor-------------------
    def adminInterface(self):
        """an interface for administrator function including Add a workshop; Update a workshop; Search in workshops;

        Returns:
            int: 0 to quit
        """
        print("Please select function: (a)Add a workshop; (u)Update a workshop; (S)Search in workshops; (q)Quit".center(100),"\n","(a/u/s/q)".center(100,"*"))
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
            
            self.adminInterface()
            
        elif(choose == "u"):
            print("Update workshop information:")
            print("Here is all the event: \n")
            administrator.listAll()
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
                
            self.adminInterface()

        elif(choose == "s"):
            print("Search workshop information:")
            print("Search based on (i)workshopID; (n):Name; (l)Location; (d)Date; (t)Time; (quo)Quota; (r)Remaining;  else to back".center(100),"\n","(i/n/d/t/quo/r)".center(100,"*"))
            choose = input().lower()
            print("Please enter the data to search:".center(100))
            data = input()
            searchEngine.setAdmin()
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
                print("Empty or Illegal input, back to the previous page!")
            
            self.adminInterface()
                
        elif(choose == "q"):
            main()
            return 0
        else:
            print("Illegal input, please try again!")
            self.adminInterface()
    
    
class student():
    users = ""
    passwd = ""
    def __init__(self, users, passwd):
        """
        constructor for student class
        """
        self.users = users
        self.passwd = passwd
        
    #-------------------functions for student login -------------------
    def setUsers():
        """
        function to create user ID
        return:
            - users as user ID
        """
        users = input("Please input users: ")
        return users

    def getUsers(self):
        """
        function to get current user ID
        """
        return self.users

    def setPasswd():
        """
        function to set password
        return: passwd
        """
        passwd = input("Please input password: ")
        return passwd

    def isContainUsers(users):
        """
        function to identify whether the user is contained
        return: 
            - True for contained
            - False for not
        """
        dictList = student.txtToDict()
        if users in dictList.keys():
            return True
        else:
            return False

    def isCorrectPasswd(users,passwd):
        """
        function to identify whether the password is correct
        retrun:
            - True for correct 
            - False for wrong
        """
        dictList = student.txtToDict()
        if passwd == dictList[users]:
            return True
        else:
            return False

    #-------------------functions for student enrolled workshop information process by student-------------------
    def txtToDict():
        """
        function to convert a dictionary from txt file
        return:
            - dictList as the out dictionary
        """
        file = open("student.txt",mode = "r")
        readFile=file.readlines()
        list = []
        for line in readFile:
            num = line.strip("\n").split()
            list.append(num)
        dictList = dict(list)
        return dictList
    
    def getWorkshopDataDict():
        """
        function to get the workshop dictionary
        return: outDitc
        """

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
        
    def getEnrolledDataDict(self,inName):
        """
        function to get studnet's workshop dictionary
        return: outDitc
        """
        workshopBysID = open(inName + ".txt")
        readLine = workshopBysID.readlines()
        outList = []

        for i in readLine:
            lineList = i.strip("\n").split(":")
            lineList[1] = lineList[1].split(" ")
            outList.append(lineList)
        outDictsID = dict(outList)
        workshopBysID.close()
        return outDictsID
    
    def writeWorkshopData(inDict):
        """a function to write a dictionary to a workshop txt file

        Args:
            inDict (String): a dictionary to be worte into the txt file
        """
        file = open('workshop.txt',mode='w+')
        for d in inDict:
            writeStr = d+":"+inDict[d][0]+" "+inDict[d][1]+" "+inDict[d][2]+" "+inDict[d][3]+" "+inDict[d][4]+" "+inDict[d][5]+"\n"
            file.write(writeStr)
        file.close()
        
    def writeEnrolledData(self,inName,inDict):
        """a function to write a dictionary to a student's txt file

        Args:
            inDict (String): a dictionary to be worte into the txt file
        """
        file = open(inName+'.txt',mode='w+')
        for d in inDict:
            writeStr = d+":"+inDict[d][0]+" "+inDict[d][1]+" "+inDict[d][2]+" "+inDict[d][3]+" "+inDict[d][4]+" "+inDict[d][5]+"\n"
            file.write(writeStr)
        file.close()

    def isfindBywIDforEroll(self,sID,inwID):
        """
        function to find whether the workshop is erolled or not 
        parameter
        - sID: the student ID
        - inwID: the input workshop ID
        """
        file = open(sID +".txt",mode='r')
        readLine = file.readlines()
        
        if readLine == ['\n']:
            return False
        else:
            return self.isfindBywIDforCancel(sID,inwID)

    def isfindBywIDforCancel(self,sID,inwID):
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
        
    def eroll(self,sID,wID):
        """
        function to ecroll workshop by student

        parameter:
            - sID: the student ID
            - wID: the workshop ID which the student want to enroll
        """
        outDict = student.getWorkshopDataDict()

        outDictsID = self.getEnrolledDataDict(sID)

        if self.isfindBywIDforEroll(sID,wID) == False:    
                    if int(outDict[wID][5]) <= 0:
                        print("Sorry you can not eroll the workshop! No remaining quota!")
                    else: 
                        outDict[wID][5] = str(int(outDict[wID][5]) - 1)
                        outDictsID[wID] = outDict[wID]
                        
                        student.writeWorkshopData(outDict)
                        for item in outDictsID:
                            outDictsID[item] = outDict[item]
                        self.writeEnrolledData(sID,outDictsID)
                        
                        print("Successful erollment!")
        else:
            print("Sorry you can not eroll this workshop more than once!")

    def cancel(self,sID,wID):
        """
        function to cancle workshop which has been erolled by student

        parameter:
            - sID: the student ID
            - wID: the workshop ID which the student want to cancel
        """
        outDict = student.getWorkshopDataDict()

        outDictsID = self.getEnrolledDataDict(sID)

        if self.isfindBywIDforCancel(sID,wID) == True: 
            
            outDict[wID][5] = str(int(outDict[wID][5]) + 1)
            outDictsID.pop(wID)
            
            student.writeWorkshopData(outDict)
            for item in outDictsID:
                outDictsID[item] = outDict[item]
            self.writeEnrolledData(sID,outDictsID)
            
            print("Successful cancllation!")

    def listAll():
        """
        function to print all workshops to studnets
        """
        file = open('workshop.txt',mode='r')
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
                      +"\nRemaining:   "+outDict[d][5]
                      +"\n----------------------")
        
    def listEnrolledWs(self,sID):
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
        
        wsDict = student.getWorkshopDataDict()
        
        if (len(outDict) == 0):
            print("No enrolled workshop!")
        else:
            for d in outDict:
                print("workshop ID: "+d
                        +"\nTitle:       "+wsDict[d][0]
                        +"\nLocation:    "+wsDict[d][1]
                        +"\nDate:        "+wsDict[d][2]
                        +"\nTime:        "+wsDict[d][3]
                        +"\nRemaining:   "+wsDict[d][5]
                        +"\n----------------------")
    
    #-------------------login interface for student-------------------
    def login():
        """
        function for student to login
        """
        for times in range(100):
            inUsers = student.setUsers()
            if student.isContainUsers(inUsers):
                for times2 in range(3):
                    inPasswd = student.setPasswd()
                    if student.isCorrectPasswd(inUsers,inPasswd)==True:
                        print("Successfully login! Welcome, student {0}!".format(inUsers))
                        inStudnet = student(inUsers,inPasswd)
                        inStudnet.studentInterface()
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
        else:
            print("")

    

    #-------------------function interface for student-------------------
    def studentInterface(self):
        """an interface for student function including Enroll a workshop; Cancel a workshop; ListAll; List enrolled workshops; Search in workshops
        """
        print("Please select function: (e)Enroll a workshop; (c)Cancel a workshop; (la)ListAll; (l)List enrolled workshops; (s) Search in workshops (q)Quit".center(100),"\n","(e/c/la/l/s/q)".center(100,"*"))
        choose = input().lower()
        if(choose == "e"):
            wID = input("Please input the ID of which workshop you want to eroll:")
            self.eroll(self.getUsers(),wID)
        elif(choose == "c"):
            wID = input("Please input the ID of which workshop you want to cancel:")
            self.cancel(self.getUsers(),wID)
        elif(choose == "la"):
            print("---All workshops---\n----------------------")
            student.listAll()
        elif(choose == "l"):
            print("---Your Enrollments---\n----------------------")
            self.listEnrolledWs(self.getUsers())
        elif(choose == "q"):
            main()
            return 0
        elif(choose == "s"):
            print("Search workshop information:")
            print("Search based on (i)workshopID; (n):Name; (l)Location; (d)Date; (t)Time; (r)Remaining; else to back".center(100),"\n","(i/n/d/t/r)".center(100,"*"))
            choose = input().lower()
            print("Please enter the data to search:".center(100))
            data = input()
            searchEngine.setStudnet()
            if(choose == "i"):
                searchEngine.findBywID(data)
            elif(choose == "n"):
                searchEngine.findByName(data)
            elif(choose == "d"):
                searchEngine.findByDate(data)
            elif(choose == "t"):
                searchEngine.findByTime(data)
            elif(choose == "r"):
                searchEngine.findByRemaining(data)
            elif(choose == "l"):
                searchEngine.findByLocation(data)
            else:
                print("Empty or Illegal input, back to the previous page!")
            self.studentInterface()
        else:
            print("Empty or illegal input, please try again!")
        self.studentInterface()
    
    def strToTxt(users):
        """
        function to write string into txt
        parameter:
            - users: user ID
        """
        # users = student.getUsers()
        if student.isContainUsers(users)==False:   
            passwd = student.setPasswd()
            str = "\n"+users+" "+passwd
            with open('student.txt','a')as file:
                file.write(str)
            print("Seccessfully register a new account as student!")
            student.login()
        else:
            print("Unseccessfully register a new account as student because already has the same users!")
            student.addusers()
       
    def addusers():
        """
        function to register a new student account
        """
        users = student.setUsers()
        if student.isContainUsers(users):
            print("The users have already register before, do you want to back to (l)login or continue (r)registering?".center(100),"\n","(l/r)".center(100,"*"))
            choose = input().lower()
            if choose=="l":
                student.login()
            elif choose =="r":
                users = student.setUsers()
                student.strToTxt(users)
        else:
            student.strToTxt(users)


def main():
    """
    function to run the whole program
    """
    print("Welcome to use Workshops Enrollment System made by Group 2!".center(100))
    print("Choose your identity, (a)administrator or (s)student? q for quit".center(100),"\n","(a/s/q)".center(100,"*"))
    identity = input()
    if identity == "a":
        administrator.login()
    elif identity == "s":
        print("Do you want to (l)login or (r)register a new account? q for quit".center(100),"\n","(l/r/q)".center(100,"*"))
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