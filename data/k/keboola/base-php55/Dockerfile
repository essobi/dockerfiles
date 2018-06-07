#VERSION 1.0.0  
FROM keboola/base  
MAINTAINER Ondrej Hlavacek <ondrej.hlavacek@keboola.com>  
  
# Image setup  
WORKDIR /tmp  
RUN rpm -Uvh https://mirror.webtatic.com/yum/el6/latest.rpm  
RUN rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-7.rpm  
RUN yum -y --enablerepo=epel,remi,remi-php55 upgrade  
RUN yum -y --enablerepo=epel,remi,remi-php55 install \  
git \  
php \  
php-cli \  
php-common \  
php-mbstring \  
php-pdo \  
php-xml  
RUN echo "date.timezone=UTC" >> /etc/php.ini  
RUN echo "memory_limit = -1" >> /etc/php.ini  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  

