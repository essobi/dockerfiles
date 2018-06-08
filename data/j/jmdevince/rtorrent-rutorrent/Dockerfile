FROM debian:stable-slim  
USER root  
  
RUN apt-get update && \  
apt-get -y install sudo && \  
useradd -m -d /rtorrent rtorrent && \  
mkdir -p /multimedia && \  
chown rtorrent:rtorrent /multimedia && \  
sudo -u rtorrent mkdir -p /rtorrent/bin && \  
sudo -u rtorrent mkdir -p /rtorrent/.downloads && \  
sudo -u rtorrent mkdir -p /rtorrent/.session && \  
sudo -u rtorrent mkdir -p /rtorrent/.rutorrent && \  
sudo -u rtorrent mkdir -p /rtorrent/.log && \  
mkdir -p /usr/share/man/man1 && \  
apt-get -y install wget git rtorrent python python-pip python-setuptools
python-pkg-resources git build-essential supervisor openjdk-8-jre-headless
php-fpm php-cli php-curl php-xml php-json nginx libarchive-zip-perl libnet-
ssleay-perl libhtml-entities-numbered-perl libhtml-html5-entities-perl libxml-
perl libdigest-sha-perl libjson-xs-perl libjson-perl curl unzip libxml-libxml-
perl irssi && \  
sudo -H -u rtorrent git clone "https://github.com/pyroscope/pyrocore.git"
/rtorrent/.local/pyroscope && \  
sudo -H -u rtorrent /rtorrent/.local/pyroscope/update-to-head.sh && \  
sudo -H -u rtorrent touch /rtorrent/.pyroscope/run/pyrotorque && \  
git clone https://github.com/jmdevince/rtorrent-rutorrent-shared.git /root/a
&& \  
cp /root/a/startup-rtorrent.sh /root/a/startup-nginx.sh /root/a/startup-php.sh
/root/a/startup-irssi.sh /root/ && \  
cp /root/a/supervisord.conf /etc/supervisor/conf.d/ && \  
cp /root/a/torque.ini /rtorrent/.pyroscope/torque.ini && \  
cp /root/a/.rtorrent.rc /rtorrent/.rtorrent.rc && \  
cp /root/a/extract_release /rtorrent/bin/extract_release && \  
rm -f /etc/php/7.0/fpm/pool.d/* && \  
cp /root/a/rutorrent.conf /etc/php/7.0/fpm/pool.d/rutorrent.conf && \  
rm -f /etc/nginx/sites-enabled/* && \  
cp /root/a/rutorrent.nginx /etc/nginx/sites-enabled/rutorrent && \  
sed -i -e 's/user www-data/user rtorrent/g' /etc/nginx/nginx.conf && \  
chmod +x /rtorrent/bin/extract_release && \  
chown rtorrent:rtorrent /rtorrent/.pyroscope/torque.ini
/rtorrent/bin/extract_release && \  
wget -O /root/filebot.deb
'https://app.filebot.net/download.php?type=deb&arch=amd64' && \  
dpkg -i /root/filebot.deb && \  
rm -f /root/filebot.deb && \  
wget -O /root/unrar.deb https://www.rarlab.com/rar/unrar_5.2.5-0.1_amd64.deb
&& \  
dpkg -i /root/unrar.deb && \  
rm -f /root/unrar.deb && \  
sudo -H -u rtorrent git clone https://github.com/Novik/ruTorrent.git
/rtorrent/.rutorrent/ && \  
rm -Rfv /rtorrent/.rutorrent/plugins/_noty && \  
rm -Rfv /rtorrent/.rutorrent/plugins/extratio && \  
rm -Rfv /rtorrent/.rutorrent/plugins/extsearch && \  
rm -Rfv /rtorrent/.rutorrent/plugins/feeds && \  
rm -Rfv /rtorrent/.rutorrent/plugins/geoip && \  
rm -Rfv /rtorrent/.rutorrent/plugins/lookat && \  
rm -Rfv /rtorrent/.rutorrent/plugins/ipad && \  
rm -Rfv /rtorrent/.rutorrent/plugins/mediainfo && \  
rm -Rfv /rtorrent/.rutorrent/plugins/retrackers && \  
rm -Rfv /rtorrent/.rutorrent/plugins/rutracker_check && \  
rm -Rfv /rtorrent/.rutorrent/plugins/screenshots && \  
rm -Rfv /rtorrent/.rutorrent/plugins/xmpp && \  
rm -Rfv /rtorrent/.rutorrent/plugins/uploadeta && \  
rm -Rfv /rtorrent/.rutorrent/plugins/unpack && \  
rm -Rfv /rtorrent/.rutorrent/plugins/spectrogram && \  
sudo -u rtorrent mkdir -p /rtorrent/.irssi/scripts/autorun && \  
cd /rtorrent/.irssi/scripts && \  
curl -sL http://git.io/vlcND | grep -Po '(?<="browser_download_url":
")(.*-v[\d.]+.zip)' | xargs wget --quiet -O autodl-irssi.zip && \  
unzip -o autodl-irssi.zip && \  
rm autodl-irssi.zip && \  
cp autodl-irssi.pl autorun/ && \  
mkdir -p /rtorrent/.autodl && \  
touch /rtorrent/.autodl/autodl.cfg && \  
echo '[options]' > /rtorrent/.autodl/autodl2.cfg && \  
echo 'gui-server-port = 50000' >> /rtorrent/.autodl/autodl2.cfg && \  
echo -n 'gui-server-password = ' >> /rtorrent/.autodl/autodl2.cfg && \  
echo $(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1) >>
/rtorrent/.autodl/autodl2.cfg && \  
chown -Rfv rtorrent:rtorrent /rtorrent/.autodl/ && \  
sudo -u rtorrent git clone https://github.com/autodl-community/autodl-
rutorrent.git /rtorrent/.rutorrent/plugins/autodl-irssi && \  
sudo -u rtorrent cp /rtorrent/.rutorrent/plugins/autodl-irssi/_conf.php
/rtorrent/.rutorrent/plugins/autodl-irssi/conf.php && \  
sed -i -e 's/autodlPort = 0/autodlPort = 50000/g'
/rtorrent/.rutorrent/plugins/autodl-irssi/conf.php && \  
sed -i -e 's/autodlPassword = ""/autodlPassword = "'$(grep gui-server-password
/rtorrent/.autodl/autodl2.cfg | awk -F" = " ' { print $2 } ')'"/g'
/rtorrent/.rutorrent/plugins/autodl-irssi/conf.php && \  
cp /root/a/config.php /rtorrent/.rutorrent/conf/config.php && \  
chown rtorrent:rtorrent -Rfv /rtorrent/.rutorrent/conf/config.php && \  
rm -Rfv /root/a/  
  
EXPOSE 80 50000 65300 65301  
VOLUME /rtorrent  
VOLUME /multimedia  
  
CMD ["supervisord"]  
  

