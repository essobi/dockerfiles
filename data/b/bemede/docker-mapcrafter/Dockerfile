ARG DEBIAN_VERSION=jessie  
FROM debian:$DEBIAN_VERSION  
  
LABEL maintainer="Bernd Meyer <be.me@posteo.de>"  
  
ARG DEBIAN_VERSION  
ENV MAPCRAFTER_VERSION=2.4-1  
ENV JOBS=1  
ENV CRON_MIN=30  
ENV CRON_HR=2  
ENV CRON_D=*  
ENV CRON_M=*  
ENV CRON_DOW=*  
  
VOLUME ["/config", "/output", "/world"]  
  
RUN apt-get update && \  
apt-get -y install --no-install-recommends \  
apt-transport-https \  
ca-certificates\  
cron \  
wget && \  
echo "deb http://packages.mapcrafter.org/debian $DEBIAN_VERSION main" >
/etc/apt/sources.list.d/mapcrafter.list && \  
wget -O /etc/apt/trusted.gpg.d/mapcrafter.gpg
http://packages.mapcrafter.org/debian/keyring.gpg && \  
apt-get update && \  
apt-get -y install --no-install-recommends \  
imagemagick \  
mapcrafter=$MAPCRAFTER_VERSION \  
python && \  
apt-get -y remove --purge \  
apt-transport-https \  
ca-certificates \  
imagemagick \  
python \  
wget && \  
apt-get -y autoremove && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD run-container /run-container  
ADD run-mapcrafter /run-mapcrafter  
ADD render.conf /  
  
RUN chmod +x /run-container /run-mapcrafter  
  
CMD ["/run-container"]  

