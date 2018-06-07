FROM alpine:latest  
MAINTAINER "Hau Nguyen Trung <haunt.hcm2015@gmail.com>"
architecture="AMD64/x86_64"  
RUN apk add --no-cache curl bash libcap \  
&& curl curl https://getcaddy.com | bash -s personal \  
&& chmod 0755 /usr/local/bin/caddy \  
&& addgroup -S caddy \  
&& adduser -D -S -H -s /sbin/nologin -G caddy caddy \  
&& setcap CAP_NET_BIND_SERVICE=+eip /usr/local/bin/caddy \  
&& apk del curl bash libcap  
  
EXPOSE 80 443 2015  
# VOLUME /srv  
WORKDIR /srv  
  
COPY files/Caddyfile /etc/Caddyfile  
COPY files/index.html /srv/index.html  
  
RUN chown -R caddy:caddy /srv  
  
USER caddy  
  
ENTRYPOINT ["/usr/local/bin/caddy"]  
CMD ["--conf", "/etc/Caddyfile"]  
  

