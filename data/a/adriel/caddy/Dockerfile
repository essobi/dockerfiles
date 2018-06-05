FROM alpine:3.7  
MAINTAINER Adriel Kloppenburg  
  
LABEL caddy_version="0.11.0" architecture="amd64"  
  
ARG plugins=http.git,tls.dns.cloudflare  
  
RUN apk add --no-cache git tar curl  
  
RUN curl --silent --show-error --fail --location \  
\--header "Accept: application/tar+gzip, application/x-gzip,
application/octet-stream" -o - \  
"https://caddyserver.com/download/linux/amd64?plugins=${plugins}&license=personal&telemetry=on"
\  
| tar --no-same-owner -C /usr/bin/ -xz caddy \  
&& chmod 0755 /usr/bin/caddy \  
&& /usr/bin/caddy -version  
  
EXPOSE 80 443 2015  
VOLUME /root/.caddy /srv  
WORKDIR /srv  
  
COPY Caddyfile /etc/Caddyfile  
COPY index.html /srv/index.html  
  
ENTRYPOINT ["/usr/bin/caddy"]  
CMD ["--conf", "/etc/Caddyfile", "--log", "stdout", "--agree"]  

