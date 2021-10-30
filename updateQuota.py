def updateQuota(wID,inQuota):
    """
    function to update a workshop's quotas by the adminnistator

    parameter:
        - wID: a String of the number of workshop's ID
        - inQuota: the quotas to update to taht workshop
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

    outDict[wID][3] = inQuota

    file = open('workshop.txt',mode='w+')
    for d in outDict:
        writeStr = d+":"+outDict[d][0]+" "+outDict[d][1]+" "+outDict[d][2]+" "+outDict[d][3]+" "+outDict[d][4]+"\n"
        file.write(writeStr)
    file.close

updateQuota("W000000","200")