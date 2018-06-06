FROM ubuntu:14.04  
MAINTAINER Vladimir Demidov "uncojet@gmail.com"  
RUN update-locale LANG=C.UTF-8 LC_MESSAGES=POSIX  
  
RUN apt-get update && apt-get install -y git  
RUN apt-get -y dist-upgrade  
RUN apt-get install -y curl  
  
RUN curl https://install.meteor.com/ | sh  
  
#Добавим ключ  
RUN mkdir -p /root/.ssh  
RUN mkdir -p /root/check  
  
#Создадим known_hosts  
RUN touch /root/.ssh/known_hosts  
  
#копируем репозиторий  
RUN meteor create myapp  
  
WORKDIR /root/myapp  
  
EXPOSE 3000  
CMD [ "meteor" ]  
  

