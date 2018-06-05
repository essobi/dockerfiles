FROM debian:7  
MAINTAINER Pavel Emelianov <pve@ctg66.ru>  
  
RUN apt-get update --fix-missing  
RUN apt-get -y install php-pear php5-cgi php5-cli php5-common php5-curl
php5-fpm php5-gd php5-imagick php5-intl php5-mcrypt php5-mysql php5-tidy
php5-xsl php-apc php5-memcached memcached ssmtp  
  
RUN sed -i '/^listen/c \  
listen = 0.0.0.0:9000' /etc/php5/fpm/pool.d/www.conf  
  
RUN sed -i 's/;daemonize = yes/daemonize = no/g' /etc/php5/fpm/php-fpm.conf  
  
# modify ssmtp settings  
RUN sed -ri -e 's/^(mailhub=).*/\1smtp-server/' -e
's/^#(FromLineOverride)/\1/' /etc/ssmtp/ssmtp.conf  
  
RUN mkdir /var/www  
  
EXPOSE 9000  
VOLUME /var/www  
  
VOLUME /tmp  
  
CMD service memcached start && /usr/sbin/php5-fpm

