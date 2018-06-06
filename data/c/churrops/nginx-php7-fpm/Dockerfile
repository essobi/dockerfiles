FROM ubuntu:16.04  
LABEL maintainer="florianocomercial@gmail.com"  
  
RUN apt-get update && apt-get install python-software-properties software-
properties-common -y \  
&& add-apt-repository ppa:nginx/stable \  
&& apt-get update && apt-get install -y nginx \  
&& apt-get install -y \  
php7.0-fpm php7.0-cli \  
php7.0-gd php7.0-dev \  
php7.0-json php7.0-mysql \  
php7.0-xml php7.0-xmlrpc \  
php7.0-imap php7.0-mbstring \  
php7.0-zip wget php-redis \  
php7.0-ldap php7.0-curl php-apcu \  
  
&& rm -rf /var/lib/apt/lists/* \  
  
&& echo 'export LANG=C' >> /etc/profile \  
&& rm /etc/localtime \  
&& ln -s /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime \  
&& mkdir /run/php \  
&& rm /etc/nginx/sites-available/default \  
&& rm /etc/php/7.0/fpm/pool.d/www.conf  
  
COPY files/default /etc/nginx/sites-available/  
COPY files/www.conf /etc/php/7.0/fpm/pool.d/  
COPY files/start.sh /  
  
RUN chmod +x /start.sh  
  
ENTRYPOINT ["/start.sh"]  
  
EXPOSE 80  

