

# Менеджемент существующих пакетов

### Команда `conan search`

Используется для поиска пакетов в удаленных репозиториях.
```
computer:/mnt/m/files/job/Guides/conan2$ conan search boost
Found 17 pkg/version recipes matching boost in conancenter
conancenter     
  boost         
    boost/1.70.0
    boost/1.71.0
    boost/1.72.0
    boost/1.73.0
    boost/1.74.0
    boost/1.75.0

```

### Команда `conan list`

Используется для поиска пакетов в локальном репозитории (кеше).

```
computer:/mnt/m/files/job/Guides/conan2$ conan list "boost"
Found 1 pkg/version recipes matching boost in local cache
Local Cache
  boost
    boost/1.84.0
```

### Команда `conan graph`

Используется для анализа пакета на его зависимости и настройки.

### Команда `conan download`

Используется для скачивания пакетов в локальный репозиторий (кеш).

### Команда `conan remove`

Используется для удаления пакетов из локального репозитория (кеша).

### Команда `conan test`

Используется для проверки использования пакета на конкретной системе.
