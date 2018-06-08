FROM ubuntu:14.04  
MAINTAINER Foncekar  
  
# Install transmission  
RUN apt-get update && \  
apt-get dist-upgrade -y && \  
apt-get install build-essential automake autoconf libtool pkg-config intltool
libcurl4-openssl-dev \  
libglib2.0-dev libevent-dev libminiupnpc-dev libappindicator-dev wget unzip -y
&& \  
apt-get clean && \  
rm -rf /tmp/*  
  
WORKDIR /tmp  
  
RUN wget http://www.sb-innovation.de/attachments/f45/15326d1428574469-linux-
transmission-2-83-14283-no-report-leecher-transmission-2.84-patched.zip && \  
mv 15326d1428574469-linux-transmission-2-83-14283-no-report-leecher-
transmission-2.84-patched.zip transmission-2.84.zip && \  
unzip transmission-2.84.zip && \  
cd transmission-2.84 && \  
chmod a+x -R configure && \  
./configure -q --enable-daemon --disable-mac && \  
make -s && \  
make install  
  
COPY config/transmission-daemon /etc/init.d/transmission-daemon  
  
RUN chmod +x /etc/init.d/transmission-daemon && \  
chown root:root /etc/init.d/transmission-daemon && \  
adduser --disabled-password transmission && \  
mkdir -p /home/transmission/.config/transmission-daemon/ && \  
mkdir -p /downloads && \  
chown -R transmission:transmission /downloads  
  
COPY config/settings.json /home/transmission/.config/transmission-
daemon/settings.json  
COPY start_service.sh /start_service.sh  
COPY transmission_cleaner.sh /transmission_cleaner.sh  
RUN chmod +x /transmission_cleaner.sh  
  
VOLUME ["/seedbox"]  
RUN chmod 777 /seedbox  
  
EXPOSE 9091 51413/tcp 51413/udp  
  
CMD ["/bin/bash", "/start_service.sh"]  

