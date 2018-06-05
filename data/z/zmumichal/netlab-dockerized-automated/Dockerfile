FROM docker:1.11.1  
MAINTAINER zmu.michal@gmail.com  
RUN echo "@testing http://dl-4.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && apk update && apk add python py-pip bash python-dev  
RUN pip install docker-compose  
ENV PYTHONUNBUFFERED 1  
RUN mkdir /code  
WORKDIR /code  
ADD requirements.txt /code/  
RUN pip install -r requirements.txt  
ADD . /code/  
CMD python manage.py runserver 0.0.0.0:80

