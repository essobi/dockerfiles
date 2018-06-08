FROM ubuntu-upstart:14.04  
  
MAINTAINER Dries De Peuter <dries@nousefreak.be>  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com \--recv-keys C300EE8C \  
&& echo "deb http://ppa.launchpad.net/nginx/development/ubuntu trusty main" >
/etc/apt/sources.list.d/nginx.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com \--recv-keys E5267A6C \  
&& echo "deb http://ppa.launchpad.net/ondrej/php5-5.6/ubuntu trusty main" >
/etc/apt/sources.list.d/php.list  
  
RUN apt-get update \  
&& apt-get install -y \  
curl \  
git \  
nginx \  
php5-fpm \  
php5-cli \  
php5-mysql \  
&& apt-get clean  
  
COPY conf/init.nginx.conf /etc/init/nginx.conf  
#COPY conf/init.php-fpm.conf /etc/init/php-fpm.conf  
COPY conf/nginx.conf /etc/nginx/sites-enabled/default  
#COPY conf/php.pool.conf /usr/local/php/etc/php-fpm.d/www.conf  
  
COPY index.php /var/www/html/index.php  
RUN rm /var/www/html/index.nginx-debian.html  
  
WORKDIR /var/www/html  
  
EXPOSE 80  

