FROM alpine:3.5  
MAINTAINER Martin Hoffesommer <3dcoder@gmail.com>  
  
ENV S6VERSION 1.17.2.0  
ENV PATH=/.composer/vendor/bin:$PATH  
  
COPY rootfs /  
  
RUN apk add --update \  
wget \  
ca-certificates \  
openssh \  
nginx \  
php5-fpm \  
php5-json \  
php5-zlib \  
php5-bz2 \  
php5-xml \  
php5-phar \  
php5-openssl \  
php5-mcrypt \  
php5-pdo \  
php5-ctype \  
php5-opcache \  
php5-memcache \  
php5-curl \  
su-exec \  
openssl-dev \  
bash \  
  
# Configure PHP  
&& chmod +x /sbin/build-php-extensions \  
&& /sbin/build-php-extensions \  
  
# some ini fixes  
&& echo "extension=apcu.so" > /etc/php5/conf.d/apcu.ini \  
&& echo "extension=mongo.so" > /etc/php5/conf.d/mongo.ini \  
&& echo "extension=mongodb.so" > /etc/php5/conf.d/mongodb.ini \  
  
&& echo "memory_limit=-1" >> /etc/php5/conf.d/docker.ini \  
&& echo "date.timezone=America/Los_Angeles" >> /etc/php5/conf.d/docker.ini \  
&& echo -e
"\n[XDebug]\nxdebug.idekey=\"docker\"\nxdebug.remote_enable=On\nxdebug.remote_connect_back=On\nxdebug.remote_autostart=Off"
>> /etc/php5/conf.d/docker.ini \  
  
# Configure SSHD server  
  
&& ssh-keygen -f /etc/ssh/ssh_host_rsa_key -N '' -t rsa \  
&& echo -e "Host *\n\tStrictHostKeyChecking
no\n\tUserKnownHostsFile=/dev/null\n" > /etc/ssh/ssh_config \  
  
# Create docker user  
  
&& adduser -u 1000 -D -s /bin/ash docker \  
&& echo "docker:docker" | chpasswd \  
  
# Install composer  
  
&& php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \  
&& php composer-setup.php --install-dir=/sbin --filename=composer \  
&& php -r "unlink('composer-setup.php');" \  
  
# Install S6  
  
&& wget https://github.com/just-
containers/s6-overlay/releases/download/v${S6VERSION}/s6-overlay-amd64.tar.gz
-O /tmp/s6-overlay.tar.gz \  
&& tar xvfz /tmp/s6-overlay.tar.gz -C / \  
&& rm -f /tmp/s6-overlay.tar.gz \  
  
## Install global PHP utilities  
  
&& composer global require friendsofphp/php-cs-fixer \  
&& composer global require phing/phing \  
&& composer global require sensiolabs/security-checker \  
  
# Cleanup  
  
&& rm -r /var/www \  
&& apk del wget \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf /tmp/* \  
&& rm -rf /root/.composer/cache  
  
# Expose the ports for nginx, XDebug  
EXPOSE 80 443 22 9000  
VOLUME "/var/www'  
  
ENTRYPOINT [ "/init" ]  

