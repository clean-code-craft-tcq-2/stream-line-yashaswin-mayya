#include <stdio.h>
#include "receiver.h"

void ReadParametersfromConsole(float* SOC, float* Temperature)
{
  for(int paramindex=0; paramindex<NO_OF_READINGS; paramindex++)
    {
        scanf("%f ,%f ",&SOC[paramindex],&Temperature[paramindex]);
    }
}

//Calculate maximum value for the battery parameters
float CalculateMaxValue(float inputData[])
{
  float MaxValue = inputData[0];
    for(int i=1; i<NO_OF_READINGS; i++)
    {
        if(MaxValue < inputData[i])
        {
            MaxValue = inputData[i];
        }
    }
    return MaxValue;
}

//Calculate minimum value for the battery parameters
float CalculateMinValue(float inputData[])
{
  float MinValue = inputData[0];
    for(int i=1; i<NO_OF_READINGS; i++)
    {
        if(MinValue > inputData[i])
        {
            MinValue = inputData[i];
        }
    }
    return MinValue;
}

//Calculate simple moving average for the last 5 parameters
float CalculateSMA(float inputData[])
{
  float sum;
  float SMA;
    for (int i = (NO_OF_READINGS - 5); i < (NO_OF_READINGS); i++)
    {
      sum += inputData[i];
    }
  SMA = sum/5;
  return SMA;
}

void PrintComputedData(float *BMSParameter, float MaxValue, float Minvalue, float SMA)
  {
  printf("Data received from sender\n");
  for(int index = 0; index < NO_OF_READINGS; index++)
  {
    printf("%f\n",BMSParameter[index]);
  }
  printf("Max value: %f, Min value: %f, SMA: %f\n",MaxValue,Minvalue,SMA);
  }
