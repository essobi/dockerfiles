##############################################  
# Dockerfile to build Apache HTTP server image  
##############################################  
# Base image  
FROM ubuntu:14.04  
  
# Author: MobileSnapp Inc.  
MAINTAINER MobileSnapp <support@mobilesnapp.com>  
  
# Disable interactive functions  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y --no-install-recommends git ca-
certificates && \  
# remove extra space from git command  
apt-get remove -y git && \  
apt-get autoremove -y && \  
# remove apt cache from image  
apt-get clean all  
  
# Set environment variables.  
ENV HOME /root  
  
RUN apt-get update && \  
apt-get install -y apache2 && \  
rm -rf /var/lib/apt/lists/*  
  
ADD dir.conf /etc/apache2/mods-enabled/dir.conf  
  
RUN apt-get update && \  
apt-get install -y php5 libapache2-mod-php5 \  
php5-fpm php5-cli php5-mysqlnd php5-pgsql php5-sqlite php5-redis \  
php5-apcu php5-intl php5-imagick php5-mcrypt php5-json php5-gd php5-curl \  
php5-cgi php5-common php5-dbg php5-dev php5-gd php-pear php-apc && \  
php5enmod mcrypt && \  
rm -rf /var/lib/apt/lists/* && \  
cd /tmp && curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN /usr/sbin/php5enmod mcrypt  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf && \  
sed -i "s/variables_order.*/variables_order = \"EGPCS\"/g"
/etc/php5/apache2/php.ini  
  
ENV ALLOW_OVERRIDE **False**  
  
# Update the default apache site with the config we created.  
ADD apache-config.conf /etc/apache2/sites-enabled/000-default.conf  
  
# Activate mod_rewrites  
RUN a2enmod rewrite  
  
# Restart server  
RUN service apache2 restart  
  
COPY index.php /var/www  
  
# Assign working directory  
WORKDIR /var/www/site/  
  
# Expose web and SSL ports.  
EXPOSE 80  
EXPOSE 443  
  
# By default start up apache in the foreground, override with /bin/bash for
interative.  
CMD /usr/sbin/apache2ctl -D FOREGROUND  

