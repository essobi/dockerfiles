FROM dramaturg/debian-systemd  
MAINTAINER Sebastian Krohn <seb@ds.ag>  
  
# Need this environment variable otherwise mysql will prompt for passwords  
RUN apt-get -y install \  
nginx wget php7.1 php7.1-cli php7.1-fpm php7.1-json php7.1-curl php7.1-mysqlnd
php7.1-gd \  
php7.1-xml php7.1-readline pwgen lame libvorbis-dev vorbis-tools flac
libmp3lame-dev \  
libavcodec-extra* libfaac-dev libtheora-dev libvpx-dev libav-tools git
inotify-tools && \  
systemctl enable nginx  
  
# Install composer for dependency management  
RUN php -r "readfile('https://getcomposer.org/installer');" | php && \  
mv composer.phar /usr/local/bin/composer  
  
# For local testing / faster builds  
# COPY master.tar.gz /opt/master.tar.gz  
ADD https://github.com/ampache/ampache/archive/master.tar.gz /opt/ampache-
master.tar.gz  
  
# extraction / installation  
RUN rm -rf /var/www/* && \  
tar -C /var/www -xf /opt/ampache-master.tar.gz ampache-master --strip=1 && \  
cd /var/www && composer install --prefer-source --no-interaction && \  
chown -R www-data /var/www  
  
ADD ampache.cfg.php /var/www/config/ampache.cfg.php  
ENV conff_ampache /var/www/config/ampache.cfg.php  
  
ENV DB_HOST mysql  
ENV DB_PORT 3306  
ENV DB_USER ampache  
ENV DB_PASS changeme  
ENV DB_NAME ampache  
  
ENV MAIL_NAME "Ampache"  
ENV MAIL_USER "sound"  
ENV MAIL_DOMAIN "example.org"  
ENV MAIL_PORT 25  
ENV MAIL_HOST localhost  
ENV MAIL_AUTH "false"  
ENV MAIL_AUTHUSER change  
ENV MAIL_AUTHPASS changeme  
  
  
  
# setup nginx  
ADD 001-ampache.conf /etc/nginx/sites-available/  
RUN rm -f /etc/nginx/sites-enabled/default && \  
ln -s /etc/nginx/sites-available/001-ampache.conf /etc/nginx/sites-enabled/  
  
# Add job to cron to clean the library every night  
RUN echo '30 7 * * * www-data php /var/www/bin/catalog_update.inc' >>
/etc/crontab  
  
VOLUME ["/media"]  
VOLUME ["/var/www/config"]  
VOLUME ["/var/www/themes"]  
EXPOSE 80  

