def findByRemaining(inRemaining):
    """
    function to find workshops according to thier remaining quotas , and print out

    parameter:
        - inName: a String of the workshop's remaining quotas
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
    
    flag = False
    print("--------Found:--------\n----------------------")
    for d in outDict:
        if (outDict[d][4] == inRemaining):
            flag = True
            print("workshop ID: "+d+"\nTitle:       "+outDict[d][0]+"\nLocation:    "+outDict[d][1]+"\nDate & Time: "+outDict[d][2]+"\nQuotas:      "+outDict[d][3]+"\nRemaining:   "+outDict[d][4]+"\n----------------------")
    if (flag == False):
        print("NOT FOUND!")

findByRemaining('100')