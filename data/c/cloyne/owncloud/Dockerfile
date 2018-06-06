FROM tozd/php:5.6  
VOLUME /var/www/owncloud/config  
VOLUME /owncloud-data  
VOLUME /var/log/redis  
VOLUME /var/lib/redis  
  
RUN apt-get update -q -q && \  
apt-get install apt-transport-https ca-certificates curl --yes --force-yes &&
\  
apt-get install redis-server php-redis --yes --force-yes && \  
curl
https://attic.owncloud.com/org/download/repositories/9.1.4/Ubuntu_14.04/Release.key
| apt-key add - && \  
echo 'deb
http://attic.owncloud.com/org/download/repositories/9.1.4/Ubuntu_14.04/ /' >>
/etc/apt/sources.list.d/owncloud.list && \  
apt-get update -q -q && \  
apt-get install owncloud --no-install-recommends --yes --force-yes && \  
apt-get install libipc-sharedcache-perl libmcrypt-dev mcrypt libterm-readkey-
perl libreoffice-writer curl php-net-ftp php5.6-gmp php-imagick libav-tools
php5.6-json php5.6-zip php5.6-xml php5.6-curl php5.6-gd php5.6-mbstring --yes
--force-yes && \  
for file in /etc/php/5.6/mods-available/*.ini; do phpenmod $(basename -s .ini
"$file"); done && \  
chown -Rh root:root /var/www/owncloud && \  
mkdir -p /owncloud-data && \  
adduser fcgi-php redis && \  
rm -f /var/www/owncloud/.user.ini  
  
COPY ./etc /etc  
COPY ./config /var/www/owncloud/config  
# We use the following directory to restore the configuration when an empty
volume is mounted over /var/www/owncloud/config.  
COPY ./config /etc/service/php/config  
COPY ./apps /var/www/owncloud/apps  

