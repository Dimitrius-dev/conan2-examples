

#pragma once

#include <gtest/gtest.h>

#include "m_simple/Tool1.h"
#include "m_simple/Tool2.h"
#include "m_simple/Printer.h"

TEST(Tool1, scenery){
    Tool1 tool;

    ASSERT_EQ(tool.tool1(1, 1), 2);
}

TEST(Tool2, scenery){
    Tool2 tool;

    ASSERT_EQ(tool.tool2(1, 1), 0);
}

TEST(Printer, scenery){
    Printer printer;

    ASSERT_TRUE(true);
}
