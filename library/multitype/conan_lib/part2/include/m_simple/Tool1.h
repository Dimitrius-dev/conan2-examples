
#pragma once

class Tool1 {
public:
    Tool1() = default;
    Tool1(const Tool1 &) = default;
    Tool1(Tool1 &&) = default;
    Tool1 &operator=(const Tool1 &) = default;
    Tool1 &operator=(Tool1 &&) = default;
    virtual ~Tool1() = default;

    int tool1(int x, int y);
};
