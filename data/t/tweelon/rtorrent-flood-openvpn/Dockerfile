FROM node:7.9.0  
RUN apt-get update; \  
apt-get install -y \  
make \  
gcc \  
g++ \  
git \  
cron \  
curl \  
expect \  
openvpn \  
screen \  
mediainfo \  
zlib1g-dev \  
libssl-dev \  
libncurses5-dev \  
libcurl4-openssl-dev \  
pkg-config  
  
ARG LIBTORRENT=libtorrent-0.13.6  
ARG RTORRENT=rtorrent-0.9.6  
RUN cd /tmp && \  
git clone https://github.com/mirror/xmlrpc-c.git /tmp/xmlrpc && \  
curl http://rtorrent.net/downloads/${LIBTORRENT}.tar.gz | tar xz && \  
curl http://rtorrent.net/downloads/${RTORRENT}.tar.gz | tar xz && \  
cd /tmp/${LIBTORRENT} && \  
./configure && \  
make && \  
make install && \  
cd /tmp/xmlrpc/stable && \  
./configure && \  
make && \  
make install && \  
cd /tmp/${RTORRENT} && \  
./configure --with-xmlrpc-c && \  
make && \  
make install && \  
ldconfig && \  
git clone https://github.com/jfurrow/flood.git /flood  
  
COPY ./import/config.js /flood/config.js  
RUN cd flood && \  
npm install && \  
npm run build  
  
RUN apt remove --purge --auto-remove -y \  
git \  
gcc \  
g++ \  
make \  
&& rm -fr /tmp/xmlrpc /tmp/${LIBTORRENT} /tmp/${RTORRENT} \  
&& npm cache clean --force  
  
ENV UID=0 \  
GID=0  
COPY ./import/meta /etc/cron.d/meta  
RUN chmod 0644 /etc/cron.d/meta  
  
COPY ./import/rtorrent.rc /tmp/.rtorrent.rc  
COPY ./scripts /scripts/  
  
EXPOSE 3000 49876 49876/udp  
  
VOLUME /data /config  
  
WORKDIR /flood  
  
CMD ["sh", "/scripts/start.sh"]  

