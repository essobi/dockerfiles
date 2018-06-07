#  
# Ubuntu Dockerfile for Moobi  
#  
# https://gitlab.com/moobiapp/moobi-docker.git  
#  
FROM ubuntu  
  
MAINTAINER Moobi Developers  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y
software-properties-common && add-apt-repository ppa:ondrej/php && apt-get
update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --assume-yes apt-utils  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y nginx && apt-get install
-y vim && apt-get install -y net-tools && apt-get install -y curl && apt-get
install -y zip unzip && apt-get install -y php7.2 php7.2-gd php7.2-xml
php7.2-json php7.2-opcache php7.2-curl php7.2-redis php7.2-mysql
php7.2-mbstring php7.2-zip php7.2-fpm && apt-get clean  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer  
  
LABEL Description = 'Moobi System'  
  
COPY user-view.conf /etc/nginx/sites-available  
  
RUN ln -s /etc/nginx/sites-available/user-view.conf /etc/nginx/sites-enabled
&& rm /etc/nginx/sites-available/default && rm /etc/nginx/sites-
enabled/default  
  
#RUN mkdir /srv/project  
#VOLUME /srv/project  
VOLUME /data/www/user-view  
  
# Definindo o diretório app como nosso diretório de trabalho  
WORKDIR /data/www/user-view  
  
#COPY /data/www/admin-view/ /srv/project  
# Create these folders and change its permissions:  
RUN mkdir /var/nginx/ && mkdir /var/nginx/client_body_temp && mkdir
/var/nginx/proxy_temp && chown -R www-data:www-data
/var/nginx/client_body_temp/ && chown -R www-data:www-data
/var/nginx/proxy_temp/ && chmod -R 755 /data/www/user-view  
  
CMD ["nginx", "-g", "daemon off;"]  

