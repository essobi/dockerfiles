FROM ubuntu:trusty  
MAINTAINER developers@khipu.com  
  
RUN echo 'America/Santiago' > /etc/timezone && \  
dpkg-reconfigure --frontend noninteractive tzdata && \  
dpkg-reconfigure --frontend noninteractive locales && \  
locale-gen en_US.UTF-8 && \  
update-locale LANG=en_US.UTF-8  
  
ENV LC_ALL en_US.UTF-8  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get -y install supervisor apache2 libapache2-mod-php5 php5-curl php5-mysql
pwgen php-apc php5-mcrypt php5-gd vim && \  
apt-get clean && \  
php5enmod mcrypt && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Add image configuration and scripts  
ADD start-apache2.sh /start-apache2.sh  
ADD run.sh /run.sh  
ADD supervisord-apache2.conf /etc/supervisor/conf.d/supervisord-apache2.conf  
  
# config to enable .htaccess  
ADD apache_default /etc/apache2/sites-available/000-default.conf  
  
#Environment variables to configure php  
ENV PHP_UPLOAD_MAX_FILESIZE 10M  
ENV PHP_POST_MAX_SIZE 10M  
  
RUN chmod 755 /*.sh && \  
a2enmod rewrite && \  
groupmod -g 2000 www-data && \  
usermod -u 2000 -g 2000 www-data && \  
find /var -uid 33 | xargs chown -R www-data:www-data && \  
find /run -uid 33 | xargs chown -R www-data:www-data && \  
echo "ServerName localhost" >> /etc/apache2/apache2.conf  
  
CMD ["/run.sh"]  

