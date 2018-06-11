# Httpd with PHP  
# VERSION 1.3  
  
FROM centos:centos7  
MAINTAINER Won Xin <woxnin@gmail.com>  
  
RUN yum update -y \  
&& yum install -y epel-release \  
&& yum install -y \  
httpd \  
libjpeg* \  
php \  
php-bcmath \  
php-devel \  
php-gd \  
php-php-gettext \  
php-imap \  
php-ldap \  
php-mbstring \  
php-mcrypt \  
php-mysqlnd \  
php-pear-Net-Socket \  
php-xml \  
php-xmlrpc \  
&& yum clean all  
  
WORKDIR /var/www/html  
  
EXPOSE 80  
  
VOLUME ["/var/www/html"]  
  
CMD ["httpd", "-DFOREGROUND"]  

