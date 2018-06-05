FROM centos:7  
MAINTAINER David Numan david.numan_at_civicactions.com  
  
RUN yum -y update; yum clean all  
  
ADD ./conf/yum/ivarch.repo /etc/yum.repos.d/ivarch.repo  
RUN rpm --import http://www.ivarch.com/personal/public-key.txt  
  
RUN yum -y install scl-utils git mariadb-libs mariadb wget sudo python-
setuptools nano vim pv && \  
yum clean all  
  
# Install php 5.5  
RUN wget
https://www.softwarecollections.org/en/scls/rhscl/php55/epel-7-x86_64/download/rhscl-
php55-epel-7-x86_64.noarch.rpm && \  
yum -y install rhscl-php55-epel-7-x86_64.noarch.rpm && \  
rm -v rhscl-php55-epel-7-x86_64.noarch.rpm && \  
yum -y install php55 php55-php-gd php55-php-mysqlnd php55-php-pdo php55-php-
xml php55-php-opcache php55-php-fpm php55-php-soap php55-php-mbstring && \  
yum clean all && \  
scl enable php55 bash  
  
# Install Xdebug compilation dependencies  
Run yum -y install gcc gcc-c++ autoconf automake  
Run yum -y --enablerepo=remi,remi-php55 install php55-php-devel  
  
# Install apache  
RUN yum -y install httpd mod_ssl mod_fcgid && yum clean all  
  
# Auto-enable php55: create file /etc/profile.d/enablephp55.sh with this
content:  
# http://developerblog.redhat.com/2014/03/19/permanently-enable-a-software-
collection/  
RUN source /opt/rh/php55/enable && \  
export X_SCLS="`scl enable php55 'echo $X_SCLS'`"  
  
RUN echo source /opt/rh/php55/enable > /etc/profile.d/php55.sh && \  
echo export X_SCLS="\\`scl enable php55 'echo $X_SCLS'\\`" >>
/etc/profile.d/php55.sh  
  
ENV PATH=/opt/rh/php55/root/usr/bin:/opt/rh/php55/root/usr/sbin:$PATH  
  
# Apache config.  
RUN sed -i 's,/var/www/html,/var/www/docroot,' /etc/httpd/conf/httpd.conf  
ADD ./conf/apache2/docker-host.conf /etc/httpd/conf.d/docker-host.conf  
  
# PHP config.  
ADD ./conf/php5/docker-php.ini /opt/rh/php55/root/etc/php.d/docker-php.ini  
ADD ./conf/php5/www.conf /opt/rh/php55/root/etc/php-fpm.d/www.conf  
  
# Xdebug  
RUN yes | pecl install xdebug \  
&& echo "zend_extension=/opt/rh/php55/root/usr/lib64/php/modules/xdebug.so" >>
/opt/rh/php55/root/etc/php.ini \  
&& echo "xdebug.remote_enable=on" >> /opt/rh/php55/root/etc/php.ini \  
&& echo "xdebug.remote_autostart=off" >> /opt/rh/php55/root/etc/php.ini  
  
# Drupal settings.  
ADD ./conf/drupal/settings.docker.php /etc/settings.docker.php  
  
# Composer.  
RUN source /opt/rh/php55/enable && \  
curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin -d
detect_unicode=0 && \  
ln -s /usr/bin/composer.phar /usr/bin/composer  
  
# Set a custom entrypoint.  
COPY ./docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  

