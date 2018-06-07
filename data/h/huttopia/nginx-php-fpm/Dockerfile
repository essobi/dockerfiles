FROM debian:wheezy  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y wget  
  
RUN echo "deb http://packages.dotdeb.org wheezy-php56 all" >>
/etc/apt/sources.list  
RUN echo "deb-src http://packages.dotdeb.org wheezy-php56 all" >>
/etc/apt/sources.list  
  
RUN wget --no-check-certificate https://www.dotdeb.org/dotdeb.gpg  
RUN apt-key add dotdeb.gpg  
  
# Install php and nginx  
RUN apt-get update && apt-get install -y \  
sudo \  
curl \  
git \  
locate \  
vim \  
mcrypt \  
php5-dev \  
php5-cli \  
php5-xdebug \  
php5-intl \  
php5-curl \  
php5-pgsql \  
php5-fpm \  
php5-apcu \  
php5-mysql \  
php5-gd \  
php5-mcrypt \  
php-pear \  
nginx  
  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
RUN sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php5/fpm/php.ini  
RUN sed -i "s/;date.timezone.*/date.timezone = Europe\/Paris/"
/etc/php5/fpm/php.ini  
RUN sed -i "s/;date.timezone.*/date.timezone = Europe\/Paris/"
/etc/php5/cli/php.ini  
RUN sed -i "s/;listen.allowed_clients = 127.0.0.1/listen.allowed_clients =
0.0.0.0/" /etc/php5/fpm/pool.d/www.conf  
RUN sed -i "s/^user\s*=.*/user = root/" /etc/php5/fpm/pool.d/www.conf  
RUN sed -i "s/^group\s*=.*/group = root/" /etc/php5/fpm/pool.d/www.conf  
RUN echo "xdebug.remote_enable = on" >> /etc/php5/fpm/conf.d/20-xdebug.ini  
RUN echo "xdebug.remote_connect_back = on" >>
/etc/php5/fpm/conf.d/20-xdebug.ini  
  
# Alias sf  
RUN echo "alias sf='php bin/console'" >> /root/.bashrc  
  
EXPOSE 80  
EXPOSE 443  
WORKDIR /src  
  
CMD php5-fpm -R && nginx -c /etc/nginx/nginx.conf  

