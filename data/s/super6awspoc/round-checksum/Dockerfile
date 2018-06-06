FROM alpine:3.4  
  
MAINTAINER InfinityWorks  
  
RUN apk add --no-cache \  
curl \  
netcat-openbsd \  
tcpdump \  
php5-common \  
php5 \  
php5-intl \  
php5-cli \  
php5-fpm \  
php5-opcache \  
php5-pdo \  
php5-pdo_mysql \  
php5-mysql \  
php5-mysqli \  
php5-ctype \  
php5-curl \  
php5-json \  
php5-xml \  
php5-openssl \  
php5-gettext \  
php5-pcntl \  
php5-phar  
  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v1.9.1.3/s6-overlay-amd64.tar.gz /tmp/  
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C / && \  
echo "date.timezone=UTC" >> /etc/php5/php.ini && \  
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \  
php composer-setup.php && \  
php -r "unlink('composer-setup.php');" && \  
mv composer.phar /bin && \  
touch /var/log/update.log /var/log/checksum.log /var/log/cron.log && \  
chown cron:cron /var/log/update.log /var/log/checksum.log /var/log/cron.log  
COPY app/ /app  
COPY etc/ /etc  
  
RUN cd /app && composer.phar install --no-dev -o  
  
USER root  
  
CMD "/init"  

