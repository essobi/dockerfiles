FROM alpine:3.5  
MAINTAINER Mitchell Hewes <me@mitcdh.com>  
  
ENV CADDY_FEATURES="git%2Cprometheus%2Crealip"  
  
ADD files/run.sh /caddy-bootstrap/run.sh  
  
RUN apk --update add \  
curl \  
openssh-client \  
git \  
tar \  
ca-certificates \  
&& curl --silent --show-error --fail --location \  
\--header "Accept: application/tar+gzip, application/x-gzip,
application/octet-stream" -o - \  
"https://caddyserver.com/download/build?os=linux&arch=amd64&features=${CADDY_FEATURES}"
\  
| tar --no-same-owner -C /usr/bin/ -xz caddy \  
&& chmod 0755 /usr/bin/caddy \  
&& /usr/bin/caddy -version \  
&& rm -rf /var/cache/apk/* \  
&& addgroup -S www-data -g 1000 \  
&& adduser -S -G www-data -g "Web Server" -h "/www" -u 1000 www-data \  
&& chmod 500 /caddy-bootstrap/run.sh \  
&& mkdir /caddy-bootstrap/pre-run/  
  
WORKDIR /www  
ENTRYPOINT ["/caddy-bootstrap/run.sh"]  

