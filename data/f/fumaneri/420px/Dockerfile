FROM ubuntu:latest  
  
# Update apt-get  
RUN apt-get -y update  
  
# Install apache, PHP, and supplimentary programs.  
RUN apt-get -y install \  
curl \  
apache2 \  
php7.0 \  
php7.0-cli \  
libapache2-mod-php7.0 \  
php7.0-gd \  
php7.0-json \  
php7.0-ldap \  
php7.0-mbstring \  
php7.0-mysql \  
php7.0-pgsql \  
php7.0-sqlite3 \  
php7.0-xml \  
php7.0-xsl \  
php7.0-zip \  
php7.0-soap \  
php7.0-curl  
  
# Enable apache mods.  
RUN a2enmod rewrite  
RUN /etc/init.d/apache2 restart  
  
# Install Composer and make it available in the PATH  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN mkdir -p /usr/src/app/ && rm -fr /var/www/html && ln -s /usr/src/app/
/var/www/html  
WORKDIR /usr/src/app/  
  
# Copy the content of the current dir (and sub-dir) to the container's
'WORKDIR'.  
COPY . /usr/src/app/  
  
# Install dependencies with Composer  
RUN composer install --prefer-source --no-interaction  
  
# Expose apache  
EXPOSE 80  
# Specify the command to execute to start the container.  
ENTRYPOINT []  
# By default start up apache in the foreground, override with /bin/bash for
interative.  
CMD /usr/sbin/apache2ctl -D FOREGROUND

