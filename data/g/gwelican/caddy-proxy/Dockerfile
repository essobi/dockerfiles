FROM lsiobase/alpine:3.6  
  
MAINTAINER Gwelican <superfly@gwelican.eu>  
  
ENV DOCKER_GEN_VERSION 0.7.3  
ENV CADDY_OPTIONS ""  
  
RUN mkdir -p /tmp/caddy && \  
apk add --no-cache curl unzip && \  
curl -sL -o /tmp/caddy/caddy_linux_amd64.tar.gz
"https://caddyserver.com/download/linux/amd64?plugins=http.cors" && \  
tar -zxf /tmp/caddy/caddy_linux_amd64.tar.gz -C /tmp/caddy && \  
mv /tmp/caddy/caddy /usr/bin/ && \  
chmod +x /usr/bin/caddy && \  
rm -rf /tmp/caddy && \  
curl -sL -o docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz
https://github.com/jwilder/docker-
gen/releases/download/$DOCKER_GEN_VERSION/docker-gen-linux-
amd64-$DOCKER_GEN_VERSION.tar.gz && \  
tar -C /usr/local/bin -xvzf docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz
&& \  
rm /docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz  
  
RUN printf ":80\nproxy / caddyserver.com" > /etc/Caddyfile  
  
ENV DOCKER_HOST unix:///tmp/docker.sock  
  
COPY root/ /  
  

