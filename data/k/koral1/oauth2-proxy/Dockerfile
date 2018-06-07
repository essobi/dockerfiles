FROM golang:1.8-alpine  
  
ENV OAUTH2_PROXY_VERSION=2.1  
ENV GOLANG_VERSION=1.6  
ENV ARCHIVE=oauth2_proxy-$OAUTH2_PROXY_VERSION.linux-amd64.go$GOLANG_VERSION  
ENV PATH /opt/oauth2-proxy/bin:$PATH  
  
RUN apk add --update openssl && mkdir -p /opt/oauth2-proxy/bin && mkdir
/opt/oauth2-proxy/etc && \  
wget -qO-
https://github.com/bitly/oauth2_proxy/releases/download/v$OAUTH2_PROXY_VERSION/$ARCHIVE.tar.gz
| \  
tar xz --strip-components 1 -C /opt/oauth2-proxy/bin  
  
CMD oauth2_proxy -config=/etc/oauth2_proxy.cfg  

