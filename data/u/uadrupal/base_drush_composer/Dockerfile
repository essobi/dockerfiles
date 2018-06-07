FROM debian:stretch  
  
RUN set -e \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \  
curl \  
git \  
php7.0-bcmath \  
php7.0-bz2 \  
php7.0-cli \  
php7.0-curl \  
php7.0-gd \  
php7.0-ldap \  
php7.0-mbstring \  
php7.0-mcrypt \  
php7.0-mysql \  
php7.0-xsl \  
php7.0-zip \  
wget \  
zip \  
&& ln -fs /usr/share/zoneinfo/America/Phoenix /etc/localtime \  
&& dpkg-reconfigure -f noninteractive tzdata \  
&& rm -r /var/lib/apt/lists/*  
  
ENV COMPOSER_ALLOW_SUPERUSER=1 \  
COMPOSER_HOME='/composer' \  
COMPOSER_VERSION='1.5.2' \  
DRUSH_VERSION='8.1.13' \  
PATH="/composer/vendor/bin:${PATH}" \  
PHPINI='/etc/php/7.0/cli'  
  
RUN echo 'memory_limit=-1' > "${PHPINI}/conf.d/memory-limit.ini" \  
&& echo "date.timezone=${PHP_TIMEZONE:-America/Phoenix}" >
"${PHPINI}/conf.d/date_timezone.ini" \  
&& installer='/tmp/installer.php' \  
&& curl -fsSL -o "$installer" 'https://getcomposer.org/installer' \  
&& sig_expect=$(curl -fsSL 'https://composer.github.io/installer.sig' ) \  
&& sig_got=$(php -r "echo hash_file('SHA384', '${installer}');") \  
&& [ "$sig_got" = "$sig_expect" ] \  
&& php "$installer" \--no-ansi --install-dir='/usr/local/bin'
\--filename=composer --version="$COMPOSER_VERSION" \  
&& rm "$installer" \  
&& composer --ansi --version --no-interaction \  
&& drushpath="/usr/local/bin/drush" \  
&& curl -fsSL -o "$drushpath" "https://github.com/drush-
ops/drush/releases/download/${DRUSH_VERSION}/drush.phar" \  
&& chmod 755 "$drushpath" \  
&& drush core-status  

