# Dockerfile for new version of PHP7-FPM.  
FROM ubuntu:latest  
MAINTAINER Pablo Gillari Ces <pgillari@lyracons.com>  
  
# Avoid terminal dialog messages on Ubuntu/Debian containers.  
# Don't show errors when calling console.  
RUN export DEBIAN_FRONTEND=noninteractive && \  
export DEBCONF_NONINTERACTIVE_SEEN=true && \  
sed -i 's/^mesg n$/tty -s \&\& mesg n/g' /root/.profile  
  
# Common packages.  
RUN apt-get install -y vim curl wget  
  
# Installation.  
RUN apt-get update && \  
apt-get install -y python-software-properties software-properties-common  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
RUN apt-add-repository ppa:ondrej/php-7.0 && \  
apt-get update && \  
apt-get install -y php7.0 php7.0-common php7.0-dev php7.0-fpm php7.0-cli
php7.0-mcrypt php7.0-intl php7.0-xsl php7.0-gd php7.0-curl php7.0-imap
php7.0-json php7.0-opcache php7.0-mysql libpcre3-dev  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Configuration.  
RUN usermod -u 1000 www-data && \  
sed -i "s/^max_execution_time = \\(.*\\)/max_execution_time = 600/g"
/etc/php/7.0/fpm/php.ini && \  
sed -i "s/^max_input_time = \\(.*\\)/max_input_time = 600/g"
/etc/php/7.0/fpm/php.ini && \  
sed -i "s/^memory_limit = \\(.*\\)/memory_limit = 2G/g"
/etc/php/7.0/fpm/php.ini && \  
sed -i "s/^upload_max_filesize = \\(.*\\)/upload_max_filesize = 4M/g"
/etc/php/7.0/fpm/php.ini && \  
sed -i "s/^;request_terminate_timeout = \\(.*\\)/request_terminate_timeout =
300/g" /etc/php/7.0/fpm/php.ini && \  
sed -i "s/^listen = \\(.*\\)/listen = 9000/g" /etc/php/7.0/fpm/pool.d/www.conf  
  
# Entrypoint.  
ADD ./entrypoint.sh /root/entrypoint.sh  
RUN chmod +x /root/entrypoint.sh  
ENTRYPOINT ["/bin/bash", "/root/entrypoint.sh"]  

