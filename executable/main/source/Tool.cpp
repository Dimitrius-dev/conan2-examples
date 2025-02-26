
#include "Tool.h"
#include "Substract.h"

void Tool::setMultiplier(int multiplier){
    Substract secondTool;

    secondTool.setSubtractive(1);
    multiplier_ = secondTool.substract(multiplier);
}

int Tool::multiplyValue(int x){
    return x * multiplier_;
}
