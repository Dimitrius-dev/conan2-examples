
#include "m_simple/Printer.h"

#include <spdlog/spdlog.h>

void Printer::print(int x){
    spdlog::info("value: {}", x);
}
