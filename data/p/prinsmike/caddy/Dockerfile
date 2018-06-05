FROM alpine:latest  
MAINTAINER prinsmike  
  
ENV HUGO_VERSION 0.18.1  
ENV HUGO_ARCHIVE hugo_${HUGO_VERSION}_Linux-64bit  
ENV HUGO_BIN hugo_${HUGO_VERSION}_linux_amd64  
  
RUN apk add --no-cache openssh-client git tar curl \  
&& curl --silent --show-error --fail --location \  
\--header "Accept: application/tar+gzip, application/x-gzip,
application/octet-stream" -o - \  
"https://caddyserver.com/download/build?os=linux&arch=amd64&features=expires%2Cfilemanager%2Cfilter%2Cgit%2Chugo%2Cipfilter%2Cjsonp%2Cjwt%2Cmailout%2Cminify%2Cmultipass%2Cprometheus%2Cratelimit%2Csearch%2Cupload"
\  
| tar --no-same-owner -C /usr/bin/ -xz caddy \  
&& chmod 0755 /usr/bin/caddy \  
&& /usr/bin/caddy -version \  
&& curl --silent --show-error --fail --location \  
\--header "Accept: application/tar+gzip, application/x-gzip,
application/octet-stream" -o - \  
"https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/${HUGO_ARCHIVE}.tar.gz"
\  
| tar --no-same-owner -C /tmp/ -xz \  
&& mv /tmp/${HUGO_BIN}/${HUGO_BIN} /usr/local/bin/hugo \  
&& rm -rf /tmp/*  
  
EXPOSE 80 443 2015  
VOLUME /root/.caddy  
WORKDIR /srv  
  
COPY Caddyfile /etc/Caddyfile  
  
ENTRYPOINT ["/usr/bin/caddy"]  
CMD ["--conf", "/etc/Caddyfile", "--log", "stdout"]  

