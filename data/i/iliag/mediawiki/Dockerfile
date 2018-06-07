FROM phusion/baseimage:latest  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV MEDIAWIKI_MAJOR 1.25  
ENV MEDIAWIKI_MINOR 2  
RUN apt-get update -y \  
&& apt-get install -y wget nginx php5-fpm php5-intl php-apc php5-gd php5-intl
php5-mysqlnd php5-pgsql php-pear php5-cli php5-curl php5-mcrypt \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY etc /etc  
  
RUN mkdir /home/vhosts \  
&& cd /home/vhosts \  
&& mkdir /home/vhosts/mediawiki \  
&& wget
http://releases.wikimedia.org/mediawiki/${MEDIAWIKI_MAJOR}/mediawiki-${MEDIAWIKI_MAJOR}.${MEDIAWIKI_MINOR}.tar.gz
-O /mediawiki.tar.gz \  
&& tar -xvzf /mediawiki.tar.gz -C /home/vhosts/mediawiki --strip-components=1
\  
&& rm /mediawiki.tar.gz \  
&& rm -f /etc/nginx/sites-enabled/default \  
&& chown -R www-data:www-data /home/vhosts/mediawiki \  
&& rm -rf /home/vhosts/mediawiki/images  
  
CMD ["/sbin/my_init"]  
  
VOLUME ["/home/vhosts/mediawiki/images"]  
  

