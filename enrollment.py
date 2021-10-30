import findBywID

def eroll(sID,wID):
    workshopRemainder = open("workshopOriginal.txt")
    readLine = workshopRemainder.readlines()
    outList = []
    
    for i in readLine:
        lineList = i.strip("\n").split(":")
        lineList[1] = lineList[1].split(" ")
        outList.append(lineList)
    outDict = dict(outList)
    workshopRemainder.close()

    
    for d in outDict:
        #print(d)
        if d == wID:
            if int(outDict[d][4]) <= 0:
                print("Sorry you can not eroll the workshop!")
            else: 
                outDict[d][4] = str(int(outDict[d][4]) - 1)
                file = open("workshopOriginal.txt",mode="w+")
                erollWorkshop = open("yhw123.txt","a+")
                for d in outDict:
                    if d == wID:
                        writeStr = d+":"+outDict[d][0]+" "+outDict[d][1]+" "+outDict[d][2]+" "+outDict[d][3]+" "+outDict[d][4]+"\n"
                        file.write(writeStr)
                        erollWorkshop.write(writeStr)
                file.close()                
                erollWorkshop.close()
                print("Successful erollment!")



def main():
    eroll("yhw789","W000000")
main()