def listEnrolledWs(sID):
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

    print("---Your Enrollments---\n----------------------")
    for d in outDict:
        print("workshop ID: "+d+"\nTitle:       "+outDict[d][0]+"\nLocation:    "+outDict[d][1]+"\nDate & Time: "+outDict[d][2]+"\nQuotas:      "+outDict[d][3]+"\nRemaining:   "+outDict[d][4]+"\n----------------------")

listEnrolledWs("cdr123")