FROM centos:6  
MAINTAINER David Numan david.numan_at_civicactions.com  
  
RUN yum -y update; yum clean all  
RUN yum -y install epel-release && yum clean all  
  
RUN yum -y install git mysql wget sudo python-setuptools nano vim pv && \  
yum clean all  
  
# Install php  
RUN yum -y install php php-gd php-pdo_mysql php-xml php-soap php-mbstring php-
pear php-imap && \  
yum clean all  
  
# Install apache  
RUN yum -y install httpd mod_ssl && yum clean all  
  
# Apache config.  
RUN sed -i 's,/var/www/html,/var/www/docroot,' /etc/httpd/conf/httpd.conf  
RUN echo "Include conf/docker-host.conf" >> /etc/httpd/conf/httpd.conf  
ADD ./conf/apache2/docker-host.conf /etc/httpd/conf/docker-host.conf  
  
# PHP config.  
ADD ./conf/php5/docker-php.ini /etc/php.d/docker-php.ini  
  
# Drupal settings.  
ADD ./conf/drupal/settings.docker.php /etc/settings.docker.php  
  
# Composer.  
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
-d detect_unicode=0 && \  
ln -s /usr/bin/composer.phar /usr/bin/composer  
  
# Solution for https://bugzilla.redhat.com/show_bug.cgi?id=1020147  
RUN sed -i -e "s/Defaults requiretty.*/ #Defaults requiretty/g" /etc/sudoers  
  
# Install xdebug and apc, clean up devel packages afterwards  
RUN yum -y install php-devel gcc pcre-devel && \  
pecl install xdebug-2.2.7 && \  
pecl install apc && \  
yum -y remove gcc php-devel pcre-devel && \  
yum clean all  
  
# Xdebug and apc settings.  
RUN \  
echo extension=apc.so >> /etc/php.d/apc.ini && \  
echo apc.enabled=1 >> /etc/php.d/apc.ini && \  
echo apc.shm_size=128M >> /etc/php.d/apc.ini && \  
echo zend_extension=/usr/lib64/php/modules/xdebug.so >> /etc/php.d/xdebug.ini
&& \  
echo xdebug.remote_enable=1 >> /etc/php.d/xdebug.ini && \  
echo xdebug.remote_connect_back=1 >> /etc/php.d/xdebug.ini && \  
echo xdebug.remote_autostart=0 >> /etc/php.d/xdebug.ini && \  
echo xdebug.max_nesting_level=256 >> /etc/php.d/xdebug.ini && \  
echo xdebug.remote_log=/var/www/logs/xdebug.log >> /etc/php.d/xdebug.ini  
  
# Set a custom entrypoint.  
COPY ./docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  

