
# Профиль

Профили в Conan используются для определения настроек, которые применяются при сборке или использовании пакетов.
Профиль может содержать информацию о компиляторе, архитектуре, операционной системе, флагах компиляции и других параметрах.
Профили позволяют легко переключаться между разными конфигурациями, например, между Debug и Release или между разными архитектурами (x86/x64).
Профили обычно хранятся в папке ~/.conan2/profiles/.


## Настройка профиля

Для использования conan требуется настройть свой собственный профиль **profile**. Это связано с тем, что уникального способа определения окружения
не существует. Поэтому именно этот момент остается в ручном режиме конфигурации. Существующие бинарные файлы библиотек будут работать только для конкретной системы, на которой они были собраны.

Список профилей можно посмотреть командой `conan profile list`.

Создать профиль с названием **default** можно используя команду:  
`conan profile detect --name default`.

Найти местоположение профиля с именем default для редактирования можно с помощью команды:  
`conan profile path default`.  
Добавлять новые профили можно с помощью создания файлов по этому же пути.

В общем случае профиль выглядит так:
```
[settings]
arch=x86_64
build_type=Release
compiler=apple-clang
compiler.cppstd=gnu17
compiler.libcxx=libc++
compiler.version=14
os=Macos
```

Доступные стандартизированные значения можно посмотреть из документации в [списке доступных значений](https://docs.conan.io/2/reference/config_files/settings.html#reference-config-files-settings-yml).
Там же и написано как можно расширить данный список. При расширении важно учесть переносимость таких библиотек и взаимодействие с общедоступными.


Чтобы не надеяться на автоматическое определение расположений нужных компонентов, conan дает возможность задать их самостоятельно:

```
[settings]
arch=x86_64
build_type=Release
compiler=apple-clang
compiler.cppstd=gnu17
compiler.libcxx=libc++
compiler.version=14
os=Macos

[conf]
tools.cmake:cmake_program=/home/belov/.local/bin/cmake
tools.cmake.cmaketoolchain:generator=Ninja

[buildenv]
CC=/usr/bin/gcc-13
CXX=/usr/bin/g++-13
```

`tools.cmake:cmake_program` - путь к CMake  
`tools.cmake.cmaketoolchain:generator` - генератор, который использует CMake  

`CC` - путь к компилятору язык C  
`CXX` - путь к компилятору язык C++  
  

Подробнее [тут](https://docs.conan.io/2/reference/config_files/profiles.html#profiles)
