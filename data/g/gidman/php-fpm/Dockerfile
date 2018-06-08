FROM ubuntu:xenial  
  
MAINTAINER Karabutin Alex <karabutinalex@gmail.com>  
  
RUN apt-get update && \  
apt-get -y install \  
software-properties-common \  
language-pack-en-base \  
wget && \  
LC_ALL=C.UTF-8 add-apt-repository -y ppa:ondrej/php && \  
apt-get update && \  
apt-get -y install \  
php5.6-cli \  
php5.6-fpm \  
php5.6-xml \  
php5.6-mongo \  
php5.6-xdebug \  
php5.6-mbstring \  
php5.6-mcrypt \  
php5.6-curl && \  
useradd -ms /bin/bash php-fpm && \  
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \  
php composer-setup.php --quiet && \  
rm composer-setup.php && \  
mv composer.phar /usr/local/bin/composer && \  
echo 'deb http://apt.newrelic.com/debian/ newrelic non-free' | tee
/etc/apt/sources.list.d/newrelic.list && \  
wget -O- https://download.newrelic.com/548C16BF.gpg | apt-key add \- && \  
apt-get update && \  
echo newrelic-php5 newrelic-php5/application-name string "NR_APP_NAME" |
debconf-set-selections && \  
echo newrelic-php5 newrelic-php5/license-key string "NR_LICENSE_KEY" |
debconf-set-selections && \  
apt-get -y install \  
newrelic-php5  
  
COPY config/php-fpm.ini /etc/php/5.6/fpm/php.ini  
COPY config/php-fpm.conf /etc/php/5.6/fpm/php-fpm.conf  
COPY config/php-fpm.www.conf /etc/php/5.6/fpm/pool.d/www.conf  
COPY entrypoint.sh /entrypoint.sh  
  
ENV NR_APP_NAME app-name  
ENV NR_LICENSE_KEY license-key  
  
EXPOSE 9000  
  
CMD ["/bin/bash", "/entrypoint.sh"]  

