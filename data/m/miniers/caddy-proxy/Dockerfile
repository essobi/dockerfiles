FROM alpine:latest  
MAINTAINER miniers <m@minier.cc>  
LABEL caddy_version="0.10.3" architecture="amd64"  
  
ARG S6_OVERLAY_VERSION=v1.19.1.1  
ARG
plugins=http.git,tls.dns.dnspod,http.filemanager,http.filter,http.upload,net,http.cors  
  
ENV DOCKER_GEN_VERSION 0.7.3  
ENV CADDY_OPTIONS ""  
ENV DOCKER_HOST unix:///tmp/docker.sock  
  
# install s6  
RUN apk add --update --no-cache curl tzdata && \  
curl -sSL https://github.com/just-
containers/s6-overlay/releases/download/${S6_OVERLAY_VERSION}/s6-overlay-
amd64.tar.gz \  
| tar xfz - -C / && \  
cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \  
echo "Asia/Shanghai" > /etc/timezone && \  
apk del tzdata && \  
rm -rf /var/cache/apk/*  
  
# install caddy  
RUN curl --silent --show-error --fail --location \  
\--header "Accept: application/tar+gzip, application/x-gzip,
application/octet-stream" -o - \  
"https://caddyserver.com/download/linux/amd64?plugins=${plugins}" \  
| tar --no-same-owner -C /usr/bin/ -xz caddy \  
&& chmod 0755 /usr/bin/caddy \  
&& /usr/bin/caddy -version  
  
# install docker-gen  
RUN curl -sL docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz
https://github.com/jwilder/docker-
gen/releases/download/$DOCKER_GEN_VERSION/docker-gen-linux-
amd64-$DOCKER_GEN_VERSION.tar.gz | \  
tar -C /usr/local/bin -xvzf -  
  
ADD root /  
  
EXPOSE 80 443 2015  
ENTRYPOINT ["/init"]

