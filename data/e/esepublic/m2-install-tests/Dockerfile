FROM ubuntu:14.04  
MAINTAINER Keith Bentrup <kbentrup@magento.com>  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes \  
mysql-server-5.6 \  
apache2 \  
libapache2-mod-php5 \  
php5-common \  
php5-gd \  
php5-mysql \  
php5-mcrypt \  
php5-curl \  
php5-intl \  
php5-xsl \  
git \  
curl  
  
RUN php5enmod mcrypt && \  
a2enmod headers ssl substitute && \  
curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer  
  
RUN git clone https://github.com/magento/magento2.git && \  
git clone https://github.com/magento/magento2-sample-data.git && \  
cp -rf magento2-sample-data/* magento2/  
  
COPY apache2-magento.conf /etc/apache2/sites-enabled/000-default.conf  
  
COPY install-m2.sh /  
CMD /install-m2.sh  

