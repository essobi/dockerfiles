FROM centos:centos7  
  
# Install the latest EPEL release RPM.  
# Then add the GPG keys to help verify packages and reduce errors(red) in the
output.  
# Update the system.  
# Perform clean-up.  
RUN yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm \  
&& rpm --import \  
/etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7 \  
/etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7 \  
&& yum -y update \  
&& yum clean all  
  
# Include the REMI release RPM to get the latest PHP version.  
# Then add the GPG keys to help verify packages and reduce errors(red) in the
output.  
# Update the system.  
# Perform clean-up.  
RUN yum -y install http://rpms.famillecollet.com/enterprise/remi-release-7.rpm
\  
&& rpm --import \  
/etc/pki/rpm-gpg/RPM-GPG-KEY-remi \  
&& yum -y update \  
&& yum clean all \  
&& rm -rf /var/cache/yum  
  
# Specify which version of PHP to install.  
# Update the system.  
# Install the PHP packages.  
# Perform clean-up.  
# Downloand PHP composer.  
# Move the default configuration files out of the way.  
RUN yum-config-manager --enable remi,remi-php71 \  
&& yum -y update \  
&& yum -y install php \  
php-apcu \  
php-bcmath \  
php-cli \  
php-common \  
php-devel \  
php-fpm \  
php-mbstring \  
php-mcrypt \  
php-mysql \  
php-pdo \  
php-pdo_dblib \  
php-pecl-libsodium \  
php-pecl-memcached \  
php-pecl-mongodb \  
php-pecl-zip \  
php-tidy \  
php-xml \  
&& curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
\  
&& mv /etc/php.ini /etc/php.txt \  
&& mv /etc/php-fpm.conf /etc/php-fpm.txt \  
&& mv /etc/php-fpm.d/www.conf /etc/php-fpm.d/www.txt \  
&& rm -rf /var/cache/yum  
  
# Use custom PHP configs.  
ADD ./php.ini /etc/php.ini  
ADD ./php-fpm.conf /etc/php-fpm.conf  
ADD ./www.conf /etc/php-fpm.d/www.conf  
ADD ./start-php-fpm.sh /bin/start-php-fpm.sh  
  
RUN chmod a+x /bin/start-php-fpm.sh  
  
EXPOSE 9000  
EXPOSE 10000  
# docker build --rm --no-cache -t khalifahks/centos-php ./centos7-php  
# docker build --rm -t khalifahks/centos-php ./centos7-php  
# docker run -d --rm -p 9000:9000 --name centos-php -h centos_php
khalifahks/centos-php  
# docker run -it --rm -p 9000:9000 --name centos-php -h centos_php
khalifahks/centos-php  
# docker exec -it centos-php bash  
# cp from docker  
# docker cp centos-apps:/etc/php.d/15-xdebug.ini ./centos7-php/  
ENTRYPOINT ["start-php-fpm.sh"]

