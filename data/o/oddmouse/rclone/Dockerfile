FROM alpine:3.4  
  
ENV GOBIN /usr/sbin  
ENV GOPATH /tmp/go  
ENV RCLONE_CONFIG /etc/rclone.conf  
  
RUN apk add --no-cache --update \  
ca-certificates \  
fuse \  
git \  
go \  
&& go get -u -v github.com/ncw/rclone \  
&& apk del git go \  
&& rm -rf \  
$GOPATH \  
/tmp/* \  
/var/cache/apk/*  
  
CMD ["rclone"]  

