FROM php:5.6-fpm  
MAINTAINER Jonas Renggli <jonas.renggli@swisscom.com>  
  
# Install general utilities  
RUN apt-get update \  
&& apt-get install -y \  
vim \  
net-tools \  
procps \  
telnet \  
netcat \  
&& rm -r /var/lib/apt/lists/*  
# Install utilities used by TYPO3 CMS / Flow / Neos  
RUN apt-get update \  
&& apt-get install -y \  
imagemagick \  
graphicsmagick \  
zip \  
unzip \  
wget \  
curl \  
git \  
mysql-client \  
moreutils \  
dnsutils \  
&& rm -rf /var/lib/apt/lists/*  
# gd  
RUN buildRequirements="libpng12-dev libjpeg-dev libfreetype6-dev" \  
&& apt-get update && apt-get install -y ${buildRequirements} \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/lib \  
&& docker-php-ext-install gd \  
&& apt-get purge -y ${buildRequirements} \  
&& rm -rf /var/lib/apt/lists/*  
  
# pdo_mysql  
RUN docker-php-ext-install pdo_mysql  
  
# mysqli  
RUN docker-php-ext-install mysqli  
  
# mysql  
RUN docker-php-ext-install mysql  
  
# mcrypt  
RUN runtimeRequirements="re2c libmcrypt-dev" \  
&& apt-get update && apt-get install -y ${runtimeRequirements} \  
&& docker-php-ext-install mcrypt \  
&& rm -rf /var/lib/apt/lists/*  
# mbstring  
RUN docker-php-ext-install mbstring  
  
# intl  
RUN buildRequirements="libicu-dev g++" \  
&& apt-get update && apt-get install -y ${buildRequirements} \  
&& docker-php-ext-install intl \  
&& apt-get purge -y ${buildRequirements} \  
&& runtimeRequirements="libicu52" \  
&& apt-get install -y --auto-remove ${runtimeRequirements} \  
&& rm -rf /var/lib/apt/lists/*  
# yaml  
RUN buildRequirements="libyaml-dev" \  
&& apt-get update && apt-get install -y ${buildRequirements} \  
&& pecl install yaml-1.3.1 \  
&& echo "extension=yaml.so" > /usr/local/etc/php/conf.d/ext-yaml.ini \  
&& apt-get purge -y ${buildRequirements} \  
&& rm -rf /var/lib/apt/lists/*  
# imagick  
RUN runtimeRequirements="libmagickwand-6.q16-dev --no-install-recommends" \  
&& apt-get update && apt-get install -y ${runtimeRequirements} \  
&& ln -s /usr/lib/x86_64-linux-gnu/ImageMagick-6.8.9/bin-Q16/MagickWand-config
/usr/bin/ \  
&& pecl install imagick \  
&& echo "extension=imagick.so" > /usr/local/etc/php/conf.d/ext-imagick.ini \  
&& rm -rf /var/lib/apt/lists/*  
# opcache  
RUN docker-php-ext-install opcache  
  
# soap  
RUN docker-php-ext-install soap  
  
# zip  
RUN docker-php-ext-install zip  
  
# redis  
RUN wget -O /tmp/redis.tar.gz
https://github.com/phpredis/phpredis/archive/2.2.7.tar.gz \  
&& mkdir -p /tmp/redis \  
&& tar xzf /tmp/redis.tar.gz -C /tmp/redis --strip-components=1 \  
&& cd /tmp/redis \  
&& phpize \  
&& ./configure \  
&& make \  
&& make install \  
&& echo "extension=redis.so" > /usr/local/etc/php/conf.d/ext-redis.ini \  
&& rm -rf /tmp/redis.tar.gz /tmp/redis  
  
# APCu  
RUN pecl install apcu-4.0.10 \  
&& echo "extension=apcu.so\napc.enable_cli = 1" >
/usr/local/etc/php/conf.d/ext-apcu.ini  
  
# create symlink to support standard /usr/bin/php  
RUN ln -s /usr/local/bin/php /usr/bin/php  
  
# locales  
COPY assets/locale.gen /etc/locale.gen  
RUN apt-get update \  
&& apt-get install -y locales \  
&& rm -r /var/lib/apt/lists/*  
# Activate login for user www-data  
RUN chsh www-data -s /bin/bash  
  
# new home folder for user  
RUN usermod -d /data/web/releases/current www-data  
  
  
COPY assets/php-fpm.conf /usr/local/etc/php-fpm.conf  
COPY assets/php.ini /usr/local/etc/php/conf.d/php.ini  
COPY assets/Settings.yaml.docker /opt/docker/Settings.yaml.docker  
COPY assets/entrypoint.sh /entrypoint.sh  
COPY assets/bin /usr/local/bin  
  
  
RUN apt-get update \  
&& apt-get install -y ssmtp \  
&& rm -rf /var/lib/apt/lists/*  
COPY assets/ssmtp.conf /opt/docker/ssmtp.conf  
  
# Cron  
RUN apt-get update \  
&& apt-get install -y cron \  
&& rm -rf /var/lib/apt/lists/*  
# Workaround ImageMagick CVE-2016-3714  
COPY assets/policy.xml /etc/ImageMagick-6/policy.xml  
  
WORKDIR /data/web/releases/current  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["php-fpm"]  

