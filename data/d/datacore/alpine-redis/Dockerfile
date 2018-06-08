FROM registry.timmertech.nl/docker/alpine-base:latest  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG REDIS_VERSION  
  
LABEL \  
maintainer="G.J.R. Timmer <gjr.timmer@gmail.com>" \  
nl.timmertech.build-date=${BUILD_DATE} \  
nl.timmertech.name=alpine-redis \  
nl.timmertech.vendor=timmertech.nl \  
nl.timmertech.vcs-url="https://github.com/GJRTimmer/docker-alpine-redis.git" \  
nl.timmertech.vcs-ref=${VCS_REF} \  
nl.timmertech.license=MIT  
  
RUN echo 'http://nl.alpinelinux.org/alpine/edge/main' >> /etc/apk/repositories
&& \  
apk add --update --no-cache redis=${REDIS_VERSION}  
  
COPY rootfs/ /  
  
EXPOSE 6379/tcp  
EXPOSE 26379/tcp  
  
VOLUME ["/var/lib/redis", "/var/log/redis"]  

