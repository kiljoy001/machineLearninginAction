import numpy as np
import operator
import os
from pathlib import Path
import sys

class HandWritingRecognition:


    def __init__(self, filename):
        self.filename = os.listdir(filename)
    
    def img2vector(self):
        returnVect = np.zeros((1,1024))
        for fileitem in self.filename:
            fr = open(fileitem)
            for i in range(32):
                lineStr = fr.readline()
            for j in range(32):
                returnVect[0, 32 * i + j] = int(lineStr[j])
            return returnVect


    def classify0(self, inX, dataSet, labels, k):
        dataSetSize = dataSet.shape[0]
        diffMat = np.tile(inX, (dataSetSize,1)) - dataSet
        sqDiffMat = diffMat**2
        sqDistances = sqDiffMat.sum(axis=1)
        distances = sqDistances**0.5
        sortedDistIndicies = distances.argsort()     
        classCount={}          
        for i in range(k):
            voteIlabel = labels[sortedDistIndicies[i]]
            classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
        sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
        return sortedClassCount[0][0]

    def handwritingClassTest(self):
        hwLabels = []
        trainingFileList = os.listdir('trainingDigits')           #load the training set
        m = len(trainingFileList)
        trainingMat = np.zeros((m,1024))
        for i in range(m):
            fileNameStr = trainingFileList[i]
            fileStr = fileNameStr.split('.')[0]     #take off .txt
            classNumStr = int(fileStr.split('_')[0])
            hwLabels.append(classNumStr)
            trainingMat[i,:] = self.img2vector()
        testFileList = os.listdir('testDigits')        #iterate through the test set
        errorCount = 0.0
        mTest = len(testFileList)
        for i in range(mTest):
            fileNameStr = testFileList[i]
            fileStr = fileNameStr.split('.')[0]     #take off .txt
            classNumStr = int(fileStr.split('_')[0])
            vectorUnderTest = self.img2vector()
            classifierResult = self.classify0(vectorUnderTest, trainingMat, hwLabels, 3)
            print(f'the classifier came back with: {classifierResult}, the real answer is: {classNumStr}')
        if (classifierResult != classNumStr): errorCount += 1.0
        print (f'\nthe total number of errors is: {errorCount}')
        print ("\nthe total error rate is: %f" % (errorCount/float(mTest)))

os.system('cls')
print("Welcome User. Please select from the menu below\n1) Run Handwriting recognition program\n2) Run Handwriting recognition test\n3) Exit Program\n")
#mod_path = Path.(__file__).parent
system = HandWritingRecognition('C:\\Users\\kiljo\\Desktop\\Machine Learning\\machinelearninginaction\\Ch02\\digits\\testDigits')
choice = int(input("Please make a selection"))
if choice == 1:
    system.handwritingClassTest()
elif choice == 2:
    system.handwritingClassTest()
elif choice == 3:
    sys.exit()
