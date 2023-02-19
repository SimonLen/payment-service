# payment-service
Simple Django app with [Stripe API](http://stripe.com/docs)


Запуск в виртуальном окружении
------

Создаем копию (удаленного) репозитория:
```
git clone https://github.com/SimonLen/payment-service.git
```
Переходим в папку Django-проекта, создаем и активируем виртуальное окружение. Команды приведенные ниже предназначены для macOS, как настроить окружение в других операционных системах можно узнать [здесь](https://pythonist.ru/virtualnye-okruzheniya-python-i-instrumenty-dlya-upravleniya-imi/)
Предполагается, что на вашем компьютере уже установлен Python. Если нет, то вот [ссылка на скачивание Python](https://www.python.org/downloads/).
```
cd payment-service/PaymentApp
python3 -m venv venv
source venv/bin/activate
```
Обновляем менеджер пакетов Python и устанавливаем внешние зависимости:
```
pip install --upgrade pip
pip install -r requirements.txt
```
В текущей директории создаем файл `.env` и сохряняем в нем три переменные:
```
DJANGO_SECRET_KEY = ''
STRIPE_PUBLIC_KEY = ''
STRIPE_SECRET_KEY = ''
```
Stripe Publishable key и Secret key получаем [здесь](https://dashboard.stripe.com/apikeys). А DJANGO_SECRET_KEY генерируем следующим образом:
```
django-admin shell
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
```
Запускаем тестовый сервер (на http://127.0.0.1:8000):
```
python manage.py runserver
```

#### Для доступа в админ панель необходимо создать учетную запись:
```
python manage.py createsuperuser
```

Запуск используя Docker
------

```
docker pull simonlendev/paymentapp:latest
docker run -d -p 8000:8000 --rm --name simonapp simonlendev/paymentapp
```

Сервис
------

* `http://localhost:8000/admin/` - Панель администратора
* `http://localhost:8000/item/<item_id>` - Страница товара (в тестовой версии доступны <item_id> от 1 до 3)
* `http://localhost:8000/buy/<item_id>` - Купить товар
