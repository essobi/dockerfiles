FROM alpine:edge  
  
LABEL maintainer="github@lplab.net" \  
version="1.1.0" \  
description="Caching DNS resolver for a local LAN. Based on Alpine and
Unbound"  
  
ENV DATA_DIR=/data  
  
# Add testing repository for daemontools retrieve  
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories  
  
RUN apk update && \  
apk upgrade && \  
apk add wget gnupg procps less ca-certificates acf-core acf-unbound alpine-
conf unbound bash  
  
# Use a dummy root password, will be changed at container startup via CLI  
RUN echo -n root:test123 | chpasswd  
  
RUN /sbin/setup-acf && \  
rm -f /etc/unbound/unbound.conf  
  
COPY unbound.conf.git /etc/unbound/unbound.conf  
  
RUN apk add --update tini  
  
COPY entrypoint.sh /sbin/entrypoint.sh  
RUN chmod 755 /sbin/entrypoint.sh  
  
EXPOSE 53/udp 53/tcp 443/tcp  
VOLUME ["${DATA_DIR}"]  
ENTRYPOINT ["/sbin/tini", "--"]  
  
CMD ["/sbin/entrypoint.sh"]  

