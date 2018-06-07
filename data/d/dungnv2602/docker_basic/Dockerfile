FROM ubuntu:16.04  
MAINTAINER DungNguyen<dungnv2602@gmail.com>  
RUN apt-get update  
RUN apt-get install -y nginx  
RUN apt-get install -y apt-transport-https ca-certificates curl software-
properties-common  
RUN mkdir venv  
ADD start.sh /venv  
WORKDIR /venv  
RUN chmod a+x /venv/*  
ENTRYPOINT ["/venv/start.sh"]  
EXPOSE 80

