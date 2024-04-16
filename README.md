# Context
In 2018, James Clear wrote the book Atomic Habits, which is about acquiring new good habits and eradicating old bad habits.
In the book, a good example of a habit is described as a specific action that can be summarized in one sentence:
I will be [ACTIVE] at [TIME] at [PLACE]
For every useful habit you need to reward yourself or immediately after do a pleasant habit. But at the same time, the habit should not take more than two minutes to complete.


# Dependencies
- python = "^3.10"
- django = "4.2.7"
- psycopg2-binary = "^2.9.9"
- python-dotenv = "^1.0.1"
- djangorestframework = "^3.14.0"
- djangorestframework-simplejwt = "^5.3.1"
- ipython = "^8.22.1"
- celery = "^5.3.6"
- django-celery-beat = "^2.6.0"
- redis = "^5.0.3"
- requests = "^2.31.0"
- coverage = "^7.4.4"
- django-cors-headers = "^4.3.1"
- drf-yasg = "^1.21.7"


# Deploy
2) Install nginx
3) Install docker
4) Instal gunicorn
5) Git clone
6) Create demon gunicorn
7) Run demon
8) Install settings for nginx
9) Check ports
10) Docker-compose build in .
11) Docker up
12) Docker-compose exec app python manage.py migrate
