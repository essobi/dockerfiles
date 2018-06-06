FROM alpine:3.6  
COPY rootfs /  
  
RUN apk add --no-cache clamav rsyslog clamav-libunrar curl dpkg && \  
# install gosu  
dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" && \  
curl -fsSL
"https://github.com/tianon/gosu/releases/download/1.10/gosu-$dpkgArch" -o
/usr/local/bin/gosu && \  
chmod +x /usr/local/bin/gosu && \  
gosu nobody true && \  
# complete gosu  
mkdir /clamav /run/clamav && \  
chown clamav:clamav /clamav /run/clamav && \  
chmod +x /start.sh && \  
apk del curl dpkg && \  
rm -rf /apk /tmp/* /var/cache/apk/*  
  
CMD ["/start.sh"]  

