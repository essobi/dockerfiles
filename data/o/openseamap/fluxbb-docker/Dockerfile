FROM phusion/baseimage:0.9.19  
MAINTAINER Axel Utech <axel@brasshack.de>  
  
ENV LANG en_US.UTF-8  
ENV DEBIAN_FRONTEND noninteractive  
  
CMD ["/sbin/my_init"]  
  
RUN \  
echo "Acquire::Languages \"none\";\nAPT::Install-Recommends
\"true\";\nAPT::Install-Suggests \"false\";" > /etc/apt/apt.conf ;\  
echo "Europe/Berlin" > /etc/timezone && dpkg-reconfigure tzdata ;\  
locale-gen en_US.UTF-8 en_DK.UTF-8 de_DE.UTF-8 ;\  
apt-get -q -y update ;\  
apt-get install -y aria2 nginx-light graphviz graphviz-dev mysql-client \  
php5-fpm \  
php5-mysql \  
php5-imagick \  
php5-mcrypt \  
php5-curl \  
php5-cli \  
php5-memcache \  
php5-intl \  
php5-gd \  
php5-xdebug \  
php5-gd \  
php5-imap \  
php-mail \  
php-pear \  
unzip \  
php-apc ;\  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN \  
echo "daemon off;" >> /etc/nginx/nginx.conf ;\  
mkdir /etc/service/nginx ;\  
echo "#!/bin/sh\n/usr/sbin/nginx" > /etc/service/nginx/run ;\  
chmod +x /etc/service/nginx/run  
  
ADD service-php5-fpm.sh /etc/service/php5-fpm/run  
RUN chmod +x /etc/service/php5-fpm/run  
  
ADD nginx-site.conf /etc/nginx/sites-available/default  
  
# create data dirs  
RUN \  
mkdir /data \  
mkdir /data/backup  
  
RUN \  
cd /tmp && aria2c -s 4
http://fluxbb.org/download/releases/1.5.9/fluxbb-1.5.9.tar.gz ;\  
mkdir /data/fluxbb ;\  
tar xvzf /tmp/fluxbb-1.5.9.tar.gz --strip-components=1 -C /data/fluxbb ;\  
rm -rf /tmp/fluxbb-1.5.9.tar.gz  
  
# set necessary rights  
RUN \  
chown -R www-data /data/fluxbb  
  
ADD docker-entrypoint.sh /etc/rc.local  
ADD backup-mysql.sh /etc/cron.daily/backup-mysql  
  
RUN sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php5/fpm/php.ini
;\  
php5dismod xdebug ;\  
chmod +x /etc/rc.local ;\  
chmod +x /etc/cron.daily/backup-mysql  
  
EXPOSE 80  
VOLUME "/data"  

