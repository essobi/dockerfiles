FROM ubuntu:trusty  
MAINTAINER <https://github.com/FuntwoX>  
USER root  
  
# add extra sources  
ADD ./extra.list /etc/apt/sources.list.d/extra.list  
  
# install  
RUN apt-get update && \  
apt-get install -y --force-yes git-core rtorrent unzip unrar mediainfo curl
php5-fpm php5-cli php5-geoip nginx wget ffmpeg supervisor && \  
rm -rf /var/lib/apt/lists/*  
  
# download rutorrent  
RUN mkdir -p /var/www && \  
git clone \--depth=1 \  
https://github.com/Novik/ruTorrent.git \  
/var/www/rutorrent && \  
git clone \  
https://github.com/QuickBox/club-QuickBox.git \  
/var/www/rutorrent/plugins/theme/themes/club-QuickBox  
  
ADD ./config.php /var/www/rutorrent/conf/  
ADD ./rules-htpasswd /.htpasswd  
  
# add startup scripts and configs  
ADD startup-nginx.sh startup-php.sh /root/  
  
RUN groupadd share  
  
COPY createUsersAndStart.sh /  
COPY template/* /template/  
  
ENV USE_SSL=false  
VOLUME /downloads /ssl  
  
RUN chmod +x createUsersAndStart.sh /root/startup-nginx.sh /root/startup-
php.sh  
  
CMD ["/createUsersAndStart.sh", ".htpasswd"]

