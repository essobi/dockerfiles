FROM resin/raspberrypi3-node:latest  
MAINTAINER orbsmiv@hotmail.com  
  
RUN [ "cross-build-start" ]  
  
# Set environment variables  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOMEBRIDGE_VER=0.4.31  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
avahi-daemon \  
avahi-discover \  
build-essential \  
iputils-ping \  
libavahi-compat-libdnssd-dev \  
libnss-mdns \  
libtool \  
autoconf \  
automake \  
git && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir /tmp/compile-libcoap  
WORKDIR /tmp/compile-libcoap  
RUN git clone \--depth 1 --recursive -b dtls https://github.com/home-
assistant/libcoap.git /tmp/compile-libcoap && \  
./autogen.sh && \  
./configure --disable-documentation --disable-shared --without-debug
CFLAGS="-D COAP_DEBUG_FD=stderr" && \  
make && \  
make install && \  
rm -rf /tmp/compile-libcoap  
  
RUN npm install -g --unsafe-perm \  
homebridge@$HOMEBRIDGE_VER \  
hap-nodejs \  
node-gyp && \  
cd /usr/local/lib/node_modules/homebridge/ && \  
npm install --unsafe-perm bignum && \  
cd /usr/local/lib/node_modules/hap-nodejs/node_modules/mdns && \  
node-gyp BUILDTYPE=Release rebuild  
  
RUN mkdir -p /var/run/dbus/  
  
RUN mkdir -p /root/.homebridge  
WORKDIR /root/.homebridge  
COPY start.sh /root/.homebridge/start.sh  
  
EXPOSE 5353 51826  
CMD ["/bin/sh", "/root/.homebridge/start.sh"]  
  
RUN [ "cross-build-end" ]  

