FROM alpine:3.5  
LABEL maintainer "Carl Mercier <foss@carlmercier.com>"  
LABEL caddy_version="0.10.10" architecture="amd64"  
  
ARG
plugins=dyndns,http.authz,http.cache,http.cgi,http.cors,http.expires,http.filemanager,http.filter,http.forwardproxy,http.git,http.hugo,http.ipfilter,http.jekyll,http.jwt,http.locale,http.login,http.nobots,http.proxyprotocol,http.ratelimit,http.realip,http.reauth,http.upload  
ARG dns=tls.dns.cloudflare,tls.dns.namecheap,tls.dns.rfc2136  
  
RUN apk add --no-cache openssh-client git tar curl ca-certificates bash &&
update-ca-certificates  
  
RUN curl --silent https://getcaddy.com | /bin/bash -s personal $plugins,$dns  
  
RUN mkdir -p /opt/assets  
  
EXPOSE 80 443 2015  
  
VOLUME /var/www  
VOLUME /caddy  
WORKDIR /var/www  
WORKDIR /caddy  
  
ENV CADDYPATH=/caddy/.caddy  
ENV RUN_ARGS=  
  
COPY Caddyfile /caddy/  
COPY index.html /var/www/  
COPY Caddyfile /opt/assets/  
COPY index.html /opt/assets/  
COPY start.sh /  
  
ENTRYPOINT ["/start.sh"]  

