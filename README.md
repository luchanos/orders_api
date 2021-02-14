# orders_api
Сервис для работы с заявками

# orders_api_service
Orders_api_service - это наш сервер на Django. В его файлах производится конфигурация всех наших частей
проекта. Сейчас в рамках проекта orders_api реализуется 1 часть: orders.

# orders
Предназначен для работы с заявками и созданию ручек по управлению ими.

# ХОЗЯЙКЕ НА ЗАМЕТКУ
Для запуска сервера Django выполняем команду:

python manage.py runserver -> дальше идём по адресу, который высветится в консоли и радуемся, если там окно с ракетой.

Чтобы создать новый подпроект, необходимо выполнить команду:

python manage.py startapp <имя_подпроекта>

После этого будет создана директория, в которой будут хранится файлы для моделей, 
вьюх, конфигурирования админки и так далее.

ПО УМОЛЧАНИЮ ИСПОЛЬЗУЕТСЯ БД SQLITE3, НО МЫ БУДЕМ ПЕРЕХОДИТЬ НА POSTGRESQL!

# ПОЛЕЗНЫЕ ССЫЛКИ

Итак, я подобрал для всех нас кое-какие материалы для изучения и погружения в Бэкендовую тематику применительно к 
проекту. Какие-то ресурсы я уже сам изучил, какие-то придётся (видеокуроки по Django)

ЧТО ПОНАДОБИТСЯ ЗНАТЬ И УМЕТЬ В ПЕРВУЮ ОЧЕРЕДЬ:

Статьи по API. Читать для понимания того, что это такое:
https://habr.com/ru/post/483202/

и

https://habr.com/ru/post/464261/#:~:text=API%20(Application%20programming%20interface)%20%E2%80%94,%D0%B1%D1%8B%D0%BB%D0%BE%20%D0%B1%D1%8B%20%D1%81%D0%BB%D0%BE%D0%B2%D0%BE%20%C2%AB%D0%B4%D0%BE%D0%B3%D0%BE%D0%B2%D0%BE%D1%80%C2%BB.

ЗАЧЕМ? Веб сервис с API - ядро нашего проекта. Именно через взаимодействие с ним будут происходить большинство операций.


Основы контейнеров. 6 статей на хабре, все можно найти по ссылке:
https://habr.com/ru/company/ruvds/blog/438796/ - докеры
https://habr.com/ru/company/ruvds/blog/450312/ - докер-компоуз

ЗАЧЕМ? Деплоить своё приложение мы будем в контейнере (на самом деле даже в контейнерах). 
В одном будет сидеть база, в другом один сервис (например обработки заявок), а в другом другой 
(например веб-сервис с API). Кроме того компоуз нам очень сильно понадобится во время тестирования.


PYTEST. Полная книга в переводе выложена на Хабре:

https://habr.com/ru/post/448782/

+ у меня неколько роликов на моём канале, обязательно их посмотрите!

ЗАЧЕМ? Очевидно, что для того, чтобы научиться писать тесты)

Django. Является тем веб-фреймворком, на котором мы будем выстраивать архитектурную логику нашего приложения. 
Я его не знаю от слова совсем, так что изучать будем вместе - от простого к сложному. Я выбрал для основы 
изучения вот этот видеокурс на ютубе:

https://www.youtube.com/watch?v=i0lkpO289jw&list=PLrgHtaQ10vi3xalWI7q6Uzr7aZUNT0BJH&ab_channel=AlekseyBelkin

https://drive.google.com/drive/folders/10gV26Vuj0nU9LDZHg6cmpwVKFQQMv-3a?usp=sharing - КУРСЫ ПО ВСЯКИМ ПОЛЕЗНОСТЯМ

ЗАЧЕМ? На этом фреймворке будет написано наше API.

- работа через API - https://www.coursera.org/lecture/python-for-web/rabota-chieriez-web-api-yKxXr

SQL. Возьмите абсолютно любой курс или набор видосов на ютубе - у нас пока всё будет достаточно просто. 
Вот что нужно уметь:

- создавать таблицы;
- изменять таблицы;
- добавлять и удалять записи;
- делать SELECT с различными группировками и условиями;
- делать JOIN'ы.

HTML, CSS - я пока не знаю, стоит ли его учить отдельно, так как видел, что в курсе по Django это есть. 
Разбираться будем на месте.

КАК УЧИТЬ: берёте примеры из статей и видосов и методично пробуете у себя на компе.

До кучи: будем осваивать работу с Гитом в команде. Пока что думаю нам более, чем достаточно. Дальше будем подключать
 технологии по мере необходимости.
