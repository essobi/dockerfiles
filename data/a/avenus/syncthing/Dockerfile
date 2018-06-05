FROM alpine:3.4  
MAINTAINER avenus.pl  
  
ENV SYNCTHING_VERSION=0.14.27  
RUN \  
apk update && apk upgrade && apk --update add --no-cache --virtual .build-
dependencies wget  
  
RUN \  
wget --no-check-certificate
https://github.com/syncthing/syncthing/releases/download/v$SYNCTHING_VERSION/syncthing-
linux-amd64-v$SYNCTHING_VERSION.tar.gz -O sycnthing.tar.gz && \  
tar zxvf sycnthing.tar.gz && \  
mv syncthing-linux-amd64-v$SYNCTHING_VERSION/syncthing /usr/sbin/ && \  
rm sycnthing.tar.gz -r && \  
mkdir -p /data && \  
mkdir -p /config && \  
addgroup -g 82 -S www-data && \  
adduser -u 82 -S -D -G www-data -h /data -s /sbin/nologin www-data && \  
chown -R www-data:www-data /data && \  
echo "Delete Build pkgs" && \  
apk del .build-dependencies && \  
rm -rvf /var/cache/apk/* && \  
rm -rvf /tmp/* && \  
rm -rvf /src && \  
rm -rvf /var/log/*  
  
EXPOSE 8384 22000 21027/udp  
  
COPY syncthing.sh /syncthing.sh  
RUN chmod +x /syncthing.sh  
  
VOLUME ["/data", "/config"]  
  
CMD ["/syncthing.sh"]  

