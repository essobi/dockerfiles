FROM resin/armhf-alpine:latest  
MAINTAINER orbsmiv@hotmail.com  
  
RUN [ "cross-build-start" ]  
  
ARG mosquitto_ver="v1.4.15"  
ARG cares_ver="1_13_0"  
  
RUN apk --no-cache -U add \  
build-base \  
autoconf \  
automake \  
libtool \  
popt-dev \  
libconfig-dev \  
openssl-dev \  
curl \  
libwebsockets-dev \  
util-linux-dev \  
coreutils \  
&& mkdir /root/mosquitto \  
&& cd /root/mosquitto \  
&& mkdir ./ares \  
&& cd ./ares \  
&& curl -L -o ./ares.tar.gz
https://github.com/c-ares/c-ares/archive/cares-${cares_ver}.tar.gz \  
&& tar -zxvf ares.tar.gz --strip-components=1 \  
&& ./buildconf \  
&& ./configure \  
&& make \  
&& make install \  
&& cd /root/mosquitto \  
&& curl -L -o ./mosquitto.tar.gz
https://github.com/eclipse/mosquitto/archive/${mosquitto_ver}.tar.gz \  
&& tar -zxvf mosquitto.tar.gz --strip-components=1 \  
&& make binary WITH_WEBSOCKETS=yes \  
&& make install WITH_DOCS=no \  
&& mkdir -p /mosquitto/config/conf.d /mosquitto/data /mosquitto/log \  
&& cp mosquitto.conf /mosquitto/config/mosquitto.conf.example \  
&& apk --purge del \  
build-base \  
autoconf \  
automake \  
libtool \  
popt-dev \  
libconfig-dev \  
curl \  
&& rm -rf \  
/etc/ssl \  
/lib/apk/db/* \  
/root/mosquitto  
  
RUN addgroup -S mosquitto \  
&& adduser -S -D -H -G mosquitto mosquitto \  
&& chown mosquitto:mosquitto /mosquitto/data /mosquitto/log  
  
COPY mosquitto.conf /mosquitto/config/  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["/usr/local/sbin/mosquitto", "-c", "/mosquitto/config/mosquitto.conf"]  
  
RUN [ "cross-build-end" ]  

