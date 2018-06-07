FROM ubuntu:16.04  
MAINTAINER dsk <393573645@qq.com>  
  
ENV TZ="Asia/Shanghai"  
RUN apt-get update  
RUN apt-get install -y apt-utils  
RUN apt-get install -y language-pack-en-base  
RUN locale-gen en_US.UTF-8  
  
RUN apt-get install -y software-properties-common  
RUN LC_ALL=en_US.UTF-8 add-apt-repository ppa:ondrej/php  
RUN apt-get update  
  
RUN apt-get install -y vim nginx python python-pip python-dev build-essential
\  
php7.1 php7.1-redis php7.1-mcrypt php7.1-fpm php7.1-mysql php7.1-curl
php7.1-xml \  
php7.1-zip php7.1-intl php7.1-gmp php7.1-mbstring php7.1-amqp php7.1-opcache
php7.1-soap php7.1-gd redis-server;  
  
RUN pip install --upgrade pip; pip --version;  
  
RUN pip install supervisor;  
  
RUN echo_supervisord_conf > /etc/supervisord.conf;  
  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/7.1/fpm/php-
fpm.conf  
  
RUN sed -i -e "s/nodaemon=false/nodaemon=true/g" /etc/supervisord.conf  
  
RUN echo "files = /config/supervisor/*.conf" >> /etc/supervisord.conf  
  
RUN sed -i -e "s/;\\[include\\]/\\[include\\]/g" /etc/supervisord.conf  
  
RUN mkdir /run/php/  
  
WORKDIR /root

