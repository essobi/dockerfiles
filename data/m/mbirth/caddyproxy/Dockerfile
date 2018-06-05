#FROM container4armhf/armhf-alpine  
FROM alpine  
  
MAINTAINER Markus Birth <markus@birth-online.de>  
  
LABEL description="Caddy HTTP/2 web server" \  
version="1.0"  
  
ENV AGREE_TOS="true" \  
CADDY_ARCH="amd64" \  
DEFAULT_EMAIL="changeme@example.com"  
COPY ["caddy.d", "/data/caddy.d/"]  
COPY ["compile_and_run.sh", "/usr/local/bin/"]  
  
RUN apk add --update sed wget \  
&& mkdir -p /data/caddy.d \  
&& wget --no-check-certificate -q -O /tmp/caddy.tar.gz
"https://caddyserver.com/download/build?os=linux&arch=${CADDY_ARCH}&features="
\  
&& mkdir -p /opt/caddy \  
&& cd /opt/caddy \  
&& tar xzf /tmp/caddy.tar.gz \  
&& rm /tmp/caddy.tar.gz \  
&& chmod a+x /usr/local/bin/compile_and_run.sh \  
&& apk del wget \  
&& rm -rf /var/cache/*  
  
VOLUME ["/data"]  
  
EXPOSE 80 443  
CMD ["/usr/local/bin/compile_and_run.sh"]  

