//
// Created by Dmitrii on 14.02.2025.
//

#pragma once

class Tool2 {
public:
    Tool2() = default;
    Tool2(const Tool2 &) = default;
    Tool2(Tool2 &&) = default;
    Tool2 &operator=(const Tool2 &) = default;
    Tool2 &operator=(Tool2 &&) = default;
    virtual ~Tool2() = default;

    int tool2(int x, int y);
};