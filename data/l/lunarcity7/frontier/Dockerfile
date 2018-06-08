FROM alpine:3.7  
ENV \  
caddy="https://caddyserver.com/download/linux/amd64?plugins=http.jwt,http.login&license=personal"
\  
build="ca-certificates" \  
run="curl jq libcap sudo socat"  
  
RUN \  
apk --update add \  
$build \  
$run \  
&& \  
\  
cd /tmp && \  
curl -L $caddy > caddy.tar.gz && \  
tar zxf * && \  
mv caddy /usr/local/bin && \  
setcap cap_net_bind_service=+ep /usr/local/bin/caddy && \  
rm -rf /tmp/* && \  
\  
mkdir /state && \  
\  
apk del $build && \  
rm -rf /var/cache/apk/*  
  
EXPOSE 80 443  
WORKDIR /tmp  
ENV CADDYPATH="/state"  
VOLUME /state  
ENTRYPOINT ["/entrypoint.sh"]  
  
ADD entrypoint.sh /  
ADD daemon.sh /  

