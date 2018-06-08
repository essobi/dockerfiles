FROM jenkinsci/slave  
  
ARG uid=1000  
ARG gid=1000  
  
USER root  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN groupmod -g ${gid} jenkins  
RUN usermod -u ${uid} -g ${gid} jenkins  
  
RUN apt-get update && \  
apt-get install -yqqm \  
curl \  
wget \  
apt-transport-https \  
lsb-release \  
ca-certificates \  
git  
RUN wget -O- https://packages.sury.org/php/apt.gpg | apt-key add - \  
&& echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" >
/etc/apt/sources.list.d/php.list  
RUN apt-get update -yqq \  
&& apt-get install -yqqm \  
vim \  
locales \  
libpng-dev \  
php5.6-fpm \  
php5.6-mysql \  
php5.6-gd \  
php5.6-imagick \  
php5.6-dev \  
php5.6-curl \  
php5.6-opcache \  
php5.6-cli \  
php5.6-sqlite \  
php5.6-intl \  
php5.6-tidy \  
php5.6-imap \  
php5.6-json \  
php5.6-pspell \  
php5.6-recode \  
php5.6-common \  
php5.6-sybase \  
php5.6-sqlite3 \  
php5.6-bz2 \  
php5.6-common \  
php5.6-memcached \  
php5.6-redis \  
php5.6-xml \  
php5.6-shmop \  
php5.6-mbstring \  
php5.6-zip \  
php5.6-soap \  
php5.6-xml \  
php-xdebug \  
&& phpenmod xdebug  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN curl -sS https://deb.nodesource.com/setup_9.x | bash - \  
&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN apt-get update -yqq && apt-get install nodejs yarn -yqq  
  
RUN chown -R jenkins:jenkins /home/jenkins  
  
RUN wget http://phpdox.de/releases/phpdox.phar \  
&& chmod +x phpdox.phar \  
&& mv phpdox.phar /usr/local/bin/phpdox  
  
USER jenkins  
  
ENV PATH /home/jenkins/.composer/vendor/bin:$PATH  
  
RUN composer global require \  
phpunit/phpunit \  
phploc/phploc \  
pdepend/pdepend \  
phpmd/phpmd \  
sebastian/phpcpd \  
phing/phing \  
jakub-onderka/php-parallel-lint \  
drupal/coder \  
drush/drush \  
wp-cli/wp-cli \  
\--no-progress --no-interaction \  
&& composer global require dealerdirect/phpcodesniffer-composer-installer
--no-progress --no-interaction  

