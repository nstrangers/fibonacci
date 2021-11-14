1. Проверка версии Git
    git --version

2. Инициализация Git
    git init

3. Зададим има пользователя и email (один раз для компьютера)
    git config --global user.name "Sergey Nikolaev"
    git config --global user.email "n.strtangers@gmail.com"

4. Проверка статуса репозитория
    git status

5. Добавление файлов в отслеживание
    git add filename

    для добавления всех файлов:
    git add .

6. Commit - сохранение текущей версии проекта на основе добавленных в отслеживание + коммент к версии
    git commit -m "message"

    комментарий можно не писать
    git commit