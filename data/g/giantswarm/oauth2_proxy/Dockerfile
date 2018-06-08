FROM alpine:3.6  
RUN apk --no-cache add ca-certificates \  
&& apk --no-cache add --virtual .build-deps curl \  
&& curl -L
https://github.com/bitly/oauth2_proxy/releases/download/v2.2/oauth2_proxy-2.2.0.linux-
amd64.go1.8.1.tar.gz \  
| tar -C /usr/local/bin --strip-components 1 -xz \  
&& apk del .build-deps  
  
COPY oauth2_proxy.cfg /etc/oauth2_proxy/  
  
CMD ["oauth2_proxy", "-config=/etc/oauth2_proxy/oauth2_proxy.cfg"]  

