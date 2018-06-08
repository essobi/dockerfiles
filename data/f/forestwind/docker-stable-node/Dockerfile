#############################################  
## fw/docker/2_stable/node ###  
#############################################  
## Оглавление  
##  
## 1. Базовый образ и разработчики  
## 2. Подавить сообщения error/warning от upstart  
## 3. Дать контейнеру знать об отсутствии tty  
## 4. Затереть скрипт /usr/sbin/policy-rc.d  
## 5. Обновить все присутствующие пакеты  
## 6. Установить bower и gulp глобально  
## 7. Установить необходимые пакеты  
## 8. Создать следующие каталоги, если они отсутствуют  
## 9. Назначить cmd по умолчанию, запускающую supervisord  
##  
  
# 1. Базовый образ и разработчики  
FROM node:6.8  
MAINTAINER Alex Malov <al.malov@gmail.com>  
  
# 2. Подавить сообщения error/warning от upstart  
RUN dpkg-divert --local --rename --add /sbin/initctl  
RUN ln -sf /bin/true /sbin/initctl  
  
# 3. Дать контейнеру знать об отсутствии tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# 4. Затереть скрипт /usr/sbin/policy-rc.d  
# - Это позволит избежать появления ошибки: invoke-rc.d: policy-rc.d denied
execution of start  
# - Подробнее см.здесь: https://habrahabr.ru/post/247903/  
RUN echo "#!/bin/sh\nexit 0" > /usr/sbin/policy-rc.d  
  
# 5. Обновить все присутствующие пакеты, установить дополнительные  
RUN apt-get update && apt-get -y upgrade && apt-get install -y \  
  
openssh-server  
  
# 6. Установить bower и gulp глобально  
RUN npm install -g gulpjs/gulp#4.0  
RUN npm install -g bower  
  
# 7. Установить необходимые пакеты  
RUN apt-get update && apt-get install -y \  
  
curl \  
cron \  
supervisor  
  
# 8. Создать следующие каталоги, если они отсутствуют  
RUN mkdir -p /var/log/supervisor  
  
# 9. Назначить cmd по умолчанию, запускающую supervisord  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor.d/websocket.ini"]  
  
# 10. Настроить SSH-демона  
  
# 10.1. Поставить пароль админу  
RUN echo 'root:password' | chpasswd  
  
# 10.2. Разрешить root-логин без пароля по SSH к контейнеру внутри сети  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# 10.3. SSH login fix. Otherwise user is kicked off after loginи  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  

