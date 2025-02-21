
#include "Substract.h"

void Substract::setSubtractive(int subtractive){
    subtractive_ = subtractive;
}

int Substract::substract(int x){
    return x - subtractive_;
}