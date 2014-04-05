FROM ubuntu:12.10
MAINTAINER Corey Burmeister "burmeister.corey@gmail.com"

RUN sed -i 's/main$/main universe/' /etc/apt/sources.list && apt-get update
RUN apt-get install -y python-pip
RUN apt-get install -y build-essential
RUN apt-get install -y python-dev
RUN apt-get install -y libpq-dev 

RUN pip install Flask==0.10.1
RUN pip install Flask-SQLAlchemy==1.0
RUN pip install gunicorn==18.0
RUN pip install redis==2.8.0
RUN pip install python-memcached==1.53
RUN pip install psycopg2==2.5.2

ADD . /test_app

WORKDIR /test_app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "test_app:app"]
