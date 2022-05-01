void ReadParametersfromConsole(float* SOC, float* Temperature)
{
  for(int paramindex=0; paramindex<NO_OF_READINGS; paramindex++)
    {
        scanf("%f ,%f ,%f",&SOC[paramindex],&Temperature[paramindex]);
    }
}

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

float CalculateSMA(float inputData[])
{
    for (int i = (NO_OF_READINGS - 5); i < (NO_OF_READINGS); i++)
    {
      sum += inputData[i];
    }
  SMA = sum/5;
  return SMA;
}
