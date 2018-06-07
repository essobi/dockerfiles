FROM php:5.5-apache  
RUN apt-get update &&\  
apt-get install -y --no-install-recommends \  
libxslt1-dev \  
libpng12-dev \  
htmldoc \  
imagemagick \  
unzip \  
zip \  
openjdk-7-jdk \  
libav-tools \  
mysql-client \  
sendmail \  
git \  
subversion \  
libcurl4-openssl-dev \  
wget \  
ghostscript \  
libmcrypt-dev \  
libldap2-dev &&\  
docker-php-ext-install \  
mysql \  
mysqli \  
mcrypt \  
xsl \  
xml \  
xmlrpc \  
gd \  
zip \  
dom \  
json \  
curl &&\  
docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ &&\  
docker-php-ext-install ldap &&\  
pecl install radius &&\  
docker-php-ext-enable radius &&\  
curl -fsSL
'https://xcache.lighttpd.net/pub/Releases/3.2.0/xcache-3.2.0.tar.gz' -o
/tmp/xcache.tar.gz &&\  
mkdir -p /tmp/xcache &&\  
tar -xf /tmp/xcache.tar.gz -C /tmp/xcache --strip-components=1 &&\  
cd /tmp/xcache &&\  
phpize &&\  
./configure --enable-xcache &&\  
make -j$(nproc) &&\  
make install &&\  
docker-php-ext-enable xcache &&\  
rm -rf /var/lib/apt/lists/* /tmp/*  
  
COPY ini/ /usr/local/etc/php/conf.d/  
ENV ILIAS_VERSION=5.1.4  
#ADD ILIAS-${ILIAS_VERSION}.tar.gz /var/www/html/  
COPY resources/ /var/www/html/ILIAS-${ILIAS_VERSION}/  
COPY iliasdata/ /ilias/  
RUN wget -qO- https://github.com/ILIAS-
eLearning/ILIAS/archive/v${ILIAS_VERSION}.tar.gz | tar xz -C /var/www/html/
&&\  
chmod -R o-rwx /var/www/html/ &&\  
ln -s ILIAS-${ILIAS_VERSION} /var/www/html/ilias &&\  
mkdir -p /var/www/html/ilias/data &&\  
mkdir -p /ilias/data &&\  
mkdir -p /ilias/log &&\  
mkdir -p /ilias/mysqldata &&\  
mkdir -p /var/opt/ilias &&\  
mkdir -p /var/log/ilias/ &&\  
mkdir -p /var/www/html/ilias/data/myilias/css &&\  
mkdir -p /var/www/html/ilias/data/myilias/lm_data &&\  
mkdir -p /var/www/html/ilias/data/myilias/mobs &&\  
mkdir -p /var/www/html/ilias/data/myilias/usr_images &&\  
mkdir -p /ilias/data/myilias/mail &&\  
chown -R www-data:www-data /var/www/html/ILIAS-${ILIAS_VERSION} &&\  
chown -R www-data:www-data /ilias/ &&\  
chown -R www-data:www-data /var/opt/ilias &&\  
chown -R www-data:www-data /var/log/ilias  
VOLUME ["/ilias", "/var/www/html/ilias/data", "/var/log/ilias"]  

