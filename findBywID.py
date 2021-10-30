def findBywID(inwID):
    """
    function to find a workshop according to its ID, and print out

    parameter:
        - inwID: a String of the workshop's ID
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
    
    if (inwID not in outDict):
        print("NO workshop with ID: "+inwID)
    else:
        print("--------Found:--------s\n----------------------")
        print("workshop ID: "+inwID+"\nTitle:       "+outDict[inwID][0]+"\nLocation:    "+outDict[inwID][1]+"\nDate & Time: "+outDict[inwID][2]+"\nQuotas:      "+outDict[inwID][3]+"\nRemaining:   "+outDict[inwID][4]+"\n----------------------")

findBywID("W000002")