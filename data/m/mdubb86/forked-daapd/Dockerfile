FROM ubuntu:xenial  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
git \  
autotools-dev \  
autoconf \  
libtool \  
gettext \  
gawk \  
gperf \  
antlr3 \  
libantlr3c-dev \  
libconfuse-dev \  
libunistring-dev \  
libsqlite3-dev \  
libavcodec-dev \  
libavformat-dev \  
libavfilter-dev \  
libswscale-dev \  
libavutil-dev \  
libasound2-dev \  
libmxml-dev \  
libgcrypt11-dev \  
libavahi-client-dev \  
zlib1g-dev \  
libevent-dev \  
libjson-c-dev \  
libgnutls-dev \  
libprotobuf-c-dev  
  
RUN git clone https://github.com/ejurgensen/forked-daapd.git && \  
cd forked-daapd && \  
autoreconf -i && \  
./configure --prefix=/usr --sysconfdir=/conf --localstatedir=/var && \  
make && \  
make install  
  
#ENTRYPOINT ["/init"]  
#EXPOSE 8883  
#VOLUME /mosquitto /etc/letsencrypt  
# Install services  
#COPY services /etc/services.d  
# Install init.sh as init script  
#COPY init.sh /etc/cont-init.d/  
# Download and extract s6 init  
#ADD https://github.com/just-
containers/s6-overlay/releases/download/v1.19.1.1/s6-overlay-amd64.tar.gz
/tmp/  
#RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /  

