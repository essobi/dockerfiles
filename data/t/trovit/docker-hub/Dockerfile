FROM debian:jessie  
  
# Get noninteractive frontend for Debian to avoid some problems:  
# debconf: unable to initialize frontend: Dialog  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo "\nexport TERM=xterm" >> /etc/bash.bashrc \  
&& apt-get update && apt-get install -y --no-install-recommends \  
apt-utils  
  
RUN echo '\n\  
deb http://packages.dotdeb.org jessie all\n\  
deb-src http://packages.dotdeb.org jessie all\n'\  
>> /etc/apt/sources.list  
  
RUN apt-key adv --keyserver keys.gnupg.net --recv-keys 7E3F070089DF5277 \  
&& apt-get update && apt-get install -y --no-install-recommends \  
ca-certificates \  
libfcgi0ldbl \  
unzip \  
php5-apcu \  
php5-gmp \  
php5-cli \  
php5-curl \  
php5-gd \  
php5-intl \  
php5-mcrypt \  
php5-mysql \  
php5-gearman \  
php5-pgsql \  
php5-readline \  
php5-redis \  
php5-ssh2 \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY conf/php-cli.ini /etc/php5/cli/php.ini

