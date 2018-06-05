FROM daewood/abase  
MAINTAINER daewood <daewood@qq.com>  
  
RUN mkdir -p /var/lib/registry && \  
addgroup -S registry && \  
adduser -S -D -g "" -G registry -s /bin/sh -h /var/lib/registry registry && \  
chown -R registry:registry /var/lib/registry && \  
apk add --update --repository
http://dl-3.alpinelinux.org/alpine/edge/community/ --allow-untrusted docker-
registry && \  
rm -rf /var/cache/apk/*  
  
COPY rootfs/ /  
  
ENTRYPOINT ["/init"]  
CMD []  
  
EXPOSE 5000  
VOLUME ["/var/lib/registry"]  

