FROM phusion/baseimage:0.9.16  
  
# Forked from:  
#MAINTAINER aptalca  
MAINTAINER riley.schuit@gmail.com  
  
VOLUME ["/config"]  
  
EXPOSE 80  
  
RUN export DEBCONF_NONINTERACTIVE_SEEN=true DEBIAN_FRONTEND=noninteractive &&
\  
apt-get update && \  
apt-get install -y \  
software-properties-common \  
python-software-properties && \  
add-apt-repository -y ppa:iconnor/zoneminder && \  
add-apt-repository ppa:jonathonf/ffmpeg-3 && \  
apt-get update && \  
apt-get install -y \  
wget \  
apache2 \  
mysql-server \  
php5 \  
libapache2-mod-php5 \  
usbutils \  
supervisor && \  
service apache2 restart && \  
service mysql restart && \  
apt-get install -y \  
zoneminder=1.30.4-trusty1 \  
libvlc-dev \  
libvlccore-dev \  
vlc \  
ffmpeg && \  
a2enmod cgi && \  
service apache2 restart && \  
service mysql restart && \  
rm -r /etc/init.d/zoneminder && \  
mkdir -p /etc/my_init.d  
  
ADD zoneminder-supervisord.conf /etc/supervisor/conf.d/zoneminder.conf  
ADD zoneminder /etc/init.d/zoneminder  
ADD firstrun.sh /etc/my_init.d/firstrun.sh  
  
RUN /etc/init.d/supervisor restart && supervisorctl reload  
  
RUN apt-get clean  
  
RUN chmod +x /etc/init.d/zoneminder && \  
chmod +x /etc/my_init.d/firstrun.sh && \  
echo "date.timezone= America/Los_Angeles" >> /etc/php5/apache2/php.ini && \  
cp /etc/apache2/conf-available/zoneminder.conf /etc/apache2/conf-enabled/ && \  
cp /etc/apache2/mods-available/rewrite.load /etc/apache2/mods-enabled/ && \  
adduser www-data video && \  
service apache2 restart && \  
cd /usr/src && \  
wget http://www.charliemouse.com:8080/code/cambozola/cambozola-0.936.tar.gz &&
\  
tar -xzvf cambozola-0.936.tar.gz && \  
cp cambozola-0.936/dist/cambozola.jar /usr/share/zoneminder/www && \  
rm /usr/share/zoneminder/www/tools/mootools/mootools-more.js && \  
rm /usr/share/zoneminder/www/tools/mootools/mootools-core.js && \  
cp /usr/share/javascript/mootools/mootools-more.js
/usr/share/zoneminder/www/tools/mootools/ && \  
cp /usr/share/javascript/mootools/mootools.js
/usr/share/zoneminder/www/tools/mootools/mootools-core.js && \  
#chown www-data -R /usr/share/javascript/mootools/* && \  
chown www-data -R /usr/share/zoneminder/www && \  
chown www-data /etc/zm/zm.conf && \  
cp /etc/zm/zm.conf /root/zm.conf && \  
update-rc.d -f apache2 remove && \  
update-rc.d -f mysql remove && \  
update-rc.d -f zoneminder remove  

