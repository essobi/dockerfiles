# Dockerfile for creating web frontend container for Moodle development.  
# See README.md for details.  
# Using eboraas/debian as base image. Clean and minimalistic  
# image based on debootstrapped version of Debian:jessie.  
FROM eboraas/debian:jessie  
  
MAINTAINER Ruslan Kabalin <r.kabalin@lancaster.ac.uk>  
  
# Install PHP and modules Moodle needs for functioning  
# (https://docs.moodle.org/31/en/PHP).  
RUN apt-get update && apt-get install -y \  
apache2 \  
php5 \  
libapache2-mod-php5 \  
php5-xmlrpc \  
php5-intl \  
php5-curl \  
php5-gd \  
php5-xsl \  
php5-mysql \  
php5-pgsql \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Prepare apache env.  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
  
# Make sure only mpm_prefork is enabled.  
RUN /usr/sbin/a2dismod 'mpm_*' && /usr/sbin/a2enmod mpm_prefork  
  
# Add Apache configuration.  
ADD 000-moodle.conf /etc/apache2/sites-available/  
ADD 001-moodle-ssl.conf /etc/apache2/sites-available/  
RUN /usr/sbin/a2enmod ssl  
RUN /usr/sbin/a2dissite '*' && /usr/sbin/a2ensite 000-moodle 001-moodle-ssl  
ADD 30-moodle.ini /etc/php5/apache2/conf.d/  
  
# Moodle data directory. Consider using data volume mounted at this path  
# for data persistency.  
RUN mkdir /srv/moodledata  
RUN chown -R www-data:www-data /srv/moodledata;  
  
# Install supervisord and clamav.  
RUN apt-get update && apt-get install -y \  
supervisor \  
clamav-daemon \  
clamav-freshclam \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Configure supervisord.  
RUN mkdir -p /var/log/supervisor  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Deploy clamav and freshclam init script.  
COPY clamav-init /usr/local/bin/  
RUN chmod 755 /usr/local/bin/clamav-init  
  
# Add www-data to clamav group to permit using it, also add clamav user to  
# www-data group for filesystem access.  
RUN adduser www-data clamav && \  
adduser clamav www-data  
  
EXPOSE 80  
EXPOSE 443  
CMD ["/usr/bin/supervisord", "-n"]  

