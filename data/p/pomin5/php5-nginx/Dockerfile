FROM phusion/baseimage:0.9.15  
MAINTAINER Pomin Wu <pomin5@gmail.com>  
ENV REFRESHED_AT 2015-04-05  
ENV HOME /root  
CMD ["/sbin/my_init"]  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get install -yq \  
git-core \  
php-apc \  
php-pear=5.5.9+dfsg-1ubuntu4.7 \  
php5-cli=5.5.9+dfsg-1ubuntu4.7 \  
php5-common=5.5.9+dfsg-1ubuntu4.7 \  
php5-curl=5.5.9+dfsg-1ubuntu4.7 \  
php5-fpm=5.5.9+dfsg-1ubuntu4.7 \  
php5-gd=5.5.9+dfsg-1ubuntu4.7 \  
php5-mysql=5.5.9+dfsg-1ubuntu4.7 \  
php5-pgsql=5.5.9+dfsg-1ubuntu4.7 \  
php5-sqlite=5.5.9+dfsg-1ubuntu4.7 \  
pwgen \  
vsftpd \  
nginx-full && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /etc/service/root \  
/etc/service/app \  
/etc/service/nginx \  
/etc/service/php5-fpm \  
/etc/service/vsftpd \  
/var/log/php5 \  
/var/log/vsftpd \  
/var/run/vsftpd/empty  
  
ADD service/root.sh /etc/service/root/run  
  
RUN useradd -u 1000 -g www-data --home-dir /home/app -s /bin/bash -m app  
ADD service/app.sh /etc/service/app/run  
  
RUN rm -f /etc/service/sshd/down  
ADD mykey.pub /tmp/mykey.pub  
  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
RUN rm -rf /etc/nginx/sites-enabled  
ADD etc/nginx/sites-enabled /etc/nginx/sites-enabled/  
ADD service/nginx.sh /etc/service/nginx/run  
  
ADD etc/php5/fpm/php-fpm.conf /etc/php5/fpm/php-fpm.conf  
ADD etc/php5/fpm/php.ini /etc/php5/fpm/php.ini  
ADD etc/php5/fpm/pool.d /etc/php5/fpm/pool.d  
ADD service/php5-fpm.sh /etc/service/php5-fpm/run  
  
ADD etc/vsftpd.conf /etc/vsftpd.conf  
ADD service/vsftpd.sh /etc/service/vsftpd/run  
  
RUN chmod 755 /etc/service/*/run  

