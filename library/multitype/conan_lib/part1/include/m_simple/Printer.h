
#pragma once

class Printer {
public:
    Printer() = default;
    Printer(const Printer &) = default;
    Printer(Printer &&) = default;
    Printer &operator=(const Printer &) = default;
    Printer &operator=(Printer &&) = default;
    virtual ~Printer() = default;

    void print(int x);
};
