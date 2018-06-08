# Master image  
FROM centos:7  
MAINTAINER sawada@stanfoot.com  
  
WORKDIR /root  
  
# Base package  
RUN yum -y update \  
&& yum -y install libxml2 libxml2-devel libcurl-devel libjpeg-turbo-devel
libpng-devel libmcrypt-devel readline-devel libtidy-devel libxslt-devel gcc
make ImageMagick-devel \  
&& yum install -y git zip unzip openssl-devel curl-devel wget \  
&& yum install -y ImageMagick \  
# Install Nginx  
&& rpm -ivh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-
centos-7-0.el7.ngx.noarch.rpm \  
&& yum -y update nginx-release-centos \  
&& yum -y --enablerepo=nginx install nginx \  
&& systemctl enable nginx \  
# Install PHP7.2  
&& rpm --import https://rpms.remirepo.net/RPM-GPG-KEY-remi \  
&& yum install yum-utils https://rpms.remirepo.net/enterprise/remi-
release-7.rpm -y \  
&& yum-config-manager --enable remi-php72 \  
&& yum -y install php php-fpm php-intl php-mbstring php-xml php-pdo php-
mysqlnd php-opcache php-mcrypt php-gd php-devel php-zip php-pgsql \  
&& yum install -y php-pear \  
&& pecl install imagick \  
  
# Clean Cache  
RUN yum clean all -y  
  
# Install Laravel newest version  
RUN curl -s http://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
RUN systemctl enable php-fpm  
COPY ./www.conf /etc/php-fpm.d/www.conf  
COPY php.ini /etc/php.ini  
COPY vhost.conf /etc/nginx/conf.d/default.conf  
  
WORKDIR /var/www/html  
EXPOSE 80  

