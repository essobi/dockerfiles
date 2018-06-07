FROM phusion/baseimage:0.9.18  
  
MAINTAINER larizzo  
  
VOLUME ["/config"]  
  
EXPOSE 80  
  
RUN export DEBCONF_NONINTERACTIVE_SEEN=true DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && \  
apt-get install -y \  
software-properties-common \  
python-software-properties && \  
add-apt-repository -y ppa:iconnor/zoneminder-master && \  
apt-get update && \  
apt-get install -y \  
wget \  
apache2 \  
php5 \  
php5-gd \  
libapache2-mod-php5 \  
usbutils \  
vlc \  
libvlc-dev \  
libvlccore-dev \  
ssmtp \  
mailutils  
  
RUN apt-get install -y \  
zoneminder \  
libvlc-dev \  
libvlccore-dev vlc && \  
chmod 740 /etc/zm/zm.conf && \  
chown root:www-data /etc/zm/zm.conf && \  
a2enconf zoneminder && \  
a2enmod rewrite && \  
a2enmod cgi && \  
cd /usr/src && \  
wget http://www.andywilcock.com/code/cambozola/cambozola-latest.tar.gz && \  
tar -xzvf cambozola-latest.tar.gz && \  
cp cambozola-*/dist/cambozola.jar /usr/share/zoneminder && \  
chown -R www-data:www-data /usr/share/zoneminder/ && \  
sed -i 's/\;date.timezone =/date.timezone = \"America\/New_York\"/'
/etc/php5/apache2/php.ini && \  
rm -r /etc/init.d/zoneminder && \  
mkdir -p /etc/my_init.d && \  
apt-get clean  
  
COPY zoneminder /etc/init.d/zoneminder  
COPY firstrun.sh /etc/my_init.d/firstrun.sh  
  
RUN chmod +x /etc/init.d/zoneminder && \  
chmod +x /etc/my_init.d/firstrun.sh && \  
adduser www-data video && \  
service apache2 restart && \  
update-rc.d -f apache2 remove && \  
update-rc.d -f zoneminder remove  

