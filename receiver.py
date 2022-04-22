import sys

samplesInMovingAverage = 5
class Receiver:

    def getRawValuesFromConsole(self):
        consoleReadValues = []
        incomingStreamLines = sys.stdin.readlines()
        for streamValue in incomingStreamLines:
            streamValue = streamValue.strip('\n')
            if not streamValue:
                continue
            consoleReadValues.append(streamValue)
        return consoleReadValues

    def processInput(self, unprocessedInput):
        for index in range(len(unprocessedInput)):
            if 'Temperature' in unprocessedInput[index]:
                temperatureDataStartIndex = index
            if 'SOC' in unprocessedInput[index]:
                SOCDataStartIndex = index
        processedTemperatureData = list(map(int, unprocessedInput[temperatureDataStartIndex+1:SOCDataStartIndex]))
        processedSOCData = list(map(int, unprocessedInput[SOCDataStartIndex+1:]))
        return (processedTemperatureData, processedSOCData)

    def getMinAndMaxData(self, processedIncomingValues):
        
        processedTemperatureData = processedIncomingValues[0]
        processedSOCData = processedIncomingValues[1]
        Temperature_Min = min(processedTemperatureData)
        Temperature_Max = max(processedTemperatureData)
        SOC_Min = min(processedSOCData)
        SOC_Max = max(processedSOCData)

        self.printToConsole(f'\nMinimum Temperature is {Temperature_Min} and Maximum Temperature is {Temperature_Max}')
        self.printToConsole(f'\nMinimum SOC is {SOC_Min} and Maximum SOC is {SOC_Max}')

        return [min(Temperature_Min,SOC_Min), max(Temperature_Max,SOC_Max)]

    
    def getSimpleMovingAverage(self, samplesInMovingAverage, processedIncomingValues):
        processedTemperatureData = processedIncomingValues[0]
        processedSOCData = processedIncomingValues[1]

        self.printToConsole(f'\nLast {samplesInMovingAverage} moving average for Temperature:')
        simpleMovingAverage_Temperature = self.calculateSimpleMovingAverage(samplesInMovingAverage, processedTemperatureData)
        for sample in simpleMovingAverage_Temperature:
            self.printToConsole(sample)
        
        self.printToConsole(f'\nLast {samplesInMovingAverage} moving average for SOC:')
        simpleMovingAverage_SOC = self.calculateSimpleMovingAverage(samplesInMovingAverage, processedSOCData)
        for sample in simpleMovingAverage_SOC:
            self.printToConsole(sample)

        return (simpleMovingAverage_Temperature,simpleMovingAverage_SOC)


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

    def main(self):
        isExecutionComplete = False
        if not isExecutionComplete:
           rawIncomingValues =  self.getRawValuesFromConsole()
           processedIncomingValues = self.processInput(rawIncomingValues)
           self.getMinAndMaxData(processedIncomingValues)
           self.getSimpleMovingAverage(samplesInMovingAverage, processedIncomingValues)
           isExecutionComplete = True
        return isExecutionComplete




#Receiver().main()