FROM fernandoe/docker-python:0.0.2  
MAINTAINER Fernando Espíndola <fer.esp@gmail.com>  
  
RUN apt-get update && apt-get upgrade -y  
  
RUN apt-get -y install mysql-client  
RUN apt-get -y install mongodb-clients  
  
RUN apt-get -y autoremove  
RUN apt-get -y autoclean  
RUN apt-get -y clean  
  
ADD ./sandbox/requirements /requirements  
ADD ./source /app  
  
RUN pip install -r /requirements/production.txt  
  
CMD python manage.py runserver 0.0.0.0:8000  
  
WORKDIR /app  

