FROM ubuntu:16.04  
MAINTAINER mmaguero <maguero@correo.ugr.es>  
  
ENV PYTHONUNBUFFERED 1 RUN apt-get -y update  
  
RUN apt-get -y update && apt-get -y upgrade  
  
RUN apt-get -y install git  
  
RUN apt-get install -y python-setuptools  
RUN apt-get -y install python-dev  
RUN apt-get -y install build-essential  
RUN apt-get -y install libpq-dev  
RUN apt-get -y install python-reportlab  
RUN easy_install pip  
RUN pip install --upgrade pip  
RUN python -m pip install Flask  
RUN python -m pip install Flask-SQLAlchemy  
RUN python -m pip install pyTelegramBotAPI  
  
RUN apt-get -y install postgresql  
RUN apt-get -y install postgresql-contrib  
RUN apt-get -y install python-psycopg2  
  

