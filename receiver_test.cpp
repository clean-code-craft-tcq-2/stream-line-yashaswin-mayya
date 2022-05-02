#define CATCH_CONFIG_MAIN
#include "test/catch.hpp"
#include "receiver.h"

TEST_CASE("Check whether the data is read from console") 
{
  float SOC[NO_OF_READINGS] = {0};
  float Temperature[NO_OF_READINGS] = {0};

  ReceiverData(SOC,Temperature);
  float expectedoutput[3][2] = {{79.326,9.747}, {47.868,13.747},{78.344, 38.571}};
  for(int i=0;i<3;i++)
  {
    REQUIRE(SOC[i] == expectedoutput[i][0]);
    REQUIRE(Temperature[i] == expectedoutput[i][1]);
  }
}
