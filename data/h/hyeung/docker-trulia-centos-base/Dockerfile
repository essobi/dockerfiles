# FE apache php base container  
# base off of ubuntu for now  
FROM centos:centos6  
  
MAINTAINER Hinling Yeung  
  
# Update the default application repository sources list  
RUN yum -y update  
  
# Install apache2  
RUN yum install -y httpd  
  
# helper tools  
RUN yum -y install telnet  
RUN yum -y install wget  
  
# Install php  
RUN yum -y install php libapache2-mod-php5 php-dev  
  
# Install mysql client  
RUN yum -y install libapache2-mod-auth-mysql php-mysql php-devel mysql-client  
  
# Install PEAR  
RUN yum -y install php-pear  
  
# Install phpmods  
RUN pear upgrade --force pear  
RUN printf "no\n" | pecl install stomp-1.0.5  
RUN yum -y install pcre-devel  
RUN yum -y install pkgconfig  
# install apc  
RUN yum -y install gcc  
RUN pecl install APC  
RUN yum -y install php-pecl-apc  
RUN pecl install xdebug  
  
# Install apache libs  
RUN yum -y install httpd-devel httpd-manual.noarch  
  
# Install all the php libraries  
RUN yum -y install php-common php-cli  
RUN yum -y install php-gd  
  
# install php-mcrypt  
RUN wget http://dl.fedoraproject.org/pub/epel/6/x86_64/php-
mcrypt-5.3.3-3.el6.x86_64.rpm  
RUN wget
http://dl.fedoraproject.org/pub/epel/6/x86_64/libmcrypt-2.5.8-9.el6.x86_64.rpm  
RUN yum -y localinstall php-mcrypt-5.3.3-3.el6.x86_64.rpm
libmcrypt-2.5.8-9.el6.x86_64.rpm  
  
RUN yum -y install php-curl  
RUN yum -y install libmemcached  
RUN yum -y install libmemcached-devel  
RUN yum -y install php-pecl-memcache  
  
# configure apache  
ADD apache_config/httpd.conf /etc/httpd/conf/httpd.conf  
  
# Create smarty dir  
RUN mkdir -p /data/smarty  
RUN chgrp -R apache /data/smarty  
RUN chmod -R 770 /data/smarty  
  
# Grant permisson for writing session info  
RUN chgrp -R apache /var/lib/php  
RUN chmod -R 770 /var/lib/php  
  

