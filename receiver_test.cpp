#define CATCH_CONFIG_MAIN
#include "test/catch.hpp"
#include "receiver.h"

TEST_CASE("Process sensor input and output in console")
{
  REQUIRE(ReceiverData() == 1);
}
