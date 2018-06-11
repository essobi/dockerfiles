###############################################  
# Dockerfile to build php-fpm  
# based on CentOS 7 image  
###############################################  
  
# Set the base image to CentOS 7  
FROM centos:centos7  
  
# Image author/maintainer  
MAINTAINER Randy Lowe <randy@weblogix.ca>  
  
# normal updates  
RUN yum -y update  
  
# install tools  
RUN yum -y install epel-release initscripts nano bind-utils net-tools ssmtp  
  
# Install PHP 7  
RUN \  
rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm && \  
  
yum -y install \  
php72w-fpm \  
php72w-opcache \  
php72w-bcmath \  
php72w-cli \  
php72w-common \  
php72w-gd \  
php72w-imap \  
php72w-mbstring \  
php72w-mcrypt \  
php72w-mysqlnd \  
php72w-pdo \  
php72w-pear \  
php72w-pecl-imagick \  
php72w-process \  
php72w-pspell \  
php72w-recode \  
php72w-tidy \  
php72w-xml  
  
# Copy php-fpm configuration  
COPY conf/php-fpm/www.conf /etc/php-fpm.d/www.conf  
COPY conf/php-fpm/php.ini /etc/php.ini  
  
# Copy supervisor configuration file  
RUN yum -y install supervisor  
COPY conf/supervisor/supervisord.conf /etc/supervisord.conf  
  
# Forward logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/php-fpm/access.log \  
&& ln -sf /dev/stderr /var/log/fpm-php.www.log \  
&& ln -sf /dev/stderr /var/log/php-fpm/fpm-error.log  
  
# Clean up  
RUN yum clean all  
  
# Expose ports  
EXPOSE 9000  
  
CMD ["/usr/bin/supervisord"]  

