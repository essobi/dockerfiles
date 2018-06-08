FROM php:5.4-fpm  
MAINTAINER Jonas Renggli <jonas.renggli@swisscom.com>  
  
# Install general utilities  
RUN apt-get update \  
&& apt-get install -y \  
vim \  
net-tools \  
procps \  
telnet \  
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
RUN buildRequirements="libpng12-dev libjpeg-dev" \  
&& apt-get update && apt-get install -y ${buildRequirements} \  
&& docker-php-ext-configure gd --with-jpeg-dir=/usr/lib \  
&& docker-php-ext-install gd \  
&& apt-get purge -y ${buildRequirements} \  
&& rm -rf /var/lib/apt/lists/*  
# pdo_mysql  
RUN docker-php-ext-install pdo_mysql  
  
# mysqli  
RUN docker-php-ext-install mysqli  
  
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
&& pecl install yaml \  
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
RUN git clone https://github.com/zendtech/ZendOptimizerPlus
/tmp/ZendOptimizerPlus \  
&& cd /tmp/ZendOptimizerPlus \  
&& /usr/local/bin/phpize \  
&& ./configure \  
\--with-php-config=/usr/local/bin/php-config \  
&& make \  
&& make install \  
&& echo "zend_extension=/usr/local/lib/php/extensions/no-debug-non-
zts-20100525/opcache.so" > /usr/local/etc/php/conf.d/ext-opcache.ini \  
&& cd / \  
&& rm -rf /tmp/ZendOptimizerPlus  
  
# create symlink to support standard /usr/bin/php  
ln -s /usr/local/bin/php /usr/bin/php  
  
# locales  
ADD assets/locale.gen /etc/locale.gen  
RUN apt-get update \  
&& apt-get install -y locales \  
&& rm -r /var/lib/apt/lists/* \  
&& locale-gen  
  
# Activate login for user www-data  
RUN chsh www-data -s /bin/bash  
  
ADD assets/php.ini /usr/local/etc/php/conf.d/php.ini  
ADD assets/Settings.yaml.docker /opt/docker/Settings.yaml.docker  
ADD assets/entrypoint.sh /entrypoint.sh  
  
RUN apt-get update \  
&& apt-get install -y ssmtp \  
&& rm -r /var/lib/apt/lists/*  
ADD assets/ssmtp.conf /opt/docker/ssmtp.conf  
  
WORKDIR /data/web/releases/current  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["php-fpm"]  

