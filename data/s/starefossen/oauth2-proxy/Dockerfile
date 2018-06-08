FROM alpine:3.6  
  
ENV OAUTH2_PROXY_SHORT_VERSION=2.2  
ENV OAUTH2_PROXY_VERSION=2.2.0  
ENV GOLANG_VERSION=1.8.1  
ENV ARCHIVE=oauth2_proxy-$OAUTH2_PROXY_VERSION.linux-amd64.go$GOLANG_VERSION  
  
RUN apk add \--no-cache ca-certificates \  
&& apk add \--no-cache --virtual .build-deps curl \  
&& curl -sL -o oauth2_proxy.tar.gz \  
"https://github.com/bitly/oauth2_proxy/releases/download/v$OAUTH2_PROXY_SHORT_VERSION/$ARCHIVE.tar.gz"
\  
&& tar xzvf oauth2_proxy.tar.gz \  
&& cp $ARCHIVE/oauth2_proxy /bin \  
&& chmod +x /bin/oauth2_proxy \  
&& apk del .build-deps  
  
ENTRYPOINT ["oauth2_proxy"]  

