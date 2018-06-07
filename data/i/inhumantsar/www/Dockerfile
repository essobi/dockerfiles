FROM centos:centos7  
MAINTAINER Shaun Martin <shaun@samsite.ca>  
  
### Declare volumes and envs  
VOLUME /var/www  
VOLUME /var/log  
  
### Install apache  
RUN yum -y install httpd  
  
### Install php  
RUN yum -y install php \  
php-fpm  
  
### Install Supervisor  
RUN yum -y install python-setuptools  
RUN easy_install supervisor  
  
### Install extra packages.  
# Doing this one group at a time for caching goodness  
RUN yum -y install php-mysql \  
php-gd \  
php-ldap \  
php-pear \  
php-xml \  
php-xmlrpc \  
php-mbstring \  
php-snmp \  
php-soap  
  
RUN yum -y install mod_fcgid  
  
# Not strictly necessary but useful in debug  
RUN yum -y install curl \  
curl-devel \  
vim  
  
### Add configs and scripts  
# First trash the defaults  
RUN rm -rf /etc/httpd /etc/php* /etc/supervisor*  
  
# Can't add with a wildcard, can't send to base dirs.  
# eg: ADD resources/etc/php* /etc/ doesn't work for both reasons.  
ADD resources/etc/httpd /etc/httpd  
ADD resources/etc/php.ini /etc/php.ini  
ADD resources/etc/php.d /etc/php.d  
ADD resources/etc/php-fpm.conf /etc/php-fpm.conf  
ADD resources/etc/php-fpm.d /etc/php-fpm.d  
ADD resources/etc/supervisord.conf /etc/supervisord.conf  
ADD resources/etc/supervisord.d /etc/supervisord.d  
ADD resources/start.sh /start.sh  
  
# Just in case  
RUN chown -R root:root /etc/httpd  
RUN chown -R root:root /etc/php*  
RUN chown -R root:root /etc/supervisord*  
RUN chmod +x /start.sh  
  
# Make sure supervisord's logdir is available  
RUN mkdir -p /var/log/supervisord  
  
# httpd.el7 expects certain symlinks  
RUN ln -s /var/log/httpd /etc/httpd/logs  
RUN ln -s /usr/lib64/httpd/modules /etc/httpd/modules  
RUN ln -s /run/httpd /etc/httpd/run  
  
CMD /start.sh  

