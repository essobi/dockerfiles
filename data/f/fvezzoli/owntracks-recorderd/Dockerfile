FROM alpine:3.7  
LABEL version="edge" description="OwnTracks Recorder"  
LABEL authors="Francesco Vezzoli <fvezzoli@iz2vtw.net>"  
  
ENV VERSION=0.7.5  
RUN apk add --no-cache build-base mosquitto-dev lua-dev libsodium-dev curl-dev
libconfig-dev ca-certificates curl python openssl && \  
update-ca-certificates && \  
wget -O recorder.tar.gz
https://github.com/owntracks/recorder/archive/$VERSION.tar.gz && \  
tar xzf recorder.tar.gz && \  
cd recorder-$VERSION && \  
sed -e 's/WITH_LUA ?= no/WITH_LUA ?= yes/' -e 's/WITH_ENCRYPT ?=
no/WITH_ENCRYPT ?= yes/' -e 's/STORAGEDEFAULT = .*/STORAGEDEFAULT =
\/owntracks\/recorder\/store/' config.mk.in > config.mk && \  
make && make install && \  
cd .. && rm -r recorder*  
  
# data volume  
VOLUME /owntracks  
  
COPY ot-recorder.default /etc/default/ot-recorder  
COPY recorder-launcher.sh /usr/local/bin/recorder-launcher.sh  
COPY recorder-health.sh /usr/local/bin/recorder-health.sh  
  
HEALTHCHECK \--interval=5m --timeout=30s CMD /usr/local/bin/recorder-health.sh  
  
RUN mkdir -p -m 775 /owntracks/recorder/store && \  
chmod 755 /usr/local/bin/recorder-launcher.sh /usr/local/bin/recorder-
health.sh  
  
EXPOSE 8083  
CMD ["/usr/local/bin/recorder-launcher.sh"]  

