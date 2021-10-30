def getDictFromTxt(inTxt):
    """
    function to return a dictionary based on a given txt file

    parameter:
        - inTxt: given txt file

    return:
        - outDict: the dictionary based on that txt file
    """
    file = open(inTxt+'.txt',mode='r')
    readLine = file.readlines()
    outList = []
    
    for i in readLine:
        lineList = i.strip("\n").split(":")
        lineList[1] = lineList[1].split(" ")
        outList.append(lineList)
    outDict = dict(outList)
    file.close()
    return outDict