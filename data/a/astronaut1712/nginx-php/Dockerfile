FROM ubuntu:14.04  
MAINTAINER Quang <quang.astronaut@gmail.com>  
  
RUN apt-get install -y software-properties-common  
RUN apt-add-repository ppa:phalcon/stable  
RUN apt-get clean && apt-get update && apt-get upgrade -y && apt-get dist-
upgrade -y  
  
RUN apt-get install -y \  
php5-fpm \  
php5-gd \  
php5-mcrypt \  
php5-curl \  
php5-mysql \  
php5-phalcon \  
&& php5enmod mcrypt  
  
RUN apt-get install -y curl supervisor  
  
RUN curl -sSL http://nginx.org/keys/nginx_signing.key | apt-key add -  
RUN echo "deb http://nginx.org/packages/ubuntu/ trusty nginx\ndeb-src
http://nginx.org/packages/ubuntu/ trusty nginx" >
/etc/apt/sources.list.d/nginx.list  
RUN apt-get update \  
&& apt-get install -y nginx \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY nginx/etc /etc/nginx/  
COPY conf/supervisord.conf /etc/supervisor/conf.d/  
  
RUN sed -i "s/^listen.*/listen = \/var\/run\/php5-fpm.sock/"
/etc/php5/fpm/php-fpm.conf  
  
EXPOSE 80  
EXPOSE 443  
CMD ["/usr/bin/supervisord"]  

