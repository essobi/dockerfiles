FROM alpine:3.5  
  
LABEL caddy-version=0.10.2  
  
RUN mkdir -p /caddy /web \  
&& addgroup -g 1000 -S caddy \  
&& adduser -S -D -G caddy -u 1000 -h /caddy caddy \  
&& chown -R caddy:caddy /caddy /web \  
&& apk add --update --no-cache --virtual .deps tar curl libcap \  
&& apk add --update --no-cache tini ca-certificates \  
&& curl --silent --show-error --fail --location \  
\--header "Accept: application/tar+gzip, application/x-gzip,
application/octet-stream" \  
-o caddy.tar.gz \  
"https://github.com/mholt/caddy/releases/download/v0.10.2/caddy_v0.10.2_linux_amd64.tar.gz"
\  
&& echo "de7b6a4301bdb5ae5c066e123d71efa9e73156878a43629ced45d8adfe5510c5
caddy.tar.gz" > checksum \  
&& sha256sum caddy.tar.gz \  
&& sha256sum -c checksum \  
&& tar --no-same-owner -C /usr/bin/ -xzf caddy.tar.gz caddy \  
&& rm caddy.tar.gz checksum \  
&& setcap cap_net_bind_service=+ep /usr/bin/caddy \  
&& apk del .deps  
  
ENTRYPOINT ["/sbin/tini"]  

