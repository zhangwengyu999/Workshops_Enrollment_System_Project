def isfindBywID(sID,inwID):
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



    if isfindBywID(sID,wID) == True:
        for d in outDict:
            #print(d)
            if d == wID: 
                outDict[d][4] = str(int(outDict[d][4]) + 1)
                file = open("workshop.txt",mode="w+")
                cancelWorkshop = open(sID+".txt","w+")
                for d in outDict:
                    writeStr = d+":"+outDict[d][0]+" "+outDict[d][1]+" "+outDict[d][2]+" "+outDict[d][3]+" "+outDict[d][4]+"\n"
                    file.write(writeStr)
                for i in outDictsID:
                    if i != wID:
                        writeStr = i+":"+outDict[i][0]+" "+outDict[i][1]+" "+outDict[i][2]+" "+outDict[i][3]+" "+outDict[i][4]+"\n"
                        cancelWorkshop.write(writeStr)
                file.close()                
                cancelWorkshop.close()
                print("Successful cancllation!")


def main():
    cancel("yhw789","W000000")
main()