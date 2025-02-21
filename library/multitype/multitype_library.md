
# Использование conan для создания static/shared библиотеки
___
Данный вид библиотеки может содержать большое количество отдельно подключаемых компонентов. Примером такой библиотеки является `Boost`.

## Структура проекта:
```
-conan_lib
    -ho_part2
        -include
            -m_simple
                Tool2.h
        -src
        CMakeLists.txt
    -part1
        -include
            -m_simple
                Printer.h            
        -src
            Printer.cpp
        CMakeLists.txt
    -part2
        -include
            -m_simple
                Tool1.h            
        -src
            Tool1.cpp
        CMakeLists.txt
    -test
        -include
            tests
                test_1.h
        -src
            tests
                test.cpp
        CMakeLists.txt
-test_package
    -src
        test_package.cpp
    CMakeLists.txt
    conanfile.py
conanfile.py
```

conan_lib - библиотека simple
test_package - тест пакета библиотеки simple

ho_part2 - header-only суб-библиотека библиотеки m_simple
part1 - суб-библиотека библиотеки m_simple
part2 - суб-библиотека библиотеки m_simple
tests - unit тесты к библиотеке m_simple

Библиотека имеет unit тесты, при сборке данные тесты по умолчанию запускаются для проверки работоспособности библиотеки на устройстве.
Если данные тесты проходят, то запускается тест пакета, который позволяет гарантировать конечному пользователю, что данный пакет безошибочно может быть подключен к сторонним проектам.


___
## conanfile.py

Метод `export_sources` определяет выгружаемые исходники (папке **conan_lib**)

Метод `requirements` определяет основные зависимости для библиотеки и тестовые зависимости для второстепенной цели тестирования (unit тесты)

Метод `configure` определяет опции зависимостей

Метод `package` импортирует заголовочные файлы каждого модуля библиотеки в соответствии с требуемой структурой

Метод `package_info` определяет способ взаимодействия с библиотекой:  
`self.cpp_info.libs` - указывает на имя выходного файла cmake (по умолчанию названию cmake цели)    
`self.cpp_info.set_property("cmake_file_name", self.name)` - задает имя выходного файла для cmake цели  
`self.cpp_info.set_property("cmake_target_name", f'{self.name}::{self.name}')` - задает имя цели  

Для произвольного компонента с именем simple_main  
`self.cpp_info.libs = [self.name]`  
`self.cpp_info.set_property("cmake_file_name", self.name)`  
`self.cpp_info.set_property("cmake_target_name", f'{self.name}::{self.name}')`  

Для компонента суб-библиотеки part1  
`self.cpp_info.components["part1_lib"].libs = ["part1"]` указывает на имя выходного файла cmake (по умолчанию названию cmake цели)  
`self.cpp_info.components["part1_lib"].set_property("cmake_target_name", f'{self.name}::part1')`  
`self.cpp_info.components["part1_lib"].includedirs = ["include/part1"]` - указывает местоположение заголовочных файлов  
`self.cpp_info.components["part1_lib"].requires = ["spdlog::spdlog"]` - указывает добавление возможности линковки списка библиотек  

Для компонента суб-библиотеки part2  
`self.cpp_info.components["part2_lib"].libs = ["part2"]` указывает на имя выходного файла cmake (по умолчанию названию cmake цели)  
`self.cpp_info.components["part2_lib"].set_property("cmake_target_name", f'{self.name}::part2')`  
`self.cpp_info.components["part2_lib"].includedirs = ["include/part2"]` - указывает местоположение заголовочных файлов  

Для компонента header-only суб-библиотеки ho_part2  
`self.cpp_info.components["ho_part2_lib"].includedirs = ["include/ho_part2"]` - указывает местоположение заголовочных файлов  

___
## Требования к шаблону

Обязательная структура проекта

```
-conan_lib
    -(название модуля библиотеки) 
        -include
            *.h
            ...
        CMakeLists.txt
        ...
    ...
    -test
        ...
        CMakeLists.txt ( цель - tests )
    CMakeLists.txt
-test_package (см документацию conan)
conanfile.py
```

Составная библиотека должна иметь хотя бы один static/shared модуль.

___
## Сборка

### Описание

Для ознакомления с разделом в данной папке представлен проект-шаблон, который вы можете собрать самостоятельно.

### Автоматическая сборка из conan
1. ```conan create . -pr=default --build=missing -c tools.build:skip_test=True```


### Сборка по частям
1. ```conan install . -of=conan_install -pr=default --build=missing -c tools.build:skip_test=True```
2. ```cmake -S . -B project_build -DCMAKE_TOOLCHAIN_FILE=../conan_install/build/Release/generators/conan_toolchain.cmake -DCMAKE_BUILD_TYPE=Release -G "Unix Makefiles" -BUILD_TESTING=OFF```
3. ```cmake --build project_build```
