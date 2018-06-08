FROM ubuntu:latest  
MAINTAINER silencej owen263@gmail.com  
  
COPY requirements.txt /home/  
RUN apt-get update && apt-get install -y python3 python3-pip python3-django-
uwsgi && pip3 install -r /home/requirements.txt  
  
VOLUME ["/home"]  
  

