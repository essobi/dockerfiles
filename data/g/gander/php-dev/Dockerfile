FROM php:7.0  
ARG DEV_USER_UID=1000  
ARG PHING2_VERSION=2.16.0  
ARG PHPUNIT5_VERSION=5.7  
ARG PHPUNIT6_VERSION=6.5  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y --no-install-recommends \  
openssh-client \  
sudo \  
git \  
wget \  
curl \  
cron \  
nano \  
libicu-dev \  
libmcrypt-dev \  
libpq-dev \  
libpng12-dev \  
libjpeg62-turbo-dev \  
libfreetype6-dev \  
libxslt-dev \  
libtidy-dev \  
&& rm -r /var/lib/apt/lists/*  
  
RUN pecl install xdebug \  
&& pecl install mongodb \  
&& docker-php-ext-enable mongodb \  
&& docker-php-ext-install bcmath \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install intl \  
&& docker-php-ext-install mbstring \  
&& docker-php-ext-install mcrypt \  
&& docker-php-ext-install opcache \  
&& docker-php-ext-install pcntl \  
&& docker-php-ext-install pdo_mysql \  
&& docker-php-ext-install pdo_pgsql \  
&& docker-php-ext-install soap \  
&& docker-php-ext-install sockets \  
&& docker-php-ext-install zip  
  
RUN curl -LsS http://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer  
RUN curl -LsS http://symfony.com/installer -o /usr/local/bin/symfony && chmod
a+x /usr/local/bin/symfony  
RUN curl -LSs http://box-project.github.io/box2/installer.php | php && mv
box.phar /usr/local/bin/box  
RUN curl -LsS http://www.phing.info/get/phing-${PHING2_VERSION}.phar -o
/usr/local/bin/phing && chmod +x /usr/local/bin/phing  
RUN curl -LsS http://phar.phpunit.de/phpunit-${PHPUNIT5_VERSION}.phar -o
/usr/local/bin/phpunit5 && chmod +x /usr/local/bin/phpunit5  
RUN curl -LsS http://phar.phpunit.de/phpunit-${PHPUNIT6_VERSION}.phar -o
/usr/local/bin/phpunit6 && chmod +x /usr/local/bin/phpunit6  
RUN curl -LsS http://deployer.org/deployer.phar -o /usr/local/bin/dep && chmod
+x /usr/local/bin/dep  
  
RUN ln -s /usr/local/bin/phpunit5 /usr/local/bin/phpunit  
  
ADD rootfs /  
  
RUN printf "alias l='ls -CF'\nalias la='ls -A'\nalias ll='ls -alF'\n" >>
/etc/bash.bashrc  
RUN printf "if [ -d \"\$HOME/.composer/vendor/bin\" ]; then\n
PATH=\"\$HOME/.composer/vendor/bin:\$PATH\"\nfi" >> /etc/bash.bashrc  
  
RUN adduser --disabled-password --gecos '' \--uid ${DEV_USER_UID} dev \  
&& adduser dev sudo \  
&& printf "dev ALL=(ALL) NOPASSWD: ALL\n" > /etc/sudoers.d/dev  
  
USER dev  
  
VOLUME /app  
WORKDIR /app  
  
EXPOSE 80  
ENTRYPOINT ["sudo", "docker-php-entrypoint"]  
CMD ["sudo", "php", "-S", "0.0.0.0:80", "-t", "/app/public"]  

