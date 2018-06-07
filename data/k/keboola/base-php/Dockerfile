FROM keboola/base  
MAINTAINER Ondrej Hlavacek <ondrej.hlavacek@keboola.com>  
  
ENV APP_VERSION 1.0.1  
# Image setup  
WORKDIR /tmp  
RUN yum -y update && \  
yum -y --enablerepo=epel,remi,remi-php55 install \  
php \  
php-cli \  
php-common \  
php-mbstring \  
php-pdo \  
php-xml  
RUN echo "date.timezone=UTC" >> /etc/php.ini  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  

