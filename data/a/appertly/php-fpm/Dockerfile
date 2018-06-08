FROM ubuntu:xenial  
MAINTAINER Jonathan Hawk <jonathan@appertly.com>  
  
# Install php  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends software-properties-common wget
\  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4F4EA0AAE5267A6C \  
&& LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends ca-certificates git librsvg2-bin
\  
php7.1-fpm php7.1-cli php7.1-opcache php7.1-gd php7.1-gmp php7.1-mcrypt php-
imagick php7.1-mbstring php7.1-intl \  
php-memcached php7.1-mysql php7.1-pgsql php7.1-sqlite3 php7.1-curl php7.1-xml
php7.1-zip php7.1-mongodb \  
php7.1-soap php7.1-xmlrpc php7.1-dev php-pear make libssl-dev pkg-config \  
&& sed -i 's/^/#/' /etc/cron.d/php \  
&& rm -rf /tmp/* /var/tmp/* \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /var/log/apt/* \  
&& rm -rf /var/log/dpkg.log \  
&& rm -rf /var/log/bootstrap.log \  
&& rm -rf /var/log/alternatives.log  
  
# error logs to docker log collector  
RUN ln -sf /dev/stderr /var/log/php7.1-fpm.log \  
&& mkdir -p /run/php \  
&& echo "1" > /run/php/php7.1-fpm.pid  
  
RUN wget https://releases.pagure.org/liberation-fonts/liberation-fonts-
ttf-2.00.0.tar.gz \  
&& tar zxvf liberation-fonts-ttf-2.00.0.tar.gz \  
&& mkdir /usr/share/fonts/truetype/liberation \  
&& cp liberation-fonts-ttf-2.00.0/*.ttf /usr/share/fonts/truetype/liberation \  
&& fc-cache -f -v  
  
ADD php.ini /etc/php/7.1/fpm/php.ini  
  
RUN pecl install mongodb  
  
ADD www.conf /etc/php/7.1/fpm/pool.d/www.conf  
ADD opcache.ini /etc/php/7.1/mods-available/opcache.ini  
ADD start.sh /scripts/start.sh  
RUN chmod +x /scripts/start.sh  
  
# PHP-FPM on FastCGI with default port of 9000  
EXPOSE 9000  
# Default command  
CMD ["/scripts/start.sh"]  

