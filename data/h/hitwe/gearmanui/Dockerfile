FROM php:5.6-apache  
  
MAINTAINER Marko OS  
  
# Enable apache rewrite module  
RUN ln -s /etc/apache2/mods-available/rewrite.load /etc/apache2/mods-enabled/  
  
# Install Composer  
RUN mkdir -p /usr/local/bin && php -r
"readfile('https://getcomposer.org/installer');" | php \  
&& mv composer.phar /usr/local/bin/composer \  
&& apt-get update && apt-get install -y unzip curl git  
  
# Copy PHP configuration file  
COPY build/php.ini /usr/local/etc/php/  
  
# Install Gearman UI from source on github  
RUN curl -L https://github.com/gaspaio/gearmanui/archive/master.zip -o
/tmp/gearmanui.zip \  
&& unzip -uo /tmp/gearmanui.zip -d /tmp/gearmanui \  
&& mv /tmp/gearmanui/gearmanui-master /gearmanui \  
&& rm -Rf /var/www/html \  
&& ln -s /gearmanui/web /var/www/html  
  
# Copy default Gearman UI configuration file  
COPY build/config.yml /gearmanui/config.yml  
  
WORKDIR /gearmanui  
  
RUN composer install  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && apt-get install
-y nodejs \  
&& npm install -g bower \  
&& bower install --allow-root \  
&& apt-get remove -y nodejs && apt-get autoremove -y \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* \  
&& chown -R www-data:www-data /var/www/html  

