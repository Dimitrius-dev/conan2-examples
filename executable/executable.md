
# Conan при создании исполняемой программы
___

## Описание

Для создания исполняемой программы нужно создать конфигурационный файл либо
**conanfile.txt**, либо **conanfile.py**.
В данной статье рассматривается только **conanfile.py** так как он имеет большую гибкость при настройке проекта. 
Про conanfile.txt можно почитать [тут](https://docs.conan.io/2/reference/conanfile_txt.html#conanfile-txt).
Про разницу conanfile.txt с conanfile.py можно почитать [тут](https://docs.conan.io/2/tutorial/consuming_packages/the_flexibility_of_conanfile_py.html#consuming-packages-flexibility-of-conanfile-py).

Структура проекта
```
-main
    -include
        Printer.h
        Substract.h
        Tool.h
    -source
        Printer.cpp
        Substract.cpp
        Tool.cpp
    CMakeLists.txt
-executable
    -include
    -source
        main.cpp
    CMakeLists.txt
-tests
    -include
        test_1.h
    -source
        tests.cpp
    CMakeLists.txt
CMakeLists.txt
conanfile.py
```

main - основной программный продукт  
executable - формирование исполняемого файла из основного программного продукта  
tests - формирование тестов из основного программного продукта  


___
## Требования к шаблону

Обязательная структура проекта

```
-tests
    ...
    CMakeLists.txt (цель - tests)
...
CMakeLists.txt
conanfile.py
```

___
## Сборка

### Описание

Для ознакомления с разделом в данной папке представлен проект-шаблон, который вы можете собрать самостоятельно.

### Автоматическая сборка из conan
Сборку в стиле conan можно провести с помощью команды:  
1. ```conan build . -s build_type="Release" -c tools.build:skip_test=False -pr=default --build=missing```

В результате мы получим папку build со всеми требуемыми целями.


### Сборка по отдельности

Можно провести сборку по отдельности
1. Подгрузить зависимости в соответствии с требованиями ```conan install . -pr=default -of=conan_install --build=missing -s build_type=Release```

2. Сконфигурировать проект ```cmake -S . -B project_build -DCMAKE_TOOLCHAIN_FILE=./conan_install/build/Release/generators/conan_toolchain.cmake -DCMAKE_BUILD_TYPE=Release -G "Unix Makefiles"```

3. Собрать проект ```cmake --build project_build```

В результате мы получим папку project_build со всеми требуемыми целями.
