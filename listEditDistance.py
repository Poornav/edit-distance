#Takes a source string along with list of destination words
import EditDistance as ed
srcStr = raw_input("Enter the source string:")
wordList = raw_input("Enter a list of words separated by commas:").split(",")
strLen = len(srcStr)
scoreList = []
for word in wordList:
    scoreList.append(ed.CalcDistance(srcStr,word))
minDist = min(scoreList)
print "Minimum edit distance is", minDist,"for the word", wordList[scoreList.index(minDist)]
