FROM ubuntu:14.04.4  
MAINTAINER SJ <sj@toright.com>  
  
# Surpress Upstart errors/warning  
RUN dpkg-divert --local --rename --add /sbin/initctl  
RUN ln -sf /bin/true /sbin/initctl  
  
# Install package  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get upgrade -y  
RUN apt-get -y install software-properties-common  
RUN apt-get -y install nginx nginx-full  
RUN apt-get -y install php5-fpm \  
php5-mysqlnd \  
php5-curl \  
php5-gd \  
php5-mcrypt \  
php5-tidy \  
php5-mongo \  
php5-gearman \  
php5-cli \  
php5-gmp \  
php5-geoip \  
php5-ldap \  
php5-common  
RUN apt-get -y install supervisor  
RUN php5enmod mcrypt  
  
# Remove and clean  
RUN apt-get remove \--purge -y software-properties-common && \  
apt-get autoremove -y && \  
apt-get clean && \  
apt-get autoclean && \  
echo -n > /var/lib/apt/extended_states && \  
rm -rf /usr/share/man/?? && \  
rm -rf /usr/share/man/??_*  
  
# Add config files  
RUN rm -Rf /etc/nginx/nginx.conf && \  
rm -Rf /etc/nginx/sites-available/default && \  
rm -Rf /etc/php5/fpm/php.ini && \  
rm -Rf /etc/php5/fpm/php-fpm.conf && \  
rm -Rf /etc/php5/fpm/pool.d/www.conf  
ADD conf/nginx.conf /etc/nginx/nginx.conf  
ADD conf/default  /etc/nginx/sites-available/default  
ADD conf/php.ini /etc/php5/fpm/php.ini  
ADD conf/php-fpm.conf /etc/php5/fpm/php-fpm.conf  
ADD conf/www.conf /etc/php5/fpm/pool.d/www.conf  
ADD conf/www-2g.conf /tmp  
ADD conf/www-4g.conf /tmp  
ADD conf/www-8g.conf /tmp  
ADD conf/www-16g.conf /tmp  
  
# init supervisor  
RUN rm -Rf /etc/supervisord.conf  
ADD conf/supervisord.conf /etc/supervisor/supervisord.conf  
ADD conf/sv-nginx.conf /etc/supervisor/conf.d  
ADD conf/sv-php5-fpm.conf /etc/supervisor/conf.d  
ADD conf/start.sh /start.sh  
  
# Expose Ports  
EXPOSE 80 9001  
  
CMD ["/start.sh"]  

