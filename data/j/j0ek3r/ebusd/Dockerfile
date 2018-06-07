##################################################################################  
## FLAVOR: ALPINE.FRONTAIL ##  
## ##  
## This Dockerfile builds an image for ebusd including the Weishaupt ##  
## message-definitions an frontail for watching ebusd-log on port 80. ##  
## The image is a multistage build: ##  
## * first stage builds the ebusd binaries ##  
## * second stage the resulting image ##  
##################################################################################  
  
##################################################################################  
## FIRST STAGE: BUILD ##  
##################################################################################  
FROM alpine:latest AS stage_build  
  
##################################################################################  
## INSTALL PACKAGES FOR BUILD ##  
##################################################################################  
RUN apk add --no-cache \  
argp-standalone \  
autoconf \  
automake \  
bash \  
curl \  
g++ \  
git \  
make \  
mosquitto-dev  
  
##################################################################################  
## FETCH AND BUILD SOURCES ##  
## ##  
## Results are copied to /build/root ##  
##################################################################################  
WORKDIR /build  
  
# RUN git clone https://github.com/john30/ebusd.git \  
RUN git clone https://github.com/J0EK3R/ebusd.git \  
&& cd ebusd \  
&& ./autogen.sh \  
&& make DESTDIR="/build/root" install-strip \  
&& cp -r contrib/etc /build/root/etc  
  
##################################################################################  
## DOWNLOAD MESSAGE DEFINITIONS ##  
## ##  
## Message definitions are copied to /build/root/etc/ebusd ##  
##################################################################################  
  
# download message definitions from github and expand them to /etc/ebusd  
RUN curl -SL https://github.com/john30/ebusd-
configuration/archive/master.tar.gz \  
| tar xz --strip-components=3 -C /build/root/etc/ebusd ebusd-configuration-
master/ebusd-2.1.x/de  
  
# download message definitions for Weishaupt WTC devices from github and
expand them to /etc/ebusd  
RUN curl -SL https://github.com/J0EK3R/ebusd-configuration-
weishaupt/archive/master.tar.gz \  
| tar xz --strip-components=1 -C /build/root/etc/ebusd ebusd-configuration-
weishaupt-master  
  
##################################################################################  
## SECOND STAGE ##  
##################################################################################  
FROM mhart/alpine-node  
  
##################################################################################  
## ENVIRONMENTAL CONFIG ##  
##################################################################################  
# Set correct environment variables  
ENV EBUSD_ADDRESS="FF"  
ENV EBUSD_SCANCONFIG="full"  
ENV EBUSD_DEVICE="ebus.fritz.box:5000"  
ENV EBUSD_LATENCY="80000"  
ENV EBUSD_RECEIVETIMEOUT="25000"  
ENV EBUSD_ANSWER="true"  
ENV EBUSD_ENABLEHEX="true"  
ENV EBUSD_LOGLEVEL="notice"  
ENV EBUSD_LOGFILE="/var/log/ebusd.log"  
  
ENV EBUSD_MQTTHOST="mqtt.fritz.box"  
ENV EBUSD_MQTTPORT="1883"  
ENV EBUSD_MQTTTOPIC="ebusd/%circuit/%name/%field"  
ENV EBUSD_MQTTRETAIN="true"  
  
ENV EBUSD_VERSION="3.1"  
ENV EBUSD_ARCH="amd64"  
  
ENV TZ="Europe/Berlin"  
  
LABEL maintainer="J0EK3R@gmx.net"  
LABEL version="${EBUSD_VERSION}-${EBUSD_ARCH}"  
  
##################################################################################  
## RUN INSTALL SCRIPT ##  
##################################################################################  
# install required packages  
  
RUN apk add --no-cache \  
argp-standalone \  
bash \  
git \  
libc6-compat \  
libgcc \  
libstdc++ \  
logrotate \  
mosquitto-libs \  
mosquitto-libs++ \  
tzdata  
  
##################################################################################  
## COPY FROM BUILD STAGE ##  
##################################################################################  
  
COPY --from=stage_build /build/root /  
  
##################################################################################  
## COPY LOCAL FILES ##  
##################################################################################  
COPY root /  
  
##################################################################################  
## INSTALL FRONTAIL ##  
##################################################################################  
  
RUN npm i frontail -g  
  
##################################################################################  
## CONTAINER START ##  
##################################################################################  
  
# define start-script as entrypoint  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
##################################################################################  
## EXPORTS AND VOLUMES ##  
##################################################################################  
# Export volumes  
VOLUME /var/log  
  
# expose port for ebusd  
EXPOSE 8888  
EXPOSE 80  

