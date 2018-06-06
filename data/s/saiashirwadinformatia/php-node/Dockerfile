# PHP-Node based image with Yarn-Grunt-Gulp-Bower-Composer components support  
FROM ubuntu:16.04  
  
MAINTAINER Rohan Sakhale <rs@saiashirwad.com>  
  
ENV LOCALE en_US.UTF-8  
ENV TZ Asia/Kolkata  
ENV LANG en_US.UTF-8  
# Install some basic tools needed for deployment  
RUN apt-get update && apt-get -yqq install \  
apt-utils \  
build-essential \  
debconf-utils \  
debconf \  
locales \  
curl \  
wget \  
zip \  
unzip \  
git \  
tzdata \  
locales  
  
# Install locale  
RUN \  
sed -i -e "s/# $LOCALE/$LOCALE/" /etc/locale.gen && \  
echo "LANG=$LOCALE">/etc/default/locale && \  
locale-gen en_US.UTF-8 && \  
dpkg-reconfigure --frontend=noninteractive locales && \  
update-locale LANG=$LOCALE \  
echo $TZ | tee /etc/timezone && \  
dpkg-reconfigure --frontend noninteractive tzdata  
  
RUN apt-get update && apt-get install -y python-software-properties \  
&& apt-get install -y apt-file \  
&& apt-file update \  
&& apt-get install -y software-properties-common \  
&& add-apt-repository -y ppa:ondrej/php \  
&& apt-get update \  
&& apt-get install -y php7.1 \  
&& apt-get install -y php7.1-curl \  
php7.1-common \  
php7.1-mcrypt \  
php7.1-cli \  
php7.1-gd \  
php7.1-gmp \  
php7.1-imap \  
php7.1-intl \  
php7.1-json \  
php7.1-ldap \  
php7.1-mbstring \  
php7.1-sqlite \  
php7.1-xml \  
php7.1-zip \  
php-geoip \  
php-imagick \  
&& php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \  
&& php composer-setup.php --install-dir=/usr/bin --filename=composer \  
&& php -r "unlink('composer-setup.php');"  
  
RUN apt-get update \  
&& curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& apt-get install -y nodejs \  
&& npm i -g npm \  
&& npm i -g n \  
&& npm i -g grunt-cli \  
&& npm i -g gulp-cli \  
&& npm i -g bower  
  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list \  
&& apt-get update \  
&& apt-get install yarn  
  
CMD ["php", "composer", "node", "npm", "bower", "grunt", "yarn", "gulp"]

