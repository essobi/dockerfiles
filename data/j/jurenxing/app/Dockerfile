FROM phusion/baseimage:latest  
MAINTAINER Allan Sun <allan.sun@bricre.com>  
  
RUN apt-get -y install --no-install-recommends software-properties-common && \  
locale-gen en_US.UTF-8 && export LANG=en_US.UTF-8 && export LC_ALL=en_US.UTF-8
&& \  
apt-add-repository ppa:ondrej/php && \  
apt-get update && \  
  
# Install necessary packagies  
apt-get -yq install --no-install-recommends \  
apache2 libapache2-mod-php7.0 iputils-ping \  
php7.0-cli php7.0-calendar php7.0-ctype php7.0-fileinfo php7.0-ftp
php7.0-gettext php7.0-pdo \  
php7.0-redis php7.0-gd php7.0-curl php7.0-intl php7.0-soap php7.0-iconv
php7.0-readline php7.0-mysql \  
php7.0-json php7.0-mcrypt php7.0-opcache php7.0-xml php7.0-zip php7.0-redis
php7.0-mongodb php7.0-gearman \  
php7.0-imagick ghostscript php-ssh2 && \  
a2enmod rewrite remoteip && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV APP_ENVIRONMENT=development  
EXPOSE 80  
CMD ["/sbin/my_init"]  
  
# Add configs  
ADD php.ini /etc/php/7.0/php.ini  
ADD run.apache.sh /etc/service/apache/run  
ADD ApacheConfig.conf /etc/apache2/sites-enabled/000-default.conf  
ADD apache2.conf /etc/apache2/apache2.conf  
RUN chmod +x /etc/service/apache/run && \  
ln -s /etc/php/7.0/php.ini /etc/php/7.0/cli/conf.d/90-php_extra.ini && \  
ln -s /etc/php/7.0/php.ini /etc/php/7.0/apache2/conf.d/90-php_extra.ini && \  
rm -rf /etc/service/cron /etc/service/sshd && \  
rm -f /etc/apache2/conf-enabled/other-vhosts-access-log.conf

