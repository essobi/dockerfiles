FROM ubuntu:14.04  
# Переключаем Ubuntu в неинтерактивный режим — чтобы избежать лишних запросов  
ENV DEBIAN_FRONTEND noninteractive  
# Устанавливаем локаль  
RUN locale-gen en_US.UTF-8  
RUN export LANG=en_US.UTF-8  
RUN apt-get update  
# Добавляем необходимые репозитарии и устанавливаем пакеты  
RUN apt-get install -y software-properties-common  
RUN apt-get install -y wget  
RUN add-apt-repository "deb http://apt.postgresql.org/pub/repos/apt/ trusty-
pgdg main"  
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc |
apt-key add -  
RUN add-apt-repository -y ppa:nginx/stable  
RUN apt-get update  
RUN apt-get install -y wget curl supervisor nginx mc htop nano iftop git vim
postgresql-9.6 rabbitmq-server  
  
EXPOSE 80  
EXPOSE 5432  
ENTRYPOINT service nginx start && service postgresql start && service
rabbitmq-server start && bash

