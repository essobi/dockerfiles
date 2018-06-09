FROM ubuntu:16.04  
RUN DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get install -y --no-install-recommends locales && \  
locale-gen en_US.UTF-8 && \  
apt-get install -y --no-install-recommends iproute2 apache2 php7.0
libapache2-mod-php7.0 \  
php7.0-mysql php7.0-sqlite php7.0-bcmath php7.0-curl ca-certificates && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/* && \  
echo "ServerName $(ip route get 8.8.8.8 | awk '{print $NF; exit}')" >>
/etc/apache2/apache2.conf && \  
a2enmod php7.0 && \  
a2enmod rewrite && \  
sed -i "s/short_open_tag = Off/short_open_tag = On/"
/etc/php/7.0/apache2/php.ini  
  
RUN ln -sf /dev/stdout /var/log/apache2/access.log \  
&& ln -sf /dev/stderr /var/log/apache2/error.log  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
ENV TZ=Europe/Moscow  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
  
WORKDIR /var/www/html  
  
EXPOSE 80  
CMD rm -f /var/run/apache2/apache2.pid && /usr/sbin/apache2ctl -D FOREGROUND  

