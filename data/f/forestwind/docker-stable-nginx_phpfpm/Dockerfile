#############################################  
## fw/docker/2_stable/nginx_phpfpm ###  
#############################################  
## Оглавление  
##  
## 1. Базовый образ и разработчики  
## 2. Подавить сообщения error/warning от upstart  
## 3. Дать контейнеру знать об отсутствии tty  
## 4. Затереть скрипт /usr/sbin/policy-rc.d  
## 5. Обновить все присутствующие пакеты  
## 6. Установить необходимые пакеты  
## 7. Создать следующие каталоги, если они отсутствуют  
## 8. Удалить конфиги nginx и php  
## 9. Сделать expose портов 80 и 443  
## 10. Добавить скрипт bootstrap.sh в образ  
## 11. Назначить cmd по умолчанию  
## 12. Установить composer  
## 13. Подготовить ведение логов для postfix  
##  
# 1. Базовый образ и разработчики  
FROM ubuntu:16.04  
MAINTAINER Alex Malov <al.malov@gmail.com>  
  
# 2. Подавить сообщения error/warning от upstart  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -sf /bin/true /sbin/initctl  
  
# 3. Дать контейнеру знать об отсутствии tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# 4. Затереть скрипт /usr/sbin/policy-rc.d  
# - Это позволит избежать появления ошибки: invoke-rc.d: policy-rc.d denied
execution of start  
# - Подробнее см.здесь: https://habrahabr.ru/post/247903/  
RUN echo "#!/bin/sh\nexit 0" > /usr/sbin/policy-rc.d  
  
# 5. Обновить все присутствующие пакеты  
RUN apt-get update && apt-get -y upgrade  
  
# 6. Установить необходимые пакеты  
# 6.1. Если нужен лог для postfix, раскомментируй и пересобери этот образ  
# - Внимание! Этот лог может стать огромным со временем, применяй лишь для
отладки.  
# - Лог будет находиться в other/logs/mail.log  
RUN apt-get update && apt-get install -y syslog-ng syslog-ng-core; exit 0  
  
# 6.2. Установить пакеты  
RUN apt-get update && apt-get install -y \  
  
curl \  
cron \  
supervisor \  
nginx \  
php7.0 php7.0-fpm php7.0-gmp php7.0-mbstring php7.0-zip \  
git \  
php7.0-mysql \  
php7.0-curl \  
php7.0-gd \  
php7.0-intl \  
php7.0-mcrypt \  
php7.0-sqlite \  
php7.0-tidy \  
php7.0-xmlrpc \  
php7.0-xsl \  
php7.0-pgsql \  
php7.0-ldap \  
pwgen \  
sshpass \  
git-all \  
mailutils \  
nano \  
php7.0-bcmath \  
; exit 0  
# 7. Создать следующие каталоги, если они отсутствуют  
RUN mkdir -p /etc/nginx  
RUN mkdir -p /var/log/supervisor  
RUN mkdir -p /var/run/php-fpm  
  
# 8. Удалить конфиги nginx и php  
# - А добавляться конфиги будет в compose-проекте  
RUN rm /etc/nginx/nginx.conf  
RUN rm /etc/php/7.0/fpm/php.ini  
  
# 9. Сделать expose портов 80 и 443  
EXPOSE 80  
EXPOSE 443  
EXPOSE 25  
EXPOSE 587  
EXPOSE 465  
EXPOSE 993  
EXPOSE 143  
EXPOSE 110  
EXPOSE 995  
# 10. Добавить скрипт bootstrap.sh в образ  
# ADD bootstrap.sh /opt/bootstrap.sh  
# RUN chmod +x /opt/bootstrap.sh  
# 11. Назначить cmd по умолчанию  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor.d/supervisor.ini"]  
  
# 12. Установить composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer  
  
# 13. Подготовить ведение логов для postfix  
# 13.1. Replace the system() source because inside Docker we can't access
/proc/kmsg.  
# https://groups.google.com/forum/#!topic/docker-user/446yoB0Vx6w  
RUN sed -i -E 's/^(\s*)system\\(\\);/\1unix-stream("\/dev\/log");/'
/etc/syslog-ng/syslog-ng.conf  
  
# 13.2. Uncomment 'SYSLOGNG_OPTS="--no-caps"' to avoid the following warning:  
# syslog-ng: Error setting capabilities, capability management disabled;
error='Operation not permitted'  
# http://serverfault.com/questions/524518/error-setting-capabilities-
capability-management-disabled#  
RUN sed -i 's/^#\\(SYSLOGNG_OPTS="--no-caps"\\)/\1/g' /etc/default/syslog-ng  
  

