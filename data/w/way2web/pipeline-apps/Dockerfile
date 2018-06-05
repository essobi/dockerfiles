FROM php:7.1-cli  
  
MAINTAINER Way2Web <developers@way2web.nl>  
  
RUN DEBIAN_FRONTEND=noninteractive  
  
ARG TZ=Europe/Amsterdam  
ENV TZ ${TZ}  
  
# add the mysql key  
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys 5072E1F5  
  
# Prepare and install mysql  
RUN echo "mysql-community-server mysql-community-server/root-pass password
root" | debconf-set-selections &&\  
echo "mysql-community-server mysql-community-server/re-root-pass password
root" | debconf-set-selections &&\  
echo "mysql-apt-config mysql-apt-config/enable-repo select mysql-5.6" |
debconf-set-selections &&\  
curl -sSL http://repo.mysql.com/mysql-apt-config_0.2.1-1debian7_all.deb -o
./mysql-apt-config_0.2.1-1debian7_all.deb &&\  
dpkg -i mysql-apt-config_0.2.1-1debian7_all.deb  
  
# Install dependencies  
RUN apt-get update && apt-get install --no-install-recommends -y \  
mysql-community-server \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libcurl4-nss-dev \  
libc-client-dev \  
libkrb5-dev \  
firebird2.5-dev \  
libicu-dev \  
libxml2-dev \  
libxslt1-dev \  
libbz2-dev \  
ssmtp \  
git \  
mercurial \  
zip \  
xvfb gtk2-engines-pixbuf xfonts-cyrillic xfonts-100dpi xfonts-75dpi xfonts-
base xfonts-scalable imagemagick x11-apps  
  
# Install PHP extensions  
RUN docker-php-ext-install -j$(nproc) bz2 &&\  
docker-php-ext-install -j$(nproc) mcrypt &&\  
docker-php-ext-install -j$(nproc) curl &&\  
docker-php-ext-install -j$(nproc) mbstring &&\  
docker-php-ext-install -j$(nproc) iconv &&\  
docker-php-ext-install -j$(nproc) interbase &&\  
docker-php-ext-install -j$(nproc) intl &&\  
docker-php-ext-install -j$(nproc) soap &&\  
docker-php-ext-install -j$(nproc) xmlrpc &&\  
docker-php-ext-install -j$(nproc) xsl &&\  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ &&\  
docker-php-ext-install -j$(nproc) gd &&\  
docker-php-ext-configure imap --with-kerberos --with-imap-ssl &&\  
docker-php-ext-install imap &&\  
docker-php-ext-install mysqli pdo pdo_mysql &&\  
docker-php-ext-install zip  
  
RUN docker-php-ext-configure pcntl --enable-pcntl && \  
docker-php-ext-install pcntl  
  
# Install Composer for Laravel/Codeigniter, NodeJS and other dependencies  
RUN curl -sSL https://deb.nodesource.com/setup_6.x | bash - &&\  
apt-get -y --no-install-recommends install nodejs &&\  
curl -sSL https://getcomposer.org/installer | php -- --filename=composer
--install-dir=/usr/bin &&\  
curl -sSL https://phar.phpunit.de/phpunit.phar -o /usr/bin/phpunit && chmod +x
/usr/bin/phpunit &&\  
curl -sSL http://codeception.com/codecept.phar -o /usr/bin/codecept && chmod
+x /usr/bin/codecept &&\  
curl -sSL https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar -o
/usr/bin/phpcs && chmod +x /usr/bin/phpcs &&\  
curl -sSL http://static.phpmd.org/php/latest/phpmd.phar -o /usr/bin/phpmd &&
chmod +x /usr/bin/phpmd &&\  
curl -sSL https://phar.phpunit.de/phpcpd.phar -o /usr/bin/phpcpd && chmod +x
/usr/bin/phpcpd &&\  
curl -o- -L https://yarnpkg.com/install.sh | bash  
  
#Install chrome - needed for Laravel Dusk  
RUN curl -sS https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key
add - && \  
sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable
main" >> /etc/apt/sources.list.d/google-chrome.list' && \  
apt-get update && apt-get install -y google-chrome-stable  
  
# Clean up APT when done  
RUN apt-get autoclean &&\  
apt-get clean &&\  
apt-get autoremove &&\  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

