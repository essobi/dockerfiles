FROM alpine:3.5  
MAINTAINER Dmitry Prazdnichnov <dp@bambucha.org>  
  
ARG BUILD_DATE  
ARG VERSION  
ARG VCS_REF  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.version=$VERSION \  
org.label-schema.vcs-url=https://github.com/bambocher/docker-syncthing-inotify
\  
org.label-schema.license=MIT \  
org.label-schema.schema-version=1.0  
  
ENV URL=github.com/syncthing/syncthing-inotify \  
XDG_CONFIG_HOME=/ \  
GOPATH=/  
  
RUN apk --no-cache add ca-certificates curl \  
&& apk --no-cache --virtual build-dependencies add go godep git libc-dev \  
&& git clone -b v$VERSION https://$URL /src/$URL \  
&& cd /src/$URL \  
&& godep get \  
&& cd / \  
&& rm -rf /src /pkg \  
&& apk del build-dependencies  
  
COPY ./entrypoint.sh /  
  
USER 1000:1000  
VOLUME ["/syncthing", "/mnt"]  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["-target=http://syncthing:8384", "-logflags=0"]  

