FROM iotsec/arm-alpine  
  
RUN apk --update add build-base \  
libtool \  
m4 \  
autoconf \  
automake \  
gettext \  
pcre \  
pcre-dev \  
libpcap-dev \  
libnet-dev \  
libcap-ng-dev \  
libcap-ng \  
libmagic \  
libtool \  
libnet-dev \  
mariadb-dev \  
git \  
daq-dev \  
libdnet-dev &&\  
cd /tmp && git clone https://github.com/firnsy/barnyard2 &&\  
cd barnyard2 &&\  
./autogen.sh && ./configure --with-mysql && make && make install &&\  
mkdir /var/log/barnyard2 &&\  
rm -rf /var/cache/apk/*  
  
CMD barnyard2 -c /usr/local/etc/suricata/barnyard2.conf \  
-d /usr/local/var/log/suricata -f unified2.alert -w /usr/local/var/log/suricata/suricata.waldo  

