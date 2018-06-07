FROM alpine:3.2  
MAINTAINER WOW! Group Development  
  
RUN apk -Uv add openssl \  
&& wget -qO- https://github.com/remind101/emp/releases/download/v0.9.2/emp-
linux-amd64-0.9.2.tgz | tar -C /usr/local/bin/ -xzf - \  
&& chmod +x /usr/local/bin/emp \  
&& apk --purge -v del openssl \  
&& rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["/usr/local/bin/emp"]  

