FROM docker:1.13  
  
LABEL maintainer "Michael Baudino <michael.baudino@alpine-lab.com>"  
  
ENV GLIBC="2.23-r3" \  
DOCKER_COMPOSE_VERSION="1.11.1"  
  
RUN apk update && apk add --no-cache openssl ca-certificates \  
&& wget -q -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub \  
&& wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/$GLIBC/glibc-$GLIBC.apk \  
&& apk add --no-cache glibc-$GLIBC.apk && rm glibc-$GLIBC.apk \  
&& ln -s /lib/libz.so.1 /usr/glibc-compat/lib/ \  
&& ln -s /lib/libc.musl-x86_64.so.1 /usr/glibc-compat/lib \  
&& wget -q -O /usr/local/bin/docker-compose
https://github.com/docker/compose/releases/download/$DOCKER_COMPOSE_VERSION/docker-
compose-Linux-x86_64 \  
&& chmod +x /usr/local/bin/docker-compose  
  
COPY docker_compose_linked_services attach_linked_services_logs
/usr/local/bin/  
  
CMD ["attach_linked_services_logs"]  

