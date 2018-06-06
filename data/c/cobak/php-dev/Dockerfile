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
curl \  
git \  
libfcgi0ldbl \  
php7.0-apcu \  
php7.0-bcmath \  
php7.0-gmp \  
php7.0-bz2 \  
php7.0-cli \  
php7.0-curl \  
php7.0-fpm \  
php7.0-gd \  
php7.0-intl \  
php7.0-mcrypt \  
php7.0-mbstring \  
php7.0-mysql \  
php7.0-pgsql \  
php7.0-xml \  
php7.0-readline \  
php7.0-redis \  
php7.0-sqlite3 \  
php7.0-soap \  
php7.0-ssh2 \  
php7.0-xml \  
php7.0-zip \  
supervisor \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY cli/php.ini /etc/php/7.0/cli/php.ini  
COPY fpm/php.ini /etc/php/7.0/fpm/php.ini  
COPY fpm/pool.d/www.conf /etc/php/7.0/fpm/pool.d/www.conf  
COPY composer /usr/local/bin/composer  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY docker-logs.sh /usr/local/bin/docker-logs.sh  
  
RUN mkfifo /dockerout \  
&& mkfifo /dockererr \  
&& chmod u+w,g+w,o+w /dockerout /dockererr  
  
ENV TINI_VERSION v0.13.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
RUN chmod +x /tini  
  
EXPOSE 9000  
ENTRYPOINT ["/tini", "--"]  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]  

