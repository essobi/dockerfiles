FROM ubuntu:14.04.4  
MAINTAINER Steve Yardumian  
  
# Surpress Upstart errors/warning  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -sf /bin/true /sbin/initctl  
  
# Let the conatiner know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# unpack the oracle instant client  
RUN mkdir -p /opt/oracle/instantclient_12_1  
ADD lib/instantclient_12_1 /opt/oracle/instantclient_12_1/  
RUN ln -s /opt/oracle/instantclient_12_1/libocci.so.12.1
/opt/oracle/instantclient_12_1/libocci.so && \  
ln -s /opt/oracle/instantclient_12_1/libclntsh.so.12.1
/opt/oracle/instantclient_12_1/libclntsh.so  
  
# Add LD Library Path  
RUN echo 'LD_LIBRARY_PATH="/opt/oracle/instantclient_12_1"' >>
/etc/environment  
  
# WGET  
RUN apt-get update && \  
apt-get -y install wget  
  
#add postgres source for apt  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" >>
/etc/apt/sources.list.d/pgdg.list  
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc |
apt-key add -  
  
# Update base image  
# Add sources for latest nginx  
# Install software requirements  
RUN apt-get update && \  
apt-get install -y software-properties-common python-software-properties
libpcre3-dev && \  
nginx=stable && \  
add-apt-repository ppa:nginx/$nginx && \  
add-apt-repository ppa:webupd8team/java -y && \  
apt-get update && \  
apt-get upgrade -y && \  
BUILD_PACKAGES="supervisor nginx php5-dev php5-fpm git php5-mysql php-apc
php5-curl php5-gd php5-intl php5-mcrypt php5-memcache php5-sqlite php5-tidy
php5-xmlrpc php5-xsl php5-pgsql php5-mongo php5-ldap pwgen postgresql-
client-9.4" && \  
apt-get -y install $BUILD_PACKAGES && \  
apt-get autoremove -y && \  
apt-get clean && \  
apt-get autoclean && \  
echo -n > /var/lib/apt/extended_states && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /usr/share/man/?? && \  
rm -rf /usr/share/man/??_*  
  
# install oci8 & zip extensions  
RUN yes 'instantclient,/opt/oracle/instantclient_12_1' | pecl install -f
oci8-2.0.10  
RUN pecl install -f zip  
  
# install java 8 and oci8 dependencies  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
apt-get install -y oracle-java8-set-default && \  
apt-get install -y libaio1 libaio-dev  
  
# PHP conf OCI8 extension  
RUN echo "extension=oci8.so" >> /etc/php5/fpm/conf.d/20-oci8.ini  
RUN echo "extension=oci8.so" >> /etc/php5/cli/conf.d/20-oci8.ini  
  
# PHP conf zip extension  
#RUN echo "extension=zip.so" >> /etc/php5/fpm/conf.d/10-zip.ini  
#RUN echo "extension=zip.so" >> /etc/php5/cli/conf.d/10-zip.ini  
# tweak nginx config  
RUN sed -i -e"s/worker_processes 1/worker_processes 5/" /etc/nginx/nginx.conf
&& \  
sed -i -e"s/keepalive_timeout\s*65/keepalive_timeout 2/" /etc/nginx/nginx.conf
&& \  
sed -i -e"s/keepalive_timeout 2/keepalive_timeout 2;\n\tclient_max_body_size
100m/" /etc/nginx/nginx.conf && \  
echo "daemon off;" >> /etc/nginx/nginx.conf  
  
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
  
# mycrypt conf  
RUN php5enmod mcrypt  
  
# nginx site conf  
RUN rm -Rf /etc/nginx/conf.d/* && \  
rm -Rf /etc/nginx/sites-available/default && \  
mkdir -p /etc/nginx/ssl/  
ADD conf/nginx-site.conf /etc/nginx/sites-available/default.conf  
RUN ln -s /etc/nginx/sites-available/default.conf /etc/nginx/sites-
enabled/default.conf  
  
# Add git commands to allow container updating  
ADD scripts/pull /usr/bin/pull  
ADD scripts/push /usr/bin/push  
RUN chmod 755 /usr/bin/pull && chmod 755 /usr/bin/push  
  
# Supervisor Config  
ADD conf/supervisord.conf /etc/supervisord.conf  
  
# Start Supervisord  
ADD scripts/start.sh /start.sh  
RUN chmod 755 /start.sh  
  
# Setup Volume  
VOLUME ["/usr/share/nginx/html"]  
  
# add test PHP file  
ADD src/index.php /usr/share/nginx/html/index.php  
RUN chown -Rf www-data.www-data /usr/share/nginx/html/  
  
# Expose Ports  
EXPOSE 443  
EXPOSE 80  
CMD ["/bin/bash", "/start.sh"]  

