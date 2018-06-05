FROM debian:jessie  
MAINTAINER Andrew Smith "andrew1972.es@gmail.com"  
ENV BUILD_DATE 2018-01-09  
RUN echo "APT::Install-Recommends \"0\" ; APT::Install-Suggests \"0\" ;" >
/etc/apt/apt.conf.d/70debconf  
  
RUN apt-get update  
RUN apt-get -y install wget  
  
ADD sources.list /tmp/sources.list  
RUN cat /tmp/sources.list > /etc/apt/sources.list  
RUN rm -f /tmp/sources.list  
  
RUN wget -O - http://www.dotdeb.org/dotdeb.gpg | apt-key add -  
  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN apt-get -y install sudo supervisor pwgen apt-utils  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install php7.0-fpm php7.0-cli \  
php7.0-curl php7.0-gd php7.0-imagick \  
php7.0-imap php7.0-intl php7.0-mcrypt php7.0-memcache php7.0-mysql \  
php7.0-sqlite php7.0-redis php7.0-bz2 php7.0-ldap php7.0-xml php7.0-mbstring \  
php7.0-zip php7.0-bcmath bzip2 unzip memcached ntpdate libxrender1
libfontconfig1 \  
imagemagick inkscape rcconf sudo libmagickwand-dev pngnq pngcrush xvfb \  
cabextract libfcgi0ldbl poppler-utils rsync xz-utils python-uno \  
xfonts-75dpi jpegoptim monit \  
pigz libtext-template-perl mailutils redis-server curl \  
mariadb-server-10.0  
  
# set root password  
RUN echo "root:root" | chpasswd  
  
# configure apache  
RUN apt-get -y install openssl ssl-cert ca-certificates openssl-blacklist  
RUN apt-get -y install apache2 libapache2-mod-fastcgi  
RUN a2dismod -f cgi autoindex mpm_worker mpm_prefork  
RUN a2enmod rewrite actions fastcgi alias status filter expires headers
setenvif proxy proxy_fcgi socache_shmcb mpm_event ssl  
RUN rm /etc/apache2/sites-enabled/*  
RUN rm -r /var/www/*  
RUN chown -R www-data:www-data /var/www  
ADD vhost.conf /etc/apache2/sites-enabled/000-default.conf  
  
# configure mysql  
RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/"
/etc/mysql/my.cnf  
  
# configure php-fpm  
RUN rm -r /etc/php/7.0/cli/php.ini  
RUN rm -r /etc/php/7.0/fpm/php.ini  
ADD php.ini /etc/php/7.0/fpm/php.ini  
RUN ln -s /etc/php/7.0/fpm/php.ini /etc/php/7.0/cli/php.ini  
RUN mv /etc/php/7.0/fpm/pool.d/www.conf /etc/php/7.0/fpm/pool.d/www.conf.dist  
ADD www-data.conf /etc/php/7.0/fpm/pool.d/www-data.conf  
  
# configure redis  
ADD redis.conf /tmp/redis.conf  
RUN cat /tmp/redis.conf >> /etc/redis/redis.conf  
  
# install tools  
RUN apt-get -y install wkhtmltopdf  
COPY ghostscript-9.19-linux-x86_64.tgz /tmp/ghostscript-9.19-linux-x86_64.tgz  
COPY ffmpeg-release-64bit-static.tar.xz /tmp/ffmpeg-release-64bit-
static.tar.xz  
ADD install-ghostscript.sh /tmp/install-ghostscript.sh  
ADD install-ffmpeg.sh /tmp/install-ffmpeg.sh  
RUN chmod 755 /tmp/*.sh  
RUN /tmp/install-ghostscript.sh  
RUN /tmp/install-ffmpeg.sh  
  
RUN rm -f /tmp/install-ghostscript.sh /tmp/install-ffmpeg.sh  
  
# setup startup scripts  
ADD start-apache.sh /start-apache.sh  
ADD start-php-fpm.sh /start-php-fpm.sh  
ADD run.sh /run.sh  
RUN chmod 755 /*.sh  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# install pimcore  
ADD install-pimcore.sh /tmp/install-pimcore.sh  
RUN chmod 755 /tmp/*.sh  
RUN /tmp/install-pimcore.sh  
  
# pimcore config files  
ADD cache.php /tmp/cache.php  
  
# ports  
EXPOSE 80  
# volumes  
VOLUME ["/var/www", "/var/lib/mysql"]  
  
CMD ["/run.sh"]  
  

