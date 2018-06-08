FROM phusion/baseimage:latest  
#MAINTAINER Brendan Tobolaski "brendan@tobolaski.com"  
MAINTAINER sauloal@gmail.com  
  
RUN apt-get -y update \  
&& apt-get install -y apache2 \  
php5 php5-gd php-xml-parser \  
php5-intl php5-mysqlnd php5-json \  
php5-mcrypt php5-curl php5-cli \  
php5-dev php5-sqlite \  
smbclient curl libcurl3 \  
bzip2 wget make \  
sqlite3 libsqlite3-0 libsqlite3-dev \  
&& apt-get clean all \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
RUN curl -k https://download.owncloud.org/community/owncloud-7.0.2.tar.bz2 |
tar jx -C /var/www/  
RUN mkdir /var/www/owncloud/data  
RUN chown -R www-data:www-data /var/www/owncloud  
  
ADD ./001-owncloud.conf /etc/apache2/sites-available/  
RUN rm -f /etc/apache2/sites-enabled/000*  
RUN ln -s /etc/apache2/sites-available/001-owncloud.conf /etc/apache2/sites-
enabled/  
RUN a2enmod rewrite  
  
#ADD sqlite3.ini /etc/php5/conf.d/sqlite3.ini  
ADD rc.local /etc/rc.local  
RUN chown root:root /etc/rc.local  
  
# Add PHP-FPM to runit  
#RUN mkdir /etc/service/php-fpm  
#ADD php-fpm.sh /etc/service/php-fpm/run  
#RUN chmod +x /etc/service/php-fpm/run  
VOLUME ["/var/www/owncloud/data" ]  
VOLUME ["/var/www/owncloud/config"]  
  
EXPOSE 80  
CMD ["/sbin/my_init"]  

