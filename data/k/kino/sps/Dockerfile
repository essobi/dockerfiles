FROM kino/conts:deb  
ENV VVV=/usr/local/docker/shairport-sync  
  
RUN (apt-get install -y g++ autoconf automake libtool libdaemon-dev
libasound2-dev libpopt-dev libconfig-dev \  
avahi-daemon libavahi-client-dev libssl-dev)  
  
RUN (git clone https://github.com/mikebrady/shairport-sync.git; \  
cd shairport-sync; \  
autoreconf -i -f; \  
mkdir -p ${VVV}/src; \  
./configure --with-alsa --with-avahi --with-ssl=openssl --with-metadata
--with-systemd; \  
getent group shairport-sync &>/dev/null || sudo groupadd -r shairport-sync
>/dev/null; \  
getent passwd shairport-sync &> /dev/null || sudo useradd -r -M -g shairport-
sync -s /usr/bin/nologin -G audio shairport-sync >/dev/null; \  
cp -R . ${VVV}/src/; \  
make install DESTDIR=${VVV})  
  
EXPOSE 22  
CMD ["/usr/local/startservice.sh"]  

