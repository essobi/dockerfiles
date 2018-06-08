FROM ubuntu:14.04  
# Переключаем Ubuntu в неинтерактивный режим — чтобы избежать лишних запросов  
ENV DEBIAN_FRONTEND noninteractive  
# Устанавливаем локаль  
RUN locale-gen en_US.UTF-8  
RUN export LANG=en_US.UTF-8  
RUN apt-get update  
# Добавляем необходимые репозитарии и устанавливаем пакеты  
RUN apt-get install -y software-properties-common  
RUN add-apt-repository -y ppa:ondrej/php  
RUN add-apt-repository -y ppa:nginx/stable  
RUN add-apt-repository ppa:chris-lea/redis-server  
RUN sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
4F4EA0AAE5267A6C  
RUN apt-get update  
RUN apt-get install -y wget curl php5 php5-common  
RUN apt-get install -y php5-fpm php5-mysql php5-gd php5-curl php5-mcrypt
php5-imagick php5-intl php5-xsl php5-xcache php5-xmlrpc php5-redis supervisor
nginx mc htop nano iftop git vim redis-server  
RUN rm -Rf /etc/nginx/sites-enabled/default  
  
#ENV MYSQL_USER=mysql \  
# MYSQL_DATA_DIR=/var/lib/mysql \  
# MYSQL_RUN_DIR=/run/mysqld \  
# MYSQL_LOG_DIR=/var/log/mysql  
#RUN apt-get update \  
# && DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-server \  
# && rm -rf /var/lib/apt/lists/*  
#COPY entrypoint.sh /sbin/entrypoint.sh  
#RUN chmod 755 /sbin/entrypoint.sh  
EXPOSE 6379  
EXPOSE 80  
#EXPOSE 3306/tcp  
#ENTRYPOINT ["/sbin/entrypoint.sh"]  
#CMD ["/usr/bin/mysqld_safe"]  
ENV N98_MAGERUN_URL https://files.magerun.net/n98-magerun.phar  
  
RUN curl -o /usr/local/bin/n98-magerun $N98_MAGERUN_URL \  
&& chmod +x /usr/local/bin/n98-magerun  
  
RUN cd /usr/local \  
&& curl -sS https://getcomposer.org/installer | php \  
&& chmod +x /usr/local/composer.phar \  
&& ln -s /usr/local/composer.phar /usr/local/bin/composer  
  
# Добавляем описание виртуального хоста  
ADD magento.conf /etc/nginx/sites-enabled/magento.conf  
  
# Добавляем конфиг supervisor (описание процессов, которые мы хотим видеть
запущенными на этом контейнере)  
#ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY set-base-url /usr/local/bin/set-base-url  
  
# Объявляем, какой порт этот контейнер будет транслировать  
# Запускаем supervisor  
#CMD ["/usr/bin/supervisord"]  
ENTRYPOINT php5enmod mcrypt && service php5-fpm restart && service nginx start
&& service redis-server start && bash

