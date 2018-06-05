FROM python:3.6.2  
LABEL MAINTAINER="egoz67@gmail.com"  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ADD ./requirements.txt /usr/src/app/requirements.txt  
  
RUN pip install -r requirements.txt  
  
ADD . /usr/src/app  
  
CMD python manage.py runserver

