FROM php:apache  
  
RUN apt-get update && \  
apt-get install -y \  
# needed tools  
supervisor \  
pdf2htmlex \  
pdftk \  
curl \  
poppler-utils \  
imagemagick \  
# tools for extension building (will be remove later)  
zlib1g-dev \  
libicu-dev \  
g++ \  
libc-client-dev \  
libkrb5-dev \  
cron \  
&& \  
  
# configure php extensions  
docker-php-ext-configure intl && \  
docker-php-ext-configure imap --with-kerberos --with-imap-ssl && \  
  
# install php extensions  
docker-php-ext-install \  
pdo_mysql \  
intl \  
opcache \  
imap \  
zip \  
&& \  
pecl install -o -f inotify && \  
pecl install -o -f redis && \  
docker-php-ext-enable \  
inotify \  
redis \  
&& \  
# clean up packages  
rm -rf /tmp/pear && \  
apt-get remove -y \  
g++ \  
libkrb5-dev \  
&& \  
docker-php-source delete && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/* && \  
  
# install composer  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN adduser apache  
  
WORKDIR /app  
  
# create directories  
# app directory  
RUN mkdir -p /app/var/logs/ && \  
  
# files directory  
mkdir -p /data && \  
chown -R apache:apache /data && \  
chmod -R 775 /data && \  
  
# inbox directory  
mkdir -p /inbox && \  
chown -R apache:apache /inbox && \  
chmod -R 775 /inbox  
  
ADD ./apache.conf /etc/apache2/sites-available/000-default.conf  
ADD ./supervisor.conf /etc/supervisord.conf  
ADD inbox.cron /etc/cron.d  
  
ADD ./app /app  
  
RUN composer install  
  
RUN chmod 664 /etc/cron.d/inbox.cron && \  
crontab /etc/cron.d/inbox.cron && \  
rm -rf /app/var/cache/* && \  
rm -rf /app/var/logs/* && \  
rm -rf /app/var/sessions/* && \  
chown -R apache:apache /app && \  
rm -rf /app/var/cache/prod/* && \  
a2enmod rewrite  
  
# for development only  
# VOLUME /app  
VOLUME /data  
VOLUME /inbox  
  
ENV APACHE_RUN_USER apache  
ENV APACHE_RUN_GROUP apache  
ENV MYSQL_DATABASE documents  
ENV MYSQL_USER documents  
ENV MYSQL_PASSWORD documents  
  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]

