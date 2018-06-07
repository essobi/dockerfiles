FROM lsiobase/alpine  
  
# install packages and symlink libs  
WORKDIR /var/tmp/  
RUN \  
echo "**** install build packages ****" && \  
apk add --no-cache --virtual=build-dependencies \  
build-base \  
git \  
psmisc \  
openssl-dev \  
util-linux-dev \  
mc \  
nano \  
htop && \  
echo "**** Clone and compile xupnpd source code ****" && \  
git clone https://github.com/clark15b/xupnpd.git && \  
cd xupnpd/src && \  
make && \  
mkdir -p \  
/etc/xupnpd && \  
mv /var/tmp/xupnpd/src/* /etc/xupnpd && \  
sed -i "s|interface='lo'|interface='br0'|g" "/etc/xupnpd/xupnpd.lua" && \  
sed -i "s|cfg.daemon=false|cfg.daemon=true|g" "/etc/xupnpd/xupnpd.lua" && \  
# cleanup  
rm -rf \  
/var/tmp/xupnpd  
COPY root/ /  
WORKDIR /  
# ports and volumes  
EXPOSE 4044  

