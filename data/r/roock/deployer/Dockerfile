FROM php:7.1-cli  
  
MAINTAINER Roman Pertl <roman@pertl.org>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo "memory_limit=-1" > "$PHP_INI_DIR/conf.d/memory-limit.ini" \  
&& echo "date.timezone=Europe/Vienna" >
"$PHP_INI_DIR/conf.d/date_timezone.ini"  
  
VOLUME /root/composer  
ENV PATH "/composer/vendor/bin:$PATH"  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_HOME /composer  
ENV COMPOSER_VERSION 1.6.4  
# Packages  
RUN apt-get update && \  
apt-get install --no-install-recommends -y \  
libmcrypt-dev \  
libbz2-dev \  
zlib1g-dev \  
openssh-client \  
rsync \  
sed \  
ca-certificates \  
curl \  
libcurl4-gnutls-dev \  
git \  
unzip \  
bzip2 \  
libxml2 \  
libxml2-dev \  
libxslt1.1 \  
wget && \  
apt-get upgrade -y  
  
# PHP Extensions  
RUN docker-php-ext-install bcmath mcrypt zip bz2 mbstring pcntl xml curl soap  
  
# Cleanup  
RUN apt-get clean && \  
rm -r /var/lib/apt/lists/*  
  
# Setup the Composer installer  
RUN curl --max-redirs 3 -o /tmp/composer-setup.php
https://getcomposer.org/installer \  
&& curl --max-redirs 3 -o /tmp/composer-setup.sig
https://composer.github.io/installer.sig \  
&& php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php'))
!== trim(file_get_contents('/tmp/composer-setup.sig'))) {
unlink('/tmp/composer-setup.php'); echo 'Invalid installer' . PHP_EOL;
exit(1); }"  
  
# Install Composer  
RUN php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin
--filename=composer --version=${COMPOSER_VERSION} && rm -rf /tmp/composer-
setup.php  
COPY ./set-composer-password.sh /usr/local/bin/set-composer-password.sh  
RUN chmod +x /usr/local/bin/set-composer-password.sh  
  
RUN composer global require deployer/deployer:6.1.0 deployer/recipes:6.0.2  
  

