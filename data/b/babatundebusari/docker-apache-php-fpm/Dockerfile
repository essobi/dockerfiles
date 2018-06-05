FROM ubuntu:14.04.4  
MAINTAINER Babatunde Busari  
  
# Surpress Upstart errors/warning  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -sf /bin/true /sbin/initctl  
  
# Let the conatiner know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y software-properties-common  
  
# RUN add-apt-repository -y "deb http://archive.ubuntu.com/ubuntu
$(lsb_release -sc) universe"  
RUN add-apt-repository -y "deb http://archive.ubuntu.com/ubuntu $(lsb_release
-sc) multiverse"  
RUN add-apt-repository -y "deb http://archive.ubuntu.com/ubuntu $(lsb_release
-sc)-updates multiverse"  
  
RUN apt-get update && \  
BUILD_PACKAGES="supervisor apache2 libapache2-mod-fastcgi php5-fpm
apache2-mpm-event git php5-mysql php-apc php5-mysql php5-curl php5-gd
php5-intl php5-mcrypt php5-memcache php5-sqlite php5-tidy php5-xmlrpc php5-xsl
php5-pgsql php5-mongo php5-ldap pwgen" && \  
apt-get -y install $BUILD_PACKAGES && \  
apt-get remove --purge -y software-properties-common && \  
apt-get autoremove -y && \  
apt-get clean && \  
apt-get autoclean && \  
echo -n > /var/lib/apt/extended_states && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /usr/share/man/?? && \  
rm -rf /usr/share/man/??_*  
  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf  
  
# tweak php-fpm config  
RUN sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g"
/etc/php5/fpm/php.ini && \  
sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g"
/etc/php5/fpm/php.ini && \  
sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g"
/etc/php5/fpm/php.ini && \  
sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php5/fpm/php-fpm.conf
&& \  
sed -i -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g"
/etc/php5/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.max_children = 5/pm.max_children = 9/g"
/etc/php5/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.start_servers = 2/pm.start_servers = 3/g"
/etc/php5/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.min_spare_servers = 1/pm.min_spare_servers = 2/g"
/etc/php5/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.max_spare_servers = 3/pm.max_spare_servers = 4/g"
/etc/php5/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.max_requests = 500/pm.max_requests = 200/g"
/etc/php5/fpm/pool.d/www.conf  
  
# fix ownership of sock file for php-fpm  
RUN sed -i -e "s/;listen.mode = 0660/listen.mode = 0750/g"
/etc/php5/fpm/pool.d/www.conf && \  
find /etc/php5/cli/conf.d/ -name "*.ini" -exec sed -i -re
's/^(\s*)#(.*)/\1;\2/g' {} \;  
  
# apache2 conf  
RUN rm -Rf /etc/apache2/sites-enabled/* && \  
rm -Rf /var/www/html/* && \  
mkdir -p /etc/apache2/ssl/  
ADD conf/apache2-site.conf /etc/apache2/sites-available/000-default.conf  
RUN ln -s /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-
enabled/000-default.conf  
  
# php5-fpm site cconf  
ADD conf/php5-fpm.conf /etc/apache2/conf-available/php5-fpm.conf  
  
# enable and disable conf  
RUN php5enmod mcrypt && \  
a2enmod actions fastcgi alias && \  
a2dismod mpm_prefork && \  
a2enconf php5-fpm && \  
a2enmod rewrite && \  
a2enmod mpm_event  
  
# Supervisor Config  
ADD conf/supervisord.conf /etc/supervisord.conf  
  
# Start Supervisord  
ADD scripts/start.sh /start.sh  
RUN chmod 755 /start.sh  
  
# Setup Volume  
#VOLUME ["/var/www/html"]  
# add test PHP file  
ADD src/index.php /var/www/html/index.php  
RUN chown -Rf www-data.www-data /var/www/html/  
  
#mount volume correct way  
VOLUME /var/www/html  
  
# Expose Ports  
EXPOSE 443  
EXPOSE 80  
CMD ["/bin/bash", "/start.sh"]  

