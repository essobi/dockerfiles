# Set the base image  
FROM ubuntu:trusty  
ENV LANG en_US.UTF-8  
  
# Dockerfile author / maintainer  
MAINTAINER spencdev tyler@tierblue.com  
# Update application repository list and install packages  
RUN locale-gen "en_US.UTF-8" && export LANG=C.UTF-8  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y apt-
transport-https curl git unzip  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y software-properties-
common && add-apt-repository ppa:ondrej/php && apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes php7.1 php-
common php-intl php-mbstring php-mysql php-curl php-zip  
RUN echo "mysql-server-5.6 mysql-server/root_password password test"  
RUN echo "mysql-server-5.6 mysql-server/root_password_again password test"  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install mysql-server-5.6  
RUN service mysql restart  
# COMPOSER INSTALL  
RUN php -r "copy('https://getcomposer.org/installer', '/tmp/composer-
setup.php');"  
RUN php /tmp/composer-setup.php \--install-dir=/usr/local/bin
\--filename=composer  
RUN composer self-update

