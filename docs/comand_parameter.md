
В некоторых командах, в зависимости от функционала, Conan позволяют заменять настройки, которые ранее были определены в conan profile.

Например:
В команде `conan build . -s build_type="Release" -c tools.build:skip_test=False` используется
изменение в разделе -s параметра build_type="Release" и
изменение в разделе -c параметра tools.build:skip_test=False