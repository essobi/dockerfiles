FROM php:5.6-apache  
  
# copy custom php.ini  
COPY config/php.ini /usr/local/etc/php/  
  
# install the PHP extensions we need  
RUN set -ex; \  
\  
savedAptMark="$(apt-mark showmanual)"; \  
\  
apt-get update; \  
apt-get install -y --no-install-recommends \  
libjpeg-dev \  
libpng-dev \  
htop \  
imagemagick \  
; \  
\  
docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr; \  
docker-php-ext-install gd mysqli opcache; \  
\  
# reset apt-mark's "manual" list so that "purge --auto-remove" will remove all
build dependencies  
apt-mark auto '.*' > /dev/null; \  
apt-mark manual $savedAptMark; \  
ldd "$(php -r 'echo ini_get("extension_dir");')"/*.so \  
| awk '/=>/ { print $3 }' \  
| sort -u \  
| xargs -r dpkg-query -S \  
| cut -d: -f1 \  
| sort -u \  
| xargs -rt apt-mark manual; \  
\  
apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false;
\  
rm -rf /var/lib/apt/lists/*  
  
# install imap ext  
RUN apt-get update && apt-get install -y libc-client-dev libkrb5-dev && rm -r
/var/lib/apt/lists/*  
RUN docker-php-ext-configure imap --with-kerberos --with-imap-ssl \  
&& docker-php-ext-install imap  
  
# install curl ext  
RUN apt-get update && apt-get install -y libcurl3-dev libcurl4-openssl-dev &&
rm -r /var/lib/apt/lists/*  
RUN docker-php-ext-install curl  
  
# install mcrypt ext  
RUN apt-get update && apt-get install -y libmcrypt-dev libreadline-dev && rm
-r /var/lib/apt/lists/*  
RUN docker-php-ext-install mcrypt  
  
# install other ext  
RUN docker-php-ext-install mbstring zip  
  
# install pecl extensions  
#RUN pecl install imagick-3.4.3 && docker-php-ext-enable imagick  
RUN apt-get update && apt-get install -y libmagickwand-dev --no-install-
recommends && rm -rf /var/lib/apt/lists/*  
RUN pecl install imagick-3.4.3 && docker-php-ext-enable imagick  
  
# install sudo  
RUN apt-get update && apt-get install --fix-missing -y sudo && rm -r
/var/lib/apt/lists/*  
  
# Create new web user for apache and grant sudo without password  
RUN useradd web -d /var/www -g www-data -s /bin/bash  
RUN usermod -aG sudo web  
RUN echo 'web ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
  
# Apache2 config  
COPY config/apache2.conf /etc/apache2  
#COPY core/envvars /etc/apache2  
COPY core/other-vhosts-access-log.conf /etc/apache2/conf-enabled/  
RUN rm /etc/apache2/sites-enabled/000-default.conf  
  
# set recommended PHP.ini settings  
# see https://secure.php.net/manual/en/opcache.installation.php  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=2'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  
  
RUN rm -rf /var/www/html && \  
mkdir -p /var/lock/apache2 /var/run/apache2 /var/log/apache2 /var/www/html &&
\  
chown -R web:www-data /var/lock/apache2 /var/run/apache2 /var/log/apache2
/var/www/html  
RUN a2enmod rewrite expires ssl  
  
# installation of ssmtp  
#RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install --fix-
missing -y ssmtp && rm -r /var/lib/apt/lists/*  
#ADD core/ssmtp.conf /etc/ssmtp/ssmtp.conf  
#ADD core/php-smtp.ini /usr/local/etc/php/conf.d/php-smtp.ini  
#ADD core/revaliases /etc/ssmtp/revaliases  
# install msmtp  
RUN set -x \  
&& DEBIAN_FRONTEND=noninteractive \  
&& apt-get update && apt-get install -y --no-install-recommends msmtp && rm -r
/var/lib/apt/lists/*  
ADD core/msmtprc.conf /usr/local/etc/msmtprc  
ADD core/php-smtp.ini /usr/local/etc/php/conf.d/php-smtp.ini  
  
VOLUME /var/www/html  
  
# create directory for ssh keys  
RUN mkdir /var/www/.ssh/  
RUN chown -R web:www-data /var/www/  
  
# Set timezone to Europe/Paris  
RUN echo "Europe/Paris" > /etc/timezone && dpkg-reconfigure -f noninteractive
tzdata  
  
# Expose 80,443 for apache  
EXPOSE 80 443  
# Add web and root .bashrc config  
# When you "docker exec -it" into the container, you will be switched as web
user and placed in /var/www/html  
RUN echo "exec su - web" > /root/.bashrc && \  
echo ". .profile" > /var/www/.bashrc && \  
echo "alias ll='ls -al'" > /var/www/.profile && \  
echo "cd /var/www/html" >> /var/www/.profile  
  
# Set and run a custom entrypoint  
COPY core/docker-entrypoint.sh /  
RUN chmod 777 /docker-entrypoint.sh && chmod +x /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  

