FROM ubuntu:16.04  
MAINTAINER Jack "564543167@qq.com"  
ENV REFRESHED_AT 2018-01-20  
RUN apt-get update -y  
RUN apt-get install -y ruby ruby-dev build-essential redis-tools  
RUN gem install --no-rdoc --no-ri sinatra json redis  
  
RUN mkdir -p /opt/webapp  
  
EXPOSE 4567  
CMD [ "/opt/webapp/bin/webapp" ]  

