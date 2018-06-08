# Dockerfile for creating cron container for Moodle.  
# See README.md for details.  
# Using eboraas/debian as base image. Clean and minimalistic  
# image based on debootstrapped version of Debian:jessie.  
FROM eboraas/debian:jessie  
  
MAINTAINER Ruslan Kabalin <r.kabalin@lancaster.ac.uk>  
  
# Install PHP and modules Moodle needs for functioning  
# (https://docs.moodle.org/31/en/PHP).  
RUN apt-get update && apt-get install -y \  
cron \  
php5-cli \  
php5-xmlrpc \  
php5-intl \  
php5-curl \  
php5-gd \  
php5-xsl \  
php5-mysql \  
php5-pgsql \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Add crontab configuration.  
ADD moodle-cron /etc/cron.d/moodle-cron  
RUN chmod 0644 /etc/cron.d/moodle-cron  
  
# Moodle data directory. You need to use data volume mounted at this path  
# for data persistency.  
RUN mkdir /srv/moodledata  
RUN chown -R www-data:www-data /srv/moodledata;  
  
CMD ["cron", "-f"]  

