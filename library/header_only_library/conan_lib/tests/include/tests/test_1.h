

#pragma once

#include <gtest/gtest.h>

#include "ho_simple/ho_simple.h"


TEST(Tool1, scenery){
    Tool1 tool;

    ASSERT_EQ(tool.tool1(1, 1), 2);
}

TEST(Tool2, scenery){
    Tool2 tool;

    ASSERT_EQ(tool.tool2(1, 1), 0);
}
