def isfindBywID(sID,inwID):
    """
    function to find whether the workshop is erolled or not 

    parameter
        - sID: the student ID
        - inwID: the input workshop ID
    """
    file = open(sID +".txt",mode='r')
    readLine = file.readlines()
    print(readLine)
    outList = []
    
    if readLine == ['\n']:
        return False
    else:
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

    if isfindBywID(sID,wID) == False:    
        for d in outDict:
            #print(d)
            if d == wID:
                if int(outDict[d][4]) <= 0:
                    print("Sorry you can not eroll the workshop!")
                else: 
                    outDict[d][4] = str(int(outDict[d][4]) - 1)
                    file = open("workshop.txt",mode="w+")
                    erollWorkshop = open(sID+".txt","a+")
                    for d in outDict:
                        writeStr = d+":"+outDict[d][0]+" "+outDict[d][1]+" "+outDict[d][2]+" "+outDict[d][3]+" "+outDict[d][4]+"\n"
                        file.write(writeStr)
                        if d == wID:
                            erollWorkshop.write(writeStr)
                    file.close()                
                    erollWorkshop.close()
                    print("Successful erollment!")
    else:
        print("Sorry you can not eroll this workshop more than once!")


def main():
    eroll("yhw789","W000000")
main()