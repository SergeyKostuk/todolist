# todolist

Пример Todo списка с использованием Django

## О проекте

Магазин выполненный на django версии 2.1, python 3.6 С SQLite.
Список имеет такой функционал:
- Cписок дел;
- возможность добавлять и удалять, редактировать записи;
- возможность отмечать выполненные задачи
- перемещать записи 

## Установка

В виртуальном окружении (virtualenv) выполнить данную команду:
```
pip install -r requirements.txt
```
Далее сделать миграции и запустить сервер командой:
```
manage.py makemigrations cand_shop
manage.py migrate cand_shop
python manage.py runserver
```
или
```
./manage.py runserver
```


## Автор

* **Kostuk Sergey**
