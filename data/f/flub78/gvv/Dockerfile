# Dockerfile to build a gvv container  
FROM php:5.6-apache  
MAINTAINER Frédéric Peignot frederic.peignot@free.fr  
  
# Define environment variables in the container  
ENV MAINTAINER "Frédéric Peignot"  
ARG MYSQL_ROOT_PASSWORD=mysql_password  
ARG REVISION="-r 2285"  
ARG SVN_VERSION='trunk/gvv'  
# install packages  
# ----------------  
RUN apt-get update  
RUN apt-get install -y subversion \  
less \  
php5-curl php5-dev php5-gd \  
libfreetype6-dev libjpeg62-turbo-dev libmcrypt-dev libpng12-dev \  
phpunit  
  
# Packages for debuging, ifconfig, etc.  
RUN apt-get install -y net-tools \  
vim \  
wget  
  
# Install mysql with no password  
# ------------------------------  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-server \  
mysql-client  
  
# Create the database  
# -------------------  
# allow database connections from other machines  
RUN sed -i '/bind-address/s/^/# /' /etc/mysql/my.cnf  
ADD mysql/create_db.sql /tmp/  
ADD mysql/init_db.sh /tmp/  
RUN /tmp/init_db.sh  
  
# Install PDO MySQL driver  
# See https://github.com/docker-library/php/issues/62  
RUN docker-php-ext-install pdo mysql  
RUN docker-php-ext-install pdo mysqli  
RUN docker-php-ext-install -j$(nproc) iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd  
  
# Configure apache  
# ----------------  
ADD apache2/servername.conf /etc/apache2/conf-available  
RUN a2enconf servername  
RUN a2enmod rewrite  
ADD apache2/php.ini-development /usr/local/etc/php/php.ini  
  
ADD apache2/sites-available/gvv.conf /etc/apache2/sites-available  
  
RUN a2ensite gvv  
  
# Fetch GVV sources  
# -----------------  
RUN cd /var/www/html && \  
svn export $REVISION http://subversion.developpez.com/projets/gvv/trunk/gvv  
  
# Configure GVV  
# -------------  
RUN chmod a+w /var/www/html/gvv/application/config/club.php \  
/var/www/html/gvv/application/config/facturation.php \  
/var/www/html/gvv/assets/images \  
/var/www/html/gvv/uploads  
  
ADD gvv/config/config.php /var/www/html/gvv/application/config  
ADD gvv/config/database.php /var/www/html/gvv/application/config  
  
ADD html/index.html /var/www/html  
ADD html/index.php /var/www/html  
  
# Miscelaneous  
# ------------  
EXPOSE 80  
EXPOSE 22  
RUN useradd -ms /bin/bash frederic  
  
ENTRYPOINT service mysql start && \  
apache2-foreground  
  

