#  
# Builder  
#  
FROM abiosoft/caddy:builder as builder  
  
ARG version="0.11.0"  
ARG plugins="git"  
RUN VERSION=${version} PLUGINS=${plugins} GOARCH=arm GOARM=7 /bin/sh
/usr/bin/builder.sh  
  
#  
# Final stage  
#  
# FROM alpine:3.6  
FROM resin/armhf-alpine:latest  
MAINTAINER orbsmiv@hotmail.com  
  
RUN [ "cross-build-start" ]  
  
LABEL caddy_version="0.11.0"  
  
RUN apk add --no-cache openssh-client git  
  
# install caddy  
COPY \--from=builder /install/caddy /usr/bin/caddy  
  
# validate install  
RUN /usr/bin/caddy -version  
RUN /usr/bin/caddy -plugins  
  
EXPOSE 80 443 2015  
VOLUME /root/.caddy /srv  
WORKDIR /srv  
  
COPY Caddyfile /etc/Caddyfile  
COPY index.html /srv/index.html  
  
ENTRYPOINT ["/usr/bin/caddy"]  
CMD ["--agree", "--conf", "/etc/Caddyfile", "--log", "stdout"]  
  
RUN [ "cross-build-end" ]  

