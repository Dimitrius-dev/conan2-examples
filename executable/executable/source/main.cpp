
#include "Tool.h"
#include "Printer.h"

int main(){
    Tool tool;

    tool.setMultiplier(6);
    int result = tool.multiplyValue(125);

    Printer printer;

    printer.print(result);

    return 0;
}