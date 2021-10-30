def updateWs(wID,infoList):
    file = open('workshop.txt',mode='r')
    readLine = file.readlines()
    outList = []
    
    for i in readLine:
        lineList = i.strip("\n").split(":")
        lineList[1] = lineList[1].split(" ")
        outList.append(lineList)
    outDict = dict(outList)
    file.close()

    outDict[wID] = infoList

    file = open('workshop.txt',mode='w+')
    for d in outDict:
        writeStr = d+":"+outDict[d][0]+" "+outDict[d][1]+" "+outDict[d][2]+" "+outDict[d][3]+" "+outDict[d][4]+"\n"
        file.write(writeStr)
    file.close
    # print(outDict)

updateWs('W000001',['workshop2','pq604b','1300-1400','50','50'])