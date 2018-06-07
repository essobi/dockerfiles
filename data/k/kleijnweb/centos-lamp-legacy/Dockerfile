FROM centos:7  
MAINTAINER John Kleijn <john@kleijnweb.nl>  
RUN yum -y install wget && wget
http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-5.noarch.rpm  
RUN rpm -ivh epel-release-7-5.noarch.rpm  
RUN yum -y install tar git httpd php php-cli php-mysql php-ldap php-memcache
php-curl php-xml php-soap php-devel php-pear \  
php-mbstring php-mysql php-ldap memcached php-memcache php-devel php-pear php-
pecl-memcached php-gd  
RUN yum clean all  
RUN wget -qO- https://getcomposer.org/installer | php -- --filename=composer
--install-dir=/usr/local/sbin  

