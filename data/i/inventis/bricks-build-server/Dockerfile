FROM php:7.1-cli  
  
LABEL vendor="Inventis BVBA" \  
maintainer="jane@inventis.be" \  
php="7.1"  
  
# install gd, iconv, mcrypt libs  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd  
  
# Install PHP extensions  
RUN apt-get update && apt-get install -y \  
libicu-dev \  
libxml2-dev \  
libmcrypt-dev \  
&& rm -r /var/lib/apt/lists/* \  
&& docker-php-ext-configure pdo_mysql --with-pdo-mysql=mysqlnd \  
&& docker-php-ext-install \  
intl \  
mbstring \  
mcrypt \  
pcntl \  
pdo_mysql \  
zip \  
opcache \  
soap  
  
# Enable appropriate locales  
RUN apt-get update && apt-get install -y \  
locales  
  
RUN echo 'de_DE ISO-8859-1\n \  
de_DE.UTF-8 UTF-8\n \  
de_DE@euro ISO-8859-15\n \  
en_GB ISO-8859-1\n \  
en_GB.ISO-8859-15 ISO-8859-15\n \  
en_US ISO-8859-1\n \  
en_US.ISO-8859-15 ISO-8859-15\n \  
en_US.UTF-8 UTF-8\n \  
fr_FR ISO-8859-1\n \  
fr_FR.UTF-8 UTF-8\n \  
fr_FR@euro ISO-8859-15\n \  
nl_BE ISO-8859-1\n \  
nl_BE.UTF-8 UTF-8\n \  
nl_BE@euro ISO-8859-15\n \  
nl_NL ISO-8859-1\n \  
nl_NL.UTF-8 UTF-8\n \  
nl_NL@euro ISO-8859-15\n' \  
>> /etc/locale.gen && \  
/usr/sbin/locale-gen  
  
# Update timezone  
RUN echo 'Europe/Brussels' > /etc/timezone && \  
dpkg-reconfigure -f noninteractive tzdata  
  
# install composer  
RUN curl https://getcomposer.org/composer.phar -o /usr/local/bin/composer &&
chmod +x /usr/local/bin/composer  
  
# install git  
RUN apt-get install -y git  
  
#install nodejs  
RUN apt-get install -y curl python-software-properties && \  
curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get install nodejs  
  
# install required npm globals  
RUN npm install --silent -g \  
gulp-cli \  
grunt-cli \  
bower \  
yarn  
  
# install bundler  
RUN apt-get install -y ruby-full && \  
gem install bundler -v 1.15.4  
  
# install magallanes v1 gobally  
RUN composer global require andres-montanez/magallanes:^1  
RUN ln -s /root/.composer/vendor/bin/mage /usr/local/bin/mage  
  
COPY ./build.sh /usr/local/bin/build  
  
VOLUME /build  
  
ENTRYPOINT ["/bin/bash"]

