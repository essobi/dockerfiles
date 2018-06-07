FROM debian:jessie  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# User settings  
RUN \  
usermod -m -d /srv/www -s /bin/bash www-data && \  
echo "www-data:www-data" | chpasswd && \  
mkdir /var/run/sshd && \  
mkdir -p /srv/www && \  
chown -R www-data:www-data /srv/www  
  
# Install curl and nodejs repo  
RUN \  
apt-get update && apt-get install -y curl && \  
curl -sL https://deb.nodesource.com/setup_5.x | bash - && \  
apt-get install -y nodejs && \  
npm install -g npm && \  
mkdir -p $(npm config get prefix)/{lib/node_modules,bin,share} && \  
chown -R www-data:www-data $(npm config get
prefix)/{lib/node_modules,bin,share} && \  
apt-get -y autoclean && apt-get -y autoremove && rm -rf /var/lib/apt/lists/*  
  
# Install RVM  
RUN \  
curl -sSL https://rvm.io/mpapis.asc | gpg --import \- && \  
curl -sSL https://get.rvm.io | bash -s stable --rails && \  
/bin/bash -l -c "gem install bundler sass compass" && \  
usermod -aG rvm www-data  
  
# Install  
RUN \  
#php-7  
echo "deb http://packages.dotdeb.org jessie all" >
/etc/apt/sources.list.d/php-7.0.list && \  
echo "deb-src http://packages.dotdeb.org jessie all" >>
/etc/apt/sources.list.d/php-7.0.list && \  
apt-get update && apt-get install -y wget && \  
wget https://www.dotdeb.org/dotdeb.gpg && \  
apt-key add dotdeb.gpg && rm -f dotdeb.gpg && \  
#Install  
apt-get update && apt-get install -y \  
postgresql-client \  
mariadb-client \  
openssh-server \  
bash-completion \  
nano \  
mc \  
git \  
wget \  
# PHP 7  
php7.0-cli \  
php7.0-dev \  
php7.0-xdebug \  
php7.0-json \  
php7.0-pgsql \  
php7.0-sqlite3 \  
php7.0-mcrypt \  
php7.0-mongodb \  
php7.0-intl \  
php7.0-gd \  
php7.0-mysql \  
php7.0-redis \  
php7.0-memcached \  
php7.0-bz2 \  
php7.0-curl \  
php7.0-opcache \  
php7.0-igbinary \  
php7.0-xml \  
php7.0-mbstring \  
php7.0-bcmath \  
# PHP 5  
php5-cli \  
php5-mcrypt \  
php5-curl \  
php5-mysql \  
php5-pgsql \  
php5-memcached \  
php5-xdebug \  
php5-intl \  
php5-gd \  
php5-mongo \  
php5-sqlite \  
# phpbrew libraries  
libxml2-dev \  
libmcrypt-dev \  
libbz2-dev \  
libmhash-dev \  
libmhash2 \  
libxslt1-dev \  
libmemcached-dev \  
libgd2-xpm-dev \  
libcurl4-openssl-dev \  
libicu-dev \  
libpq-dev && \  
apt-get clean -y && apt-get autoclean -y && \  
apt-get -y autoremove && rm -rf /var/lib/apt/lists/*  
  
# Install PhpBrew  
RUN \  
curl -L -O https://github.com/phpbrew/phpbrew/raw/master/phpbrew && \  
chmod +x phpbrew && \  
mv phpbrew /usr/local/bin/phpbrew && \  
chown www-data:www-data /usr/local/bin/phpbrew  
  
# Install composer  
RUN \  
curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer && \  
chown www-data:www-data /usr/local/bin/composer && \  
chmod +x /usr/local/bin/composer  
  
# Install drush  
RUN \  
wget http://files.drush.org/drush.phar && \  
php drush.phar core-status && \  
chmod +x drush.phar && \  
mv drush.phar /usr/local/bin/drush && \  
chown www-data:www-data /usr/local/bin/drush  
  
# Setting php-cli for symfony  
RUN echo "date.timezone = Europe/Minsk" >> /etc/php/7.0/cli/php.ini  
  
# Problem http://goo.gl/UcMZ9a  
RUN echo 'KexAlgorithms curve25519-sha256@libssh.org,ecdh-sha2-nistp256,ecdh-
sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group-exchange-sha256,diffie-
hellman-group14-sha1,diffie-hellman-group1-sha1' >> /etc/ssh/sshd_config  
  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
EXPOSE 22  
  
ENTRYPOINT ["/usr/sbin/sshd"]  
CMD ["-D"]  

