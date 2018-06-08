FROM ubuntu:xenial  
MAINTAINER jlelse <contact@jlelse.de>  
  
EXPOSE 80  
RUN apt-get update && \  
apt-get -y install software-properties-common && \  
LC_ALL=C.UTF-8 apt-add-repository -y ppa:ondrej/php && \  
LC_ALL=C.UTF-8 apt-add-repository -y ppa:ondrej/nginx && \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get -y install \  
nginx \  
ca-certificates \  
php7.2 php7.2-fpm php7.2-cli php7.2-json php7.2-curl php7.2-sqlite3 php7.2-xml
php7.2-zip && \  
apt-get autoremove -y && \  
apt-get autoclean -y && \  
apt-get clean -y && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV PAGEKIT_VERSION 1.0.13  
RUN mkdir /pagekit  
WORKDIR /pagekit  
VOLUME /pagekit  
  
ADD nginx.conf /etc/nginx/nginx.conf  
  
CMD ["sh", "-c", "chown -R www-data: /pagekit && service php7.2-fpm start &&
nginx"]  

