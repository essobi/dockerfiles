FROM python:3  
ENV PYTHONUNBUFFERED 1  
RUN mkdir /code  
RUN apt-get update && apt-get install gettext cron libz-dev libjpeg-dev
libfreetype6-dev python-dev -y  
WORKDIR /code  
ADD requirements.txt /code/  
RUN pip install -r requirements.txt  
ADD . /code/  

