FROM debian:jessie  
MAINTAINER Filipe Silva <silvam.filipe@gmail.com>  
  
COPY etc/apt/sources.list /etc/apt/sources.list  
  
# Install apache  
RUN apt-get update \  
&& apt-get upgrade -y && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y -q --no-install-recommends \  
build-essential \  
apache2 apache2-doc apache2-utils libapache2-mod-fastcgi \  
php5-fpm php5-xdebug php5-mysql php5-sqlite php5-gd php5-memcached \  
php5-intl php5-mcrypt php5-curl php5-ssh2 php5-sqlite \  
git memcached curl rsync zlib1g-dev ssh \  
python2.7 python2.7-dev python-pip && \  
pip install --upgrade pip virtualenv && \  
pip install Jinja2 && \  
apt-get clean && \  
rm -fr /var/lib/apt/lists/* && \  
a2enmod actions fastcgi alias rewrite  
  
COPY etc /etc  
COPY var/www/html /var/www/html  
  
RUN rm -rf /etc/apache2/sites-enabled/*  
  
ENV USE_XDEBUG no  
ENV GOSU_VERSION 1.10  
ENV COMPOSER_HOME /var/www/.composer  
ENV COMPOSER_VERSION 1.4.2  
ENV PATH vendor/bin:$COMPOSER_HOME/vendor/bin:$PATH  
  
# Grab gosu for easy step-down from root  
RUN set -x \  
&& curl -sSLo /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& curl -sSLo /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- \  
\--install-dir=/usr/local/bin \  
\--filename=composer \  
\--version=${COMPOSER_VERSION} && \  
mkdir -p $COMPOSER_HOME/cache && \  
chown -R www-data:www-data /var/www  
VOLUME $COMPOSER_HOME/cache  
  
WORKDIR /var/www  
  
COPY entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  
  
# Expose ports to other containers only  
EXPOSE 80  
EXPOSE 443  
EXPOSE 11211  
CMD /usr/bin/memcached -d -u www-data && \  
/usr/sbin/php5-fpm -D && \  
/usr/sbin/apache2ctl -D FOREGROUND  

