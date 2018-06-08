FROM centos:centos6  
  
MAINTAINER PhuongDTQ dau.phuong@rivercrane.vn  
  
#Install repository  
RUN yum -y localinstall http://dl.fedoraproject.org/pub/epel/6/i386/epel-
release-6-8.noarch.rpm  
RUN yum -y localinstall http://rpms.famillecollet.com/enterprise/remi-
release-6.rpm  
  
#Add user: webike  
RUN useradd -m webike  
  
#Add C/C++ install  
RUN yum install -y gcc  
  
#Install Apache  
RUN yum install -y httpd  
  
# Install node.js:  
RUN yum install -y nodejs npm --enablerepo=epel libcurl-devel libxml2-devel
mod_ssl pcre-devel  
  
# Install gulp globally  
RUN npm install -y gulp -g  
  
# Install bower  
RUN npm install -g bower  
  
#Intall PHP 5.5  
RUN yum install -y --enablerepo=remi,remi-php56 php php-mysql php-pear php-gd
php-mcrypt php-ldap php-xcache php-devel php-mbstring php-pdo php-pecl-xdebug
php-pecl-memcache php-xml php-process libcurl-devel libxml2-devel mod_ssl
pcre-devel libtool  
  
#Install Composer  
RUN curl -k -sS https://getcomposer.org/installer | php && mv composer.phar
/usr/local/bin/composer  
  
#Install Memcache  
RUN yum install -y memcached  
  
#Copy httpd.conf from Host to Container  
ADD config/httpd.conf /etc/httpd/conf/httpd.conf  
ADD config/php.ini /etc/php.ini  
ADD config/server.crt /etc/httpd/conf/server.crt  
ADD config/server.key /etc/httpd/conf/server.key  
ADD config/mime.types /etc/httpd/conf/mime.types  
ADD config/ssl.conf /etc/httpd/conf/ssl.conf  
  
#Create php-info file  
RUN echo "<?php phpinfo(); ?>" > /var/www/html/phpinfo.php  
  
#Clean yum cache  
RUN yum clean -y all  
  
#Run service memcached  
RUN service memcached start  
  
#Open port 80,443  
EXPOSE 80 443

