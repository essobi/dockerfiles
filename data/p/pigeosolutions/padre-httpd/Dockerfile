FROM debian:jessie  
MAINTAINER Jean Pommier <jean.pommier@pi-geosolutions.fr>  
  
LABEL version="1.0"  
LABEL description="Apache 2 / PHP with postgresql support & phppgadmin"  
  
#RUN apt-get update && apt-get install -y \  
# libpq-dev \  
# vim  
#RUN docker-php-ext-configure pgsql -with-pgsql=/usr/include/postgresql \  
# && docker-php-ext-install pgsql pdo_pgsql  
#EXPOSE 80  
#CMD ["apache2-foreground"]  
# Update the package repository  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y wget curl locales unzip  
  
# Configure timezone and locale  
RUN echo "Etc/UTC" > /etc/timezone && \  
dpkg-reconfigure -f noninteractive tzdata  
RUN export LANGUAGE=en_US.UTF-8 && \  
export LANG=en_US.UTF-8 && \  
export LC_ALL=en_US.UTF-8 && \  
locale-gen en_US.UTF-8 && \  
dpkg-reconfigure locales  
  
# Install APACHE & PHP 5  
RUN apt-get update && \  
apt-get install -y \  
apache2 \  
libapache2-mod-php5 \  
libpq-dev \  
php5 \  
php5-cli \  
php5-curl \  
php5-mcrypt \  
php5-pgsql \  
phppgadmin \  
postgresql-contrib \  
vim  
  
# Let's set the default timezone in both cli and apache configs  
RUN sed -i 's/\;date\\.timezone\ \=/date\\.timezone\ \=\ Etc\/UTC/g'
/etc/php5/cli/php.ini && \  
sed -i 's/\;date\\.timezone\ \=/date\\.timezone\ \=\ Etc\/UTC/g'
/etc/php5/apache2/php.ini  
  
# Activate a2enmod  
RUN a2enmod rewrite  
  
WORKDIR /var/www  
  
#install phppgadmin from github repo  
ENV PHPPGADMIN_VERSION REL_5-1-0  
RUN ln -sf /dev/stdout /var/log/apache2/access.log \  
&& ln -sf /dev/stdout /var/log/apache2/error.log \  
&& chown -R www-data:www-data /var/log/apache2 /var/www \  
&& wget
https://github.com/phppgadmin/phppgadmin/archive/${PHPPGADMIN_VERSION}.zip \  
&& unzip /var/www/${PHPPGADMIN_VERSION}.zip \  
&& rm /var/www/${PHPPGADMIN_VERSION}.zip \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD config.inc.php
/var/www/phppgadmin-${PHPPGADMIN_VERSION}/conf/config.inc.php  
  
WORKDIR /var/www/html  
  
#make it read the environment variables  
RUN sed -i 's/variables_order = "GPCS"/variables_order = "EGPCS"/g'
/etc/php5/apache2/php.ini  
  
# Set Apache environment variables (can be changed on docker run with -e)  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_SERVERADMIN admin@localhost  
ENV APACHE_SERVERNAME localhost  
ENV POSTGRES_DEFAULTDB defaultdb  
ENV POSTGRES_HOST localhost  
ENV POSTGRES_PORT 5432  
ADD run.sh /run.sh  
  
RUN chmod -v +x /run.sh  
  
EXPOSE 80  
CMD ["/run.sh"]  

