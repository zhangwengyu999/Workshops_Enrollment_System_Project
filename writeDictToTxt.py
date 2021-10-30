def writeDictToTxt(inDict,inTxt):
    """
    function to override a given txt file with a dictionary

    parameter:
        - inDict: a dictionary to be written into a dictionary
        - inTxt: given txt file
    """
    file = open(inTxt+'.txt',mode='w+')
    for d in inDict:
        writeStr = d+":"+inDict[d][0]+" "+inDict[d][1]+" "+inDict[d][2]+" "+inDict[d][3]+" "+inDict[d][4]+"\n"
        file.write(writeStr)
    file.close