
#pragma once

class Tool {
private:
    int multiplier_;
public:
    Tool() = default;

    Tool(const Tool &) = default;
    Tool(Tool &&) = default;
    Tool &operator=(const Tool &) = default;
    Tool &operator=(Tool &&) = default;
    virtual ~Tool() = default;

    void setMultiplier(int multiplier);

    int multiplyValue(int x);
};
