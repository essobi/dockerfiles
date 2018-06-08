FROM alpine:edge  
MAINTAINER Sebastian Knoth <sk@bytepark.de>  
  
ENV S6_VERSION v1.17.2.0  
# Add testing repo to get latest apk packages  
RUN echo "ipv6" >> /etc/modules  
  
## Add basic stuff  
RUN apk add --update --no-cache curl bash  
  
# Add NGINX-Webserver with NAXSI  
RUN apk upgrade -U && \  
apk --update --repository=http://dl-4.alpinelinux.org/alpine/edge/testing add
\  
nginx  
  
COPY /rootfs /  
  
# Small fixes  
RUN rm -fr /var/cache/apk/*  
  
# Add S6-overlay to use S6 process manager  
# https://github.com/just-containers/s6-overlay/#the-docker-way  
ADD https://github.com/just-
containers/s6-overlay/releases/download/${S6_VERSION}/s6-overlay-amd64.tar.gz
/tmp/  
RUN gunzip -c /tmp/s6-overlay-amd64.tar.gz | tar -xf - -C /  
  
# Expose Ports  
EXPOSE 443  
EXPOSE 80  
ENTRYPOINT ["/init"]

