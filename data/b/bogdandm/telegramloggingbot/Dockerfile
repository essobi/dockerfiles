FROM python:3.6  
MAINTAINER Bogdan Kalashnikov <bogdan.dm1995@yandex.ru>  
ARG CONFIG_BUILD_PATH=./config_docker.json  
ENV TERM=xterm  
  
RUN pip install git+https://github.com/bogdandm/telegram-logging-bot.git
--upgrade # v0.2.1  
ADD $CONFIG_BUILD_PATH /tmp/config.json  
ENV CONFIG_PATH=/tmp/config.json  

