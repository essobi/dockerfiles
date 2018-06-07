FROM debian  
MAINTAINER Jason Cameron <jbkc85@gmail.com>  
  
LABEL version="2.1" \  
description="Debian Image for running Deep Thought.php"  
  
ENV DT_PROJECT_DIR=site \  
DT_DOCKER_GRP=staff \  
DT_LOG_TO_DOCKER=false  
  
# Install basic packages needed to get php/apache up and running.  
RUN apt-get update && \  
apt-get -y install sqlite3 php5 phpunit curl php5-curl php5-mysql php5-pgsql
php5-sqlite php5-oauth php5-mcrypt php5-json libapache2-mod-php5 git && \  
a2enmod ssl && \  
a2enmod rewrite && \  
a2dissite 000-default.conf && \  
apt-get clean && rm -rf /var/lib/apt/lists* /tmp/* /var/tmp/*  
  
# Convenience  
RUN perl -pi -e 's/short_open_tag = Off/short_open_tag = On/g'
/etc/php5/*/php.ini  
  
# Copy in all scripts, default settings and configurations  
COPY rootfs /  
  
# Adjust permissions of the data folder for SQLite Database  
# and create the basic database  
RUN ln -sf /dev/stdout /var/www/dt-logs/docker-access.log && \  
ln -sf /dev/stderr /var/www/dt-logs/docker-error.log && \  
chown www-data:staff /var/www/dt-example/logs/error.log  
  
# Expose /var/www/deepthought Volume  
VOLUME ["/var/www/deepthought"]  
# Expose port 80 by default  
EXPOSE 80 443  
RUN chmod +x /run.sh  
  
WORKDIR /var/www/deepthought  
CMD ["/run.sh"]  

