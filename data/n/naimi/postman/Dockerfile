FROM ubuntu:xenial  
  
MAINTAINER Amangeldy Kadyl <lex0.kz@gmail.com>  
  
ENV GOSU_VERSION 1.10  
ENV ENVIRONMENT dev  
  
RUN set -x \  
&& apt-get update && apt-get install -y --no-install-recommends ca-
certificates wget locales && rm -rf /var/lib/apt/lists/* \  
&& dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch"
\  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc"
\  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& locale-gen ru_RU \  
&& locale-gen ru_RU.UTF-8 \  
&& echo 'LANG="ru_RU.UTF-8"' > /etc/default/locale \  
&& useradd -s /bin/bash -m naimi \  
&& echo "deb http://nginx.org/packages/ubuntu/ xenial nginx" >
/etc/apt/sources.list.d/nginx.list \  
&& echo "deb-src http://nginx.org/packages/ubuntu/ xenial nginx" >>
/etc/apt/sources.list.d/nginx.list \  
&& echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu xenial main" >
/etc/apt/sources.list.d/php.list \  
&& echo "deb-src http://ppa.launchpad.net/ondrej/php/ubuntu xenial main" >>
/etc/apt/sources.list.d/php.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys ABF5BD827BD9BF62 \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4F4EA0AAE5267A6C \  
&& apt update \  
&& apt install -y \  
nginx \  
git \  
php-msgpack \  
php-pear \  
php-xml \  
php-pear \  
php7.1 \  
php7.1-dev \  
php7.1-cli \  
php7.1-common \  
php7.1-curl \  
php7.1-dev \  
php7.1-fpm \  
php7.1-json \  
php7.1-mbstring \  
php7.1-opcache \  
php7.1-pgsql \  
php7.1-readline \  
php7.1-xml \  
supervisor \  
vim \  
curl \  
unzip \  
jq \  
openssh-server \  
&& cd ~/ \  
&& git clone https://github.com/tarantool/tarantool-php.git \  
&& cd tarantool-php \  
&& git checkout -b php7-v2 origin/php7-v2 \  
&& phpize \  
&& ./configure \  
&& make \  
&& make install \  
&& echo 'extension=tarantool.so' > /etc/php/7.1/mods-available/tarantool.ini \  
&& ln -s /etc/php/7.1/mods-available/tarantool.ini
/etc/php/7.1/cli/conf.d/20-tarantool.ini \  
&& ln -s /etc/php/7.1/mods-available/tarantool.ini
/etc/php/7.1/fpm/conf.d/20-tarantool.ini \  
&& php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \  
&& php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'669656bab3166a7aff8a7506b8cb2d1c292f042046c5a994c43155c0be6190fa0355160742ab2e1c88d40d5be660b410')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" \  
&& php composer-setup.php --install-dir=/usr/local/bin --filename=composer \  
&& apt remove --auto-remove php7.1-dev -y \  
&& apt remove --auto-remove make -y \  
&& rm -rf \  
/var/lib/apt/lists/* \  
/root/tarantool-php  
  
COPY init.sh /usr/local/bin/init.sh  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
COPY config /usr/share/container_config  
  
RUN set -x\  
&& chmod +x /usr/local/bin/entrypoint.sh \  
&& chmod +x /usr/local/bin/init.sh  
  
VOLUME /home/naimi  
VOLUME /home/naimi/.ssh  
VOLUME /root/.ssh  
  
EXPOSE 80  
EXPOSE 22  
  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

