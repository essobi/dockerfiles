FROM php:5.6-fpm  
MAINTAINER HomeRefill IT Team  
  
# Ignore APT warnings about not having a TTY  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get upgrade -yq \  
&& apt-get -yq install \  
build-essential \  
python \  
wget \  
bindfs \  
vim \  
git-core \  
g++ \  
autoconf \  
file \  
gcc \  
libc-dev \  
make \  
pkg-config \  
re2c \  
&& apt-get clean -qq \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN apt-get update && apt-get install -y \  
ca-certificates \  
curl \  
libedit2 \  
libsqlite3-0 \  
libxml2 \  
\--no-install-recommends && rm -r /var/lib/apt/lists/*  
  
#
==============================================================================  
# Install MySQL, Drivers and more dependencies  
#
==============================================================================  
  
RUN apt-get update -qq \  
&& apt-get install -y -qq \  
autoconf \  
imagemagick \  
libbz2-dev \  
libevent-dev \  
libglib2.0-dev \  
libjpeg-dev \  
libmagickcore-dev \  
libmagickwand-dev \  
libncurses-dev \  
libcurl4-openssl-dev \  
libffi-dev \  
libgdbm-dev \  
libpq-dev \  
libreadline-dev libreadline6-dev \  
libssl-dev \  
libtool \  
libxml2-dev \  
libxslt-dev \  
libyaml-dev \  
software-properties-common \  
zlib1g-dev \  
mysql-client libmysqlclient-dev \  
sqlite3 libsqlite3-dev \  
&& apt-get clean -qq \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN set -xe \  
&& buildDeps=" \  
$PHP_EXTRA_BUILD_DEPS \  
libcurl4-openssl-dev \  
libedit-dev \  
libsqlite3-dev \  
libssl-dev \  
libmcrypt-dev \  
libxml2-dev \  
xz-utils \  
" \  
&& apt-get update && apt-get install -y $buildDeps --no-install-recommends &&
rm -rf /var/lib/apt/lists/*  
  
# PHP Extensions  
RUN docker-php-ext-install zip xml json curl xml pdo_mysql soap ctype mcrypt  
  
RUN useradd --home /home/homerefill -m -U -s /bin/bash homerefill  
  
RUN echo 'Defaults !requiretty' >> /etc/sudoers; \  
echo 'homerefill ALL= NOPASSWD: /usr/sbin/dpkg-reconfigure -f noninteractive
tzdata, /usr/bin/tee /etc/timezone' >> /etc/sudoers;  
  
RUN mkdir -p /var/www  
RUN chown -R homerefill\:homerefill /var/www && chown -R
homerefill\:homerefill /usr/local && chown -R homerefill\:homerefill
/home/homerefill  
  
USER homerefill  
  
ENV HOME /home/homerefill  
  
RUN cd $HOME && mkdir -p $HOME/tmp  
  
RUN cd /home/homerefill/tmp &&\  
curl -s https://getcomposer.org/installer | php &&\  
mv composer.phar /usr/local/bin/composer &&\  
rm -fr tmp

