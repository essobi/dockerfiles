FROM debian:stretch  
MAINTAINER Michael J. Stealey < michael.j.stealey@gmail.com>  
  
RUN apt-get update && apt-get upgrade -y && apt-get install -y \  
php7.0 \  
libapache2-mod-php7.0 \  
php7.0-mcrypt \  
php7.0-mysql \  
php7.0-gd \  
php7.0-curl \  
php7.0-mbstring \  
php7.0-xml \  
php7.0-zip \  
openssl \  
wget \  
unzip \  
sudo  
  
RUN wget https://github.com/getgrav/grav/releases/download/1.3.0-rc.4/grav-
admin-v1.3.0-rc.4.zip \  
&& mkdir -p /var/www/html/ \  
&& cd /var/www/html/ \  
&& unzip /grav-admin-v1.3.0-rc.4.zip \  
&& cd grav-admin \  
&& cp -a * .. \  
&& cp .htaccess .. \  
&& rm -f index.html \  
&& chown -R www-data: /var/www/html/  
  
ADD docker-entrypoint.sh /docker-entrypoint.sh  
  
ENV SERVERADMIN=admin@localhost  
ENV SERVERNAME=localhost  
ENV SERVERALIAS=localhost  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["run"]  

