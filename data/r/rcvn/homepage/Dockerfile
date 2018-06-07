FROM centos:centos6  
  
MAINTAINER RCVN duc.cnv@rivercrane.vn  
  
#Install repository  
RUN yum -y localinstall http://dl.fedoraproject.org/pub/epel/6/i386/epel-
release-6-8.noarch.rpm  
RUN yum -y localinstall http://rpms.famillecollet.com/enterprise/remi-
release-6.rpm  
  
#Add user: webike  
RUN useradd -m webike  
  
#Add C/C++ install  
RUN yum install -y gcc  
  
#Install Apache 2.4  
RUN yum install -y httpd  
  
#Intall PHP 5.4  
RUN yum install -y --enablerepo=remi php php-mysql php-pear php-gd php-mcrypt
php-ldap php-xcache php-devel php-mbstring php-pdo php-pecl-xdebug php-pecl-
memcache php-xml php-process libcurl-devel libxml2-devel mod_ssl pcre-devel  
  
#Install Composer  
RUN curl -k -sS https://getcomposer.org/installer | php && mv composer.phar
/usr/local/bin/composer  
  
#Copy httpd.conf from Host to Container  
ADD config/httpd.conf /etc/httpd/conf/httpd.conf  
ADD config/mime.types /etc/httpd/conf/mime.types  
ADD config/php.ini /etc/php.ini  
  
#Create php-info file  
RUN echo "<?php phpinfo(); ?>" > /var/www/html/phpinfo.php  
  
#Clean yum cache  
RUN yum clean -y all  
  
#Open port 80,443  
EXPOSE 80 443

