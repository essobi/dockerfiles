FROM alpine:3.2  
MAINTAINER Benjamin Halsted <bhalsted@gmail.com>  
  
ENV MOSQUITTO_VERSION 1.4.5  
RUN echo 'http://dl-4.alpinelinux.org/alpine/edge/main' >>
/etc/apk/repositories  
  
RUN apk --update add git postgresql-dev util-linux-dev c-ares-dev build-base
hiredis-dev && rm -rf /var/cache/apk/*  
  
# COMPILE MOSQUITTO  
ADD http://mosquitto.org/files/source/mosquitto-${MOSQUITTO_VERSION}.tar.gz
/build/  
RUN cd /build && tar xvfz mosquitto-${MOSQUITTO_VERSION}.tar.gz && \  
cd /build/mosquitto-${MOSQUITTO_VERSION} && make  
  
# COMPILE AUTH MODULE WITH REDIS & POSTGRES  
RUN cd /build && git clone https://github.com/jpmens/mosquitto-auth-plug.git
&& \  
cd /build/mosquitto-auth-plug && cp config.mk.in config.mk && \  
sed -i.bak 's/BACKEND_MYSQL \?= yes/BACKEND_MYSQL \?= no/' /build/mosquitto-
auth-plug/config.mk && \  
sed -i.bak 's/BACKEND_REDIS \?= no/BACKEND_REDIS \?= yes/' /build/mosquitto-
auth-plug/config.mk && \  
sed -i.bak 's/BACKEND_POSTGRES \?= no/BACKEND_POSTGRES \?= yes/'
/build/mosquitto-auth-plug/config.mk && \  
sed -i.bak 's/MOSQUITTO_SRC =/MOSQUITTO_SRC =
\/build\/mosquitto-${MOSQUITTO_VERSION}/' /build/mosquitto-auth-plug/config.mk
&& \  
cd /build/mosquitto-auth-plug && make  
  
CMD ["/bin/sh"]  

