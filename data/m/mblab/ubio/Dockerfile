FROM ubuntu:precise  
MAINTAINER Dmitry Mozzherin  
  
ENV LAST_FULL_REBUILD 2015-11-30  
RUN groupmod -g 1002 www-data && \  
usermod -s /bin/bash -u 1002 -g 1002 -d /home/www-data www-data  
  
RUN apt-get update && apt-get -y upgrade && \  
apt-get -y install python-software-properties locales git vim-nox rsync \  
supervisor sudo ruby1.9.1 mysql-client curl imagemagick \  
php5-cli php5-curl php-soap php5-imagick php5-gd php5-mcrypt \  
php5-xmlrpc php5-xsl php5-xdebug libarc-php php5-mysql \  
libphp-phpmailer php-auth-sasl php-http php-http-request php-http-upload \  
php-http-webdav-server php-image-text php-log php-mail \  
php-mail-mime php-mail-mimedecode php-mime-type php-net-dime php-net-ftp \  
php-net-smtp php-net-socket php-net-url php-pear php-xml-htmlsax3 \  
php-xml-parser php5-dev php5-memcache php5-memcached phpsysinfo \  
php5-fpm && echo "US/Eastern" > /etc/timezone && \  
dpkg-reconfigure -f noninteractive tzdata  
  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
RUN locale-gen en_US.UTF-8 && \  
dpkg-reconfigure locales  
  
# Can't run cron without policy:  
RUN echo "#!/bin/sh" > /usr/sbin/policy-rc.d && \  
echo "exit 0" >> /usr/sbin/policy-rc.d  
  
RUN add-apt-repository -y ppa:nginx/stable && \  
apt-get update && \  
apt-get install -qq -y nginx cron unzip && \  
echo "\ndaemon off;" >> /etc/nginx/nginx.conf  
  
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" \  
/etc/php5/fpm/php-fpm.conf  
RUN sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php5/fpm/php.ini  
  
COPY config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY config/php.ini /usr/local/lib/php.ini  
COPY config/nginx.conf /etc/nginx/nginx.conf  
COPY config/default /etc/nginx/sites-available/default  
COPY config/start.sh /  
COPY config/variables.php.template /  
  
RUN apt-get clean && \  
rm -rf /tmp/* /var/tmp/* && \  
apt-get -y autoremove && \  
mkdir /data  
  
CMD ["/start.sh"]  

