//
// Created by Dmitrii on 13.02.2025.
//

#pragma once

class Substract {
private:
    int subtractive_;
public:
    Substract() = default;
    Substract(const Substract &) = default;
    Substract(Substract &&) = default;
    Substract &operator=(const Substract &) = default;
    Substract &operator=(Substract &&) = default;
    virtual ~Substract() = default;

    void setSubtractive(int subtractive);

    int substract(int multiplier);
};