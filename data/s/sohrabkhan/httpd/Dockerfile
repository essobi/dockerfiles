FROM php:5.6-apache  
MAINTAINER Sohrab Khan <sohrab@sohrabkhan.com>  
  
# Install IonCube Loader  
RUN apt-get update && apt-get upgrade -yqq  
RUN apt-get install -y wget  
RUN wget
http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz  
RUN tar zxvf ioncube_loaders_lin_x86-64.tar.gz  
RUN mv ioncube/ioncube_loader_lin_5.6.so /usr/local/lib/php/extensions/no-
debug-non-zts-20131226/  
RUN touch /usr/local/etc/php/conf.d/ioncube.ini && echo
"zend_extension=ioncube_loader_lin_5.6.so" >>
/usr/local/etc/php/conf.d/ioncube.ini  
  
# Install xDebug  
RUN pecl install xdebug  
RUN touch /usr/local/etc/php/conf.d/xdebug.ini && echo
'zend_extension=xdebug.so \n xdebug.remote_enable=1 \n
xdebug.profiler_enable=1 \n xdebug.profiler_output_dir="/var/xdebug_profiler"'
>> /usr/local/etc/php/conf.d/xdebug.ini  
  
# Install Sass  
RUN apt-get install -y rubygems  
RUN su -c "gem install sass"  
  
RUN wget https://getcomposer.org/composer.phar  
RUN mv composer.phar /usr/local/bin/composer  
  
RUN docker-php-ext-install -j$(nproc) mysqli pdo pdo_mysql mbstring mysql  
RUN apt-get install -y php5-gd  
RUN a2enmod rewrite  
ADD public_html/ /var/www/html/  
ADD custom.conf /etc/apache2/sites-available/custom.conf  
RUN mkdir /var/xdebug_profiler  
  
#RUN composer install  
EXPOSE 80  

