FROM ubuntu:14.04  
MAINTAINER Ben Dean-Kawamura <ben@pculture.org>  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python-pip python-dev
build-essential curl  
RUN pip install uwsgi  
ADD . /app  
RUN pip install -r /app/requirements.txt  
EXPOSE 5000  
USER www-data  
CMD ["/usr/local/bin/uwsgi", "--ini", "/app/.docker/app.ini"]  

