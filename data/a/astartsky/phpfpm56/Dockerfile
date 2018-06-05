FROM ubuntu:14.04  
MAINTAINER Dmitry Sinev <astartsky@gmail.com>  
ENV DEBIAN_FRONTEND=noninteractive \  
REFRESHED_AT=2015_09_10 \  
TERM=xterm  
  
# set locale  
RUN dpkg-reconfigure locales && \  
locale-gen ru_RU.UTF-8 && \  
/usr/sbin/update-locale LANG=ru_RU.UTF-8  
  
# install custom repositories  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-key E5267A6C  
RUN apt-get update && apt-get install -y software-properties-common && \  
add-apt-repository -y ppa:ondrej/php5-5.6  
  
# install packages  
RUN apt-get update && apt-get install -y \  
php5-fpm \  
php5-gd \  
php5-mcrypt \  
php5-curl \  
php5-imagick \  
php5-mysql \  
php5-xcache \  
php5-memcache \  
php5-intl \  
php5-xdebug \  
php5-xsl \  
wget \  
curl \  
nano \  
git \  
mercurial \  
lrzsz  
  
# configure fpm  
RUN sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g"
/etc/php5/fpm/php.ini && \  
sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g"
/etc/php5/fpm/php.ini && \  
sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g"
/etc/php5/fpm/php.ini && \  
sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php5/fpm/php-fpm.conf
&& \  
sed -i -e "s/listen =.*/listen = 9000/" /etc/php5/fpm/pool.d/www.conf && \  
echo "env[APP_ENV] = \$APP_ENV" >> /etc/php5/fpm/pool.d/www.conf  
  
# configure php  
RUN sed -i -e "s/.*sendmail_path =.*/sendmail_path = \/usr\/bin\/env
\/usr\/local\/bin\/catchmail --smtp-ip mc -f address@example\\.com/"
/etc/php5/fpm/php.ini && \  
sed -i -e "s/.*sendmail_path =.*/sendmail_path = \/usr\/bin\/env catchmail
--smtp-ip mc -f address@example\\.com/" /etc/php5/cli/php.ini && \  
echo "error_reporting = E_ALL\ndisplay_startup_errors = 1\ndisplay_errors = 1"
>> /etc/php5/fpm/conf.d/01-errors.ini && \  
echo "error_reporting = E_ALL\ndisplay_startup_errors = 1\ndisplay_errors = 1"
>> /etc/php5/cli/conf.d/01-errors.ini && \  
sed -i "s/short_open_tag = Off/short_open_tag = On/" /etc/php5/fpm/php.ini &&
\  
sed -i "s/short_open_tag = Off/short_open_tag = On/" /etc/php5/cli/php.ini  
  
# configure composer  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
RUN chmod +x /usr/local/bin/composer  
  
# cleanup  
RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
  
VOLUME ["/var/www"]  
WORKDIR /var/www  
  
EXPOSE 9000  
  
ENTRYPOINT ["/usr/sbin/php5-fpm","-F"]  
  
  

