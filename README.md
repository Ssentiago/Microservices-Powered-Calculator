# Microservices-Powered-Calculator

### Описание проекта
Данный проект представляет собой реализацию простого калькулятора, разделённого на три модуля:
* api - центральный узел, который обрабатывает запросы на реализацию математических вычислений 
  от своих клиентов
* web-application - клиент, веб-приложение, отображает веб-интерфейс калькулятора для пользователя
* aiogram-bot - клиент, бот платформы telegram, взаимодействует с пользователем в формате чата, 
  точно также отображает для него интерфейс для взаимодействия с калькулятором

Проект задумывался как учебный. Его основная цель - это познакомиться с базовыми основами разделения составных частей проекта на независимые модули и с их контейнеризацией при помощи docker, а также оркестрацией посредством docker-compose

### Технологии
Backend: Python, FastAPI
Frontend: HTML, JS, Node JS
Build and Development: Docker, Docker-Compose

### Установка 
* git clone https://github.com/Ssentiago/Microservices-Powered-Calculator
* cd Microservices-Powered-Calculator
* docker-compose up -d

### Как пользоваться
Прежде всего, убедитесь, что вы перешли по пути aiogram_bot/src/config и переименовали файл .
env_example на .env. Вам понадобится получить ваш собственный токен botfather и поместить его 
внутрь .env так, как это показано в .env_example.

Ссылка для получения токена: https://t.me/botfather

После выполнения этого шага, выполните шаги из блока по установке, а затем, убедившись, что 
контейнеры успешно запущены и работают, перейдите в браузере по адресу 127.0.0.1:3000, чтобы 
открыть страницу веб-приложения. Также вы можете воспользоваться вашим ботом, если вставили его 
токен в .env - просто откройте диалог с ним и введите команду /start

### Требования
Используемые версии:
* Docker v26.1.3
* Docker-compose v2.27.1