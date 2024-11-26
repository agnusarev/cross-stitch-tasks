# cross-stitch-tasks

Приложения для автоматизации выполнений заданий для тех кто занимается вышивкой крестиком.

## .env example

<table>
    <tr>
        <th>Переменная</th>
        <th>Значение</th>
        <th>Описание</th>
    </tr>
    <tr>
        <td>SECRET_KEY</td><td></td><td>секретный ключ, который используется для обеспечения безопасности приложения</td>
    </tr>
    <tr>
        <td>DIALECT</td><td>postgresql</td><td>Диалект языка SQL для подключения к БД</td>
    </tr>
    <tr>
        <td>DRIVER</td><td>db</td><td>драйвер для подключения к БД</td>
    </tr>
    <tr>
        <td>DB_NAME</td><td></td><td>имя БД</td>
    </tr>
    <tr>
        <td>DB_USER</td><td></td><td>имя пользователя БД</td>
    </tr>
    <tr>
        <td>DB_PASSWORD</td><td></td><td>пароль для подключения к БД</td>
    </tr>
    <tr>
        <td>DB_HOST</td><td>localhost</td><td>адрес машины, на которой запущена БД</td>
    </tr>
    <tr>
        <td>DB_PORT</td><td>5432</td><td>порт для подключения к БД</td>
    </tr>
    <tr>
        <td>DB_SCHEMA</td><td>schema</td><td>название схемы БД</td>
    </tr>
    <tr>
        <td>FLASK_DEBUG</td><td>1</td><td>1-включение режима отладки в Flask</td>
    </tr>
</table>

# installation
```bash
poetry install
```

# run
```bash
make run
```

# tests
TODO
