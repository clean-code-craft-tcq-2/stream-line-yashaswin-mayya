#define CATCH_CONFIG_MAIN
#include "test/catch.hpp"
#include "receiver.h"

TEST_CASE("Test to calculate maximum value in an array")
{
    float inputarray[5] = {1.05, 80.2, 48, 17.66, 0.001};
    float MaxValue = CalculateMaxValue(inputarray);

    REQUIRE(MaxValue == 80.2f);
}

