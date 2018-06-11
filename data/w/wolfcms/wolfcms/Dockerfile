# Set the base image to Ubuntu  
FROM ubuntu:14.04.1  
# File Author / Maintainer  
MAINTAINER Martijn <martijn.niji@gmail.com>  
  
# Install basic applications  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get -yq install \  
curl \  
git-core \  
apache2 \  
libapache2-mod-php5 \  
php5-mysql \  
php5-gd \  
php5-curl && \  
rm -rf /var/lib/apt/lists/*  
RUN sed -i "s/variables_order.*/variables_order = \"EGPCS\"/g"
/etc/php5/apache2/php.ini  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Turn on rewrite module  
RUN a2enmod rewrite  
  
# copy a few things from apache's init script that it requires to be setup  
ENV APACHE_CONFDIR /etc/apache2  
ENV APACHE_ENVVARS $APACHE_CONFDIR/envvars  
  
# and then a few more from $APACHE_CONFDIR/envvars itself  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_PID_FILE $APACHE_RUN_DIR/apache2.pid  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV LANG C  
RUN mkdir -p $APACHE_RUN_DIR $APACHE_LOCK_DIR $APACHE_LOG_DIR  
  
# make CustomLog (access log) go to stdout instead of files  
# and ErrorLog to stderr  
RUN find "$APACHE_CONFDIR" -type f -exec sed -ri ' \  
s!^(\s*CustomLog)\s+\S+!\1 /proc/self/fd/1!g; \  
s!^(\s*ErrorLog)\s+\S+!\1 /proc/self/fd/2!g; \  
' '{}' ';'  
  
# Create document root  
RUN rm -rf /var/www/html && mkdir -p /var/www/html  
  
# Set the default directory where CMD will execute  
WORKDIR /var/www/html  
  
# git clone checks out to /var/www/html/wolfcms  
RUN git clone https://github.com/wolfcms/wolfcms.git  
  
# Mount an external volume for /var/www/html/wolfcms/public  
#VOLUME /var/www/html  
# Create Apache vhost and enable is  
COPY docker-apache.conf /etc/apache2/sites-available/wolfcms.conf  
RUN a2dissite 000-default && a2ensite wolfcms  
  
# Expose ports  
EXPOSE 80  
#COPY docker-entrypoint.sh /entrypoint.sh  
#ENTRYPOINT ["/entrypoint.sh"]  
# Run Apache  
CMD ["apache2", "-DFOREGROUND"]  

