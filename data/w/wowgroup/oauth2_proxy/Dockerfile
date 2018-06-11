FROM gliderlabs/alpine:3.3  
MAINTAINER WOW! Group Development  
  
RUN apk -Uv add curl \  
&& curl -L
https://github.com/bitly/oauth2_proxy/releases/download/v2.0.1/oauth2_proxy-2.0.1.linux-
amd64.go1.4.2.tar.gz \  
| tar -xvz -C /tmp \  
&& mv /tmp/oauth2_proxy*/oauth2_proxy /usr/local/bin/ \  
&& chmod +x /usr/local/bin/oauth2_proxy \  
&& apk --purge -v del curl \  
&& rm -rf /tmp/* /var/cache/apk/*  
  
ENTRYPOINT ["/usr/local/bin/oauth2_proxy"]  

