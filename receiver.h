#define NO_OF_READINGS 50

float CalculateSMA(float inputData[]);
float CalculateMaxValue(float inputData[]);
float CalculateMinValue(float inputData[]);

void ReadParametersfromConsole(float* SOC, float* Temperature);
void PrintComputedData(float *BMSParameter, float MaxValue, float Minvalue, float SMA);
int ReceiverData(//float* SOC, float* Temperature);
