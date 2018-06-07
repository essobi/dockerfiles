FROM alpine:3.5  
LABEL caddy_version="0.10.3" architecture="amd64"  
  
ARG plugins=http.git  
  
RUN apk add --no-cache openssh-client git tar curl  
  
RUN curl --silent --show-error --fail --location \  
\--header "Accept: application/tar+gzip, application/x-gzip,
application/octet-stream" -o - \  
"https://caddyserver.com/download/linux/amd64?plugins=${plugins}" \  
| tar --no-same-owner -C /usr/bin/ -xz caddy \  
&& chmod 0755 /usr/bin/caddy \  
&& /usr/bin/caddy -version  
  
VOLUME /root/.caddy  
WORKDIR /srv  
  
COPY Caddyfile /etc/Caddyfile  
COPY website/ /srv/  
  
EXPOSE 80 443 2015  
ENTRYPOINT ["/usr/bin/caddy"]  
CMD ["--conf", "/etc/Caddyfile", "--log", "stdout"]  

