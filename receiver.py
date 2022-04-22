import sys


class Receiver:

    def getRawValuesFromConsole(self):
        consoleReadValues = []
        incomingStreamLines = sys.stdin.readlines()
        for streamValue in incomingStreamLines:
            streamValue = streamValue.strip()
            if streamValue == '\n':
                continue
            consoleReadValues.append(streamValue)
        return consoleReadValues

    def processInput(self):
        unprocessedInput = self.getRawValuesFromConsole()
        for index in range(len(unprocessedInput)):
            if 'Temperature' in unprocessedInput[index]:
                temperatureDataStartIndex = index
            if 'SOC' in unprocessedInput[index]:
                SOCDataStartIndex = index
        processedTemperatureData = unprocessedInput[temperatureDataStartIndex+1:SOCDataStartIndex]
        processedSOCData = unprocessedInput[SOCDataStartIndex+1:]
        return processedTemperatureData, processedSOCData

    def getMinAndMaxData(self):
        
        processedTemperatureData, processedSOCData = self.processInput()
        Temperature_Min = min(processedTemperatureData)
        Temperature_Max = max(processedTemperatureData)
        SOC_Min = min(processedSOCData)
        SOC_Max = max(processedSOCData)

        self.printToConsole(f'\nMinimum Temperature is {Temperature_Min} and Maximum Temperature is {Temperature_Max}')
        self.printToConsole(f'\nMinimum SOC is {SOC_Min} and Maximum SOC is {SOC_Max}')

    
    def getSimpleMovingAverage(self):
        samplesInMovingAverage = 5
        processedTemperatureData, processedSOCData = self.processInput()

        self.printToConsole(f'\nLast {samplesInMovingAverage} moving average for Temperature:')
        for sample in self.calculateSimpleMovingAverage(samplesInMovingAverage, processedTemperatureData):
            self.printToConsole(sample)
        

        self.printToConsole(f'\nLast {samplesInMovingAverage} moving average for SOC:')
        for sample in self.calculateSimpleMovingAverage(samplesInMovingAverage, processedSOCData):
            self.printToConsole(sample)


    def calculateSimpleMovingAverage(self, samplesInMovingAverage, listToProcess):
        simpleMovingAverageList = []
        for index in range(len(listToProcess)):
            if(index<samplesInMovingAverage-1):
                simpleMovingAverageList.append('-')
                continue
            samplesForAverageCalulation = listToProcess[index-samplesInMovingAverage+1:index+1]
            movingAverage = round(sum(samplesForAverageCalulation)/samplesInMovingAverage, 2)
            simpleMovingAverageList.append(movingAverage)
        return simpleMovingAverageList


    def printToConsole(self, consoleMessage):
        print(consoleMessage)
        return consoleMessage

#Receiver().getMinAndMaxData()
#Receiver().getSimpleMovingAverage()