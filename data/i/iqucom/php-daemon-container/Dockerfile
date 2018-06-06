FROM php:7-fpm  
  
MAINTAINER mauricio.van.der.maesen@iqu.com  
  
# Dependencies  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get autoremove -y \  
&& apt-get install -y git wget nano libmcrypt-dev libpng12-dev libjpeg-dev
libpq-dev curl phing libxml2-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install mcrypt gd mbstring zip soap \  
&& pear install --alldeps Mail \  
&& rm -rf /tmp/pear  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"  
RUN php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'669656bab3166a7aff8a7506b8cb2d1c292f042046c5a994c43155c0be6190fa0355160742ab2e1c88d40d5be660b410')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;"  
RUN php composer-setup.php  
RUN php -r "unlink('composer-setup.php');"  
RUN mv composer.phar /usr/local/bin/composer  
  
# PCNTL extension  
RUN git clone https://github.com/php/php-src.git && \  
cd php-src/ext/pcntl/ && \  
phpize && ./configure && make install  
  
## NEW RELIC  
RUN wget -O - https://download.newrelic.com/548C16BF.gpg | apt-key add -  
RUN sh -c 'echo "deb http://apt.newrelic.com/debian/ newrelic non-free" >
/etc/apt/sources.list.d/newrelic.list'  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install newrelic-php5 newrelic-
sysmond  
RUN /usr/sbin/update-rc.d newrelic-daemon defaults 90 10  
RUN /usr/sbin/update-rc.d newrelic-daemon enable  
  
# PHP configuration files  
RUN touch /usr/local/etc/php/php.ini  
RUN echo "extension=pcntl.so" >> /usr/local/etc/php/php.ini

