FROM alpine:3.4  
MAINTAINER Zoltan Burgermeiszter <zoltan@burgermeiszter.com>  
  
ENV VERSION="v0.14.3" \  
ARCH="amd64" \  
CHOWN="/usr/bin"  
RUN apk add --no-cache --update curl tar && \  
curl -L
https://github.com/syncthing/syncthing/releases/download/${VERSION}/syncthing-
linux-${ARCH}-${VERSION}.tar.gz | tar xvz -C /usr/bin syncthing-
linux-${ARCH}-${VERSION}/syncthing --strip-components=1 --same-permissions &&
\  
apk del curl tar  
  
VOLUME ["/syncthing"]  
WORKDIR "/syncthing"  
EXPOSE 8384 22000 21027/UDP  
  
ADD start.sh /sbin/start.sh  
RUN chmod +x /sbin/start.sh  
  
ADD my_init /sbin/my_init  
RUN chmod +x /sbin/my_init  
ENTRYPOINT ["/sbin/my_init"]  
  
CMD ["/sbin/start.sh"]

