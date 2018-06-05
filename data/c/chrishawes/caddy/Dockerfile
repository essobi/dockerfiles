FROM alpine:3.4  
ARG
plugins=cors,filemanager,git,hugo,ipfilter,jwt,locale,mailout,minify,prometheus,ratelimit,realip,search,upload,cloudflare,digitalocean,dnsimple,dyn,gandi,googlecloud,namecheap,rfc2136,route53,vultr  
  
RUN apk --update --no-cache add openssh-client git tar curl libcap && \  
curl --silent --show-error --fail --location \  
\--header "Accept: application/tar+gzip, application/x-gzip,
application/octet-stream" -o - \  
"https://caddyserver.com/download/build?os=linux&arch=amd64&features=${plugins}"
\  
| tar --no-same-owner -C /usr/bin/ -xz caddy && \  
chmod 0755 /usr/bin/caddy && \  
addgroup -S caddy && adduser -D -S -s /sbin/nologin -G caddy caddy && \  
setcap cap_net_bind_service=+ep /usr/bin/caddy && \  
mkdir -p /caddy && \  
/usr/bin/caddy -version  
  
EXPOSE 80 443 2015  
WORKDIR /srv  
  
COPY Caddyfile /etc/Caddyfile  
COPY index.html /srv/index.html  
  
RUN chown -R caddy:caddy /srv  
  
VOLUME /caddy  
  
ENV CADDYPATH /caddy  
USER caddy  
  
ENTRYPOINT ["/usr/bin/caddy"]  
CMD ["--conf", "/etc/Caddyfile", "--log", "stdout"]  

