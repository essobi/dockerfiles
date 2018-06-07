FROM alpine:3.3  
  
ENV CONFIG_SOURCE="" \  
GOROOT=/usr/lib/go \  
GOPATH=/gopath \  
GOBIN=/usr/bin \  
AWS_REGION=us-west-2  
  
RUN apk add -U --no-cache go bash git gnupg && \  
go get -v github.com/ncw/rclone && \  
adduser -D orbit && \  
apk del --purge go git && \  
rm -rf /var/cache/apk && \  
rm -rf /gopath && \  
mkdir /config  
  
WORKDIR /home/orbit/  
  
VOLUME /config  
  
COPY sync-config.sh /usr/bin/sync-config  
COPY rclone.conf.template /home/orbit/.rclone.conf.template  
  
CMD chown -R orbit: /config && su -c "sync-config" orbit  

