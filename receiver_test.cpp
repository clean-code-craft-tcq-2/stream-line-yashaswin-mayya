#define CATCH_CONFIG_MAIN
#include "test/catch.hpp"
#include "receiver.h"

//TEST_CASE("Tests to check whether sensor data is read from console") 
//{
  float Temperature[NO_OF_READINGS] = {0};
  float SOC[NO_OF_READINGS] = {0};
  //float ChargeRate[NO_OF_READINGS] = {0};
  //float Current_MaxValue, Current_MinValue, Current_SMAValue, expectedMaxValue, expectedMinValue, expectedSMAValue;
  
  ReceiverData(SOC,Temperature);
 
