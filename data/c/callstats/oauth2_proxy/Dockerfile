FROM alpine:3.5  
  
RUN apk add --no-cache --virtual .fetch-deps \  
ca-certificates \  
openssl \  
tar \  
&& wget -O /oauth2_proxy.tar.gz
https://github.com/bitly/oauth2_proxy/releases/download/v2.2/oauth2_proxy-2.2.0.linux-
amd64.go1.8.1.tar.gz \  
&& tar -xzf /oauth2_proxy.tar.gz \  
&& mv oauth2_proxy-2.2.0.linux-amd64.go1.8.1/oauth2_proxy / \  
&& rm -rf oauth2_proxy-2.2.0.linux-amd64.go1.8.1 \  
&& rm /oauth2_proxy.tar.gz \  
&& apk del .fetch-deps \  
&& apk add --no-cache ca-certificates  
  
ENTRYPOINT ["/oauth2_proxy"]  

