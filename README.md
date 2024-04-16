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
1) Install nginx
2) Install docker
3) Instal gunicorn
4) Git clone
5) Create demon gunicorn
6) Run demon
7) Install settings for nginx
8) Check ports
9) Docker-compose build in .
10) Docker up
11) Docker-compose exec app python manage.py migrate
