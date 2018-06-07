FROM php:5.6-apache  
  
MAINTAINER Damien Roch, damien.roch@gmail.com  
  
# Enable apache rewrite module  
RUN ln -s /etc/apache2/mods-available/rewrite.load /etc/apache2/mods-enabled/  
  
# Install Composer  
RUN mkdir -p /usr/local/bin && php -r
"readfile('https://getcomposer.org/installer');" | php \  
&& mv composer.phar /usr/local/bin/composer  
  
# Copy PHP configuration file  
COPY build/php.ini /usr/local/etc/php/  
  
# Install utils  
RUN apt-get update && apt-get install -y unzip curl git  
  
# Install Gearman UI from source on github  
RUN curl -L https://github.com/gaspaio/gearmanui/archive/master.zip -o
/tmp/gearmanui.zip \  
&& unzip -uo /tmp/gearmanui.zip -d /tmp/gearmanui \  
&& mv /tmp/gearmanui/gearmanui-master /gearmanui \  
&& rm -Rf /tmp/gearmanui.zip /tmp/gearmanui \  
&& rm -Rf /var/www/html \  
&& ln -s /gearmanui/web /var/www/html  
  
# Copy default Gearman UI configuration file  
COPY build/config.yml /gearmanui/config.yml  
  
# Install Gearman UI PHP Dependencies with Composer  
WORKDIR /gearmanui  
RUN composer install  
  
# Install frontend assets  
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash - && apt-get install
-y nodejs && npm install -g bower && bower install --allow-root && rm -rf
/usr/lib/node_modules && apt-get remove -y nodejs && apt-get autoremove -y  
  
# Fix log file permissions  
RUN chown www-data:www-data /gearmanui/logs  

