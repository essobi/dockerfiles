FROM containerstack/alpine:3.5.2  
MAINTAINER Remon Lam [remon@containerstack.io]  
  
ENV REGISTRY_VERSION=2.6.1  
ENV CPU_ARCH=amd64  
  
RUN set -ex && \  
apk add --no-cache ca-certificates apache2-utils && \  
rm -rf /var/cache/apk/*  
  
COPY ./registry/registry /bin/registry  
COPY ./registry/config.yml /etc/docker/registry/config.yml  
COPY entrypoint.sh /entrypoint.sh  
  
VOLUME ["/var/lib/registry"]  
  
EXPOSE 5000  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/etc/docker/registry/config.yml"]  

