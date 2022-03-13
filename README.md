# SupportApplication
***

### __Технологии__:
1. [Django](https://www.djangoproject.com)
2. [Django Rest Framework](https://www.django-rest-framework.org)
3. [PostgreSQL](https://www.postgresql.org)
4. [Celery](https://docs.celeryproject.org)
5. [Redis](https://redis.io)
6. JWT авторизация
***
### __Описание__:

API стремится к __RESTFUL__ и представляет собой службу имитацию службы поддержки.
Пользователь (supporter) устанавливается админом.
Тикет уходит к самому разгруженному саппорту.

Перейдя на /redoc/ можно посмотреть документацию.

***
### __Эндпоинты__:

* /api/auth/jwt/create/ - Получить токен
* /api/auth/refresh/ - Обновить токен
* /api/auth/refresh/ - Проверить токен
* /api/tickets/ - Получить список ваших тикетов / Создать новый
  * /{id}/ - Подробная информация
    * /feedbacks/ - Переписка по выбранному тикету
* /api/supporter/tickets/ - Просмотреть подписки / Подписаться
  * /{id}/ - Подробная информация
    * /feedbacks/ - Переписка по выбранному тикету

***
### __Для развертывания__:
    git clone git@github.com:AlexandrBurak/SupportApplication.git
    cd supportaplication/
    docker build .
    docker-compose up -d --build
***