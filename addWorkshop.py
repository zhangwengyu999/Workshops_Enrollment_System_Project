from os import write

#print(inWorkshop.readlines())
def addWs(wID,infoString):
    inWorkshop = open("workshop.txt",'a+')
    inAllInfo = wID + ":" + infoString
    inWorkshop.write("\n")
    inWorkshop.write(inAllInfo)
    inWorkshop.close()


def main():
    addWs("W000002","workshop1,pq604a,1200-1300,100,100")
main()

