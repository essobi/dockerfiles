FROM jedisct1/phusion-baseimage-latest:16.04  
  
RUN (curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -) \  
&& (curl -sS http://nginx.org/keys/nginx_signing.key | sudo apt-key add -) \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" \  
| sudo tee /etc/apt/sources.list.d/yarn.list \  
&& echo "deb http://nginx.org/packages/mainline/ubuntu/ xenial nginx" \  
| sudo tee /etc/apt/sources.list.d/nginx.list \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive \  
apt-get install -yq --no-install-recommends \  
apt-utils \  
software-properties-common \  
apt-transport-https \  
python-software-properties \  
build-essential \  
language-pack-en-base \  
&& curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& DEBIAN_FRONTEND=noninteractive \  
apt-get install -yq \  
nginx \  
nodejs \  
yarn \  
python \  
curl \  
zip \  
&& LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive \  
apt-get install -yq --force-yes \  
php7.1-cli \  
php7.1-fpm \  
php7.1-mysql \  
php7.1-pgsql \  
php7.1-sqlite3 \  
php7.1-ldap \  
php7.1-curl \  
php7.1-gd \  
php7.1-mcrypt \  
php7.1-mbstring \  
php7.1-intl \  
php7.1-xmlrpc \  
php7.1-json \  
php7.1-bz2 \  
php7.1-tidy \  
php7.1-opcache \  
php7.1-xml \  
php7.1-xsl \  
php7.1-yaml \  
php7.1-zip \  
composer \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& sed -i "s/;date.timezone =.*/date.timezone = UTC/" \  
/etc/php/7.1/fpm/php.ini \  
/etc/php/7.1/cli/php.ini \  
&& sed -i "/listen\./s/www-data/nginx/g" /etc/php/7.1/fpm/pool.d/www.conf \  
&& sed -i "s/;daemonize\s*=\s*yes/daemonize = no/" /etc/php/7.1/fpm/php-
fpm.conf \  
&& sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php/7.1/fpm/php.ini
\  
&& sed -i "s/;clear_env\s*=\s*no/clear_env = no/"
/etc/php/7.1/fpm/pool.d/www.conf \  
&& mkdir -p \  
/var/www \  
/run/php \  
/etc/service/nginx \  
/etc/service/phpfpm  
  
COPY nginx.conf /etc/nginx/  
COPY etc/*.conf /etc/nginx/conf.d/  
  
COPY nginx.sh /etc/service/nginx/run  
COPY phpfpm.sh /etc/service/phpfpm/run  
  
RUN chmod +x \  
/etc/service/nginx/run \  
/etc/service/phpfpm/run && \  
ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log  
  
EXPOSE 80  

