FROM alpine:3.7  
LABEL maintainer "Darwin Smith II <dwin@dlsmi.com>"  
  
LABEL caddy_version="0.10.14" architecture="amd64"  
  
ARG plugins=http.cache,http.git,http.ratelimit,tls.dns.cloudflare,http.hugo  
  
RUN apk add --no-cache openssh-client git tar curl  
  
RUN curl --silent --show-error --fail --location \  
\--header "Accept: application/tar+gzip, application/x-gzip,
application/octet-stream" -o - \  
"https://caddyserver.com/download/linux/amd64?plugins=${plugins}&license=personal"
\  
| tar --no-same-owner -C /usr/bin/ -xz caddy \  
&& chmod 0755 /usr/bin/caddy \  
&& /usr/bin/caddy -version  
  
EXPOSE 80 443 2015  
VOLUME /root/.caddy  
WORKDIR /srv  
  
COPY Caddyfile /etc/Caddyfile  
COPY index.html /srv/www/public/index.html  
  
ENTRYPOINT ["/usr/bin/caddy"]  
CMD ["--conf", "/etc/Caddyfile", "--log", "stdout"]  

