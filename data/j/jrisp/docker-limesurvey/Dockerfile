FROM php:7-apache  
  
MAINTAINER Jeremy RICHARD <jri@sciencespo.paris>  
  
ENV LIMESURVEY_VERSION=2.67.2+170728  
ENV
LIMESURVEY_URL=https://github.com/LimeSurvey/LimeSurvey/archive/${LIMESURVEY_VERSION}.tar.gz  
  
ENV ROOT_DIR=/var/www/html  
  
RUN apt-get update \  
# Install Postgre PDO  
&& apt-get install -y libpq-dev \  
&& docker-php-ext-configure pgsql -with-pgsql=/usr/local/pgsql \  
&& docker-php-ext-install pdo pdo_pgsql pgsql pdo_mysql \  
# Install GD  
&& apt-get install -y libfreetype6-dev libjpeg62-turbo-dev libpng12-dev \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
# Install LDAP  
&& apt-get install libldap2-dev -y \  
&& docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ \  
&& docker-php-ext-install ldap \  
# Install zip  
&& apt-get install -y zlib1g-dev \  
&& docker-php-ext-install zip \  
# Install imap  
&& apt-get install -y libc-client-dev libkrb5-dev \  
&& docker-php-ext-configure imap --with-kerberos --with-imap-ssl \  
&& docker-php-ext-install imap \  
# Clean  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Download and install Limesurvey  
# then Move content to Apache root folder  
RUN cd $ROOT_DIR \  
&& curl --location $LIMESURVEY_URL | tar --extract --gunzip --verbose --strip
1 \  
&& chown --recursive www-data:www-data $ROOT_DIR  
  
COPY config.docker.php $ROOT_DIR/application/config/  
  
COPY entrypoint.sh /entrypoint.sh  
  
VOLUME $ROOT_DIR/upload  
  
EXPOSE 80  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["apache2-foreground"]  

