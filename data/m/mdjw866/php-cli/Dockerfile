FROM php:7-fpm  
MAINTAINER M.D.Ward <dev@mattdw.co.uk>  
  
# Install build dependencies  
RUN apt-get update && \  
apt-get install -fy --no-install-recommends \  
openssh-client rsync bzip2 libsasl2-dev \  
libmcrypt-dev librabbitmq-dev libbz2-dev \  
librecode0 libpng12-0 && \  
rm -rf /var/lib/apt/lists/*  
  
RUN buildDeps=" \  
$PHP_EXTRA_BUILD_DEPS \  
libcurl4-openssl-dev \  
libreadline6-dev \  
librecode-dev \  
libsqlite3-dev \  
libssl-dev \  
libxml2-dev \  
libpng12-dev \  
xz-utils \  
" \  
&& apt-get update && apt-get install -y $buildDeps \--no-install-recommends &&
rm -rf /var/lib/apt/lists/* \  
&& (for EXT in mbstring intl zip bz2 pdo pdo_mysql pdo_pgsql pdo_odbc phar
reflection standard simplexml xml sockets gd; \  
do \  
docker-php-ext-install $EXT; \  
docker-php-ext-enable $EXT; \  
done; \  
for EXT in apcu-5.1.2 mongodb-1.1.6; \  
do \  
EXT_NAME=$(echo $EXT | sed "s/-.\\+$//"); \  
printf "\n" | pecl install $EXT \  
&& echo "extension=$EXT_NAME.so" > $PHP_INI_DIR/conf.d/$EXT_NAME.ini; \  
done; \  
echo "date.timezone=Europe/London" > $PHP_INI_DIR/conf.d/date-timezone.ini) \  
&& { find /usr/local/bin /usr/local/sbin -type f -executable -exec strip
--strip-all '{}' \+ || true; } \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false -o
APT::AutoRemove::SuggestsImportant=false $buildDeps  
  
CMD ["php", "-a"]  

