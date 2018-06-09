FROM ubuntu:16.04  
MAINTAINER KreativeDev <dev@kreativedev.com>  
  
ADD ./supervisor-superiormagento.conf /etc/supervisor/conf.d/supervisor-
superiormagento.conf  
  
RUN apt-get update && apt-get install -y build-essential git vim curl nginx
libmariadb-client-lgpl-dev php7.0-fpm php7.0-mysql php7.0-common php7.0-gd
php7.0-json php7.0-cli php7.0-curl php7.0-simplexml php7.0-xml php7.0-dom
php7.0-gd supervisor  
  
ADD ./nginx.conf /etc/nginx/nginx.conf  
ADD ./fastcgi_params /etc/nginx/fastcgi_params  
  
ADD ./nginx-superiormagento.conf /etc/nginx/conf.d/nginx-superiormagento.conf  
RUN rm /etc/nginx/sites-enabled/default  
ADD ./www.conf /etc/php/7.0/fpm/pool.d/www.conf  
RUN mkdir -p /run/php/  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
CMD ["supervisord", "-n"]  
  

