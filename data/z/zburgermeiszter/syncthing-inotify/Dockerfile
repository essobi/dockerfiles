FROM alpine:3.4  
MAINTAINER Zoltan Burgermeiszter <zoltan@burgermeiszter.com>  
  
ENV VERSION="v0.8.3" \  
ARCH="amd64"  
RUN apk add --no-cache --update curl tar && \  
curl -L https://github.com/syncthing/syncthing-
inotify/releases/download/${VERSION}/syncthing-inotify-
linux-${ARCH}-${VERSION}.tar.gz | tar xvz -C /usr/bin syncthing-inotify
--same-permissions && \  
apk del curl tar  
  
WORKDIR "/syncthing"  
  
ADD start.sh /sbin/start.sh  
RUN chmod +x /sbin/start.sh  
  
ADD my_init /sbin/my_init  
RUN chmod +x /sbin/my_init  
ENTRYPOINT ["/sbin/my_init"]  
  
CMD ["/sbin/start.sh"]

