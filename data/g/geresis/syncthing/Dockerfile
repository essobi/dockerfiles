FROM alpine:latest  
  
MAINTAINER Geresis <docker@mbffm.de>  
  
# LABEL version=1  
# VARIABLES  
ENV SYNCTHING_USER syncthing  
ENV SYNCTHING_GROUP syncthing  
ENV SYNCTHING_UID 22000  
ENV SYNCTHING_GID 22000  
#ENV STNOUPGRADE=1  
ENV RELEASE=  
  
# CREATE GROUP AND USER  
RUN addgroup -g $SYNCTHING_GID $SYNCTHING_GROUP && \  
adduser -h /data -s /sbin/nologin -G $SYNCTHING_GROUP -D -u $SYNCTHING_UID
$SYNCTHING_USER  
  
# CREATE FOLDERS  
RUN mkdir \  
/app \  
/config && \  
chown $SYNCTHING_USER \  
/app \  
/config \  
/data && \  
chmod 700 \  
/app \  
/config && \  
chmod 750 \  
data  
  
# INSTALL PACKAGES  
RUN apk add --update \  
curl \  
jq && \  
rm -rf /var/cache/apk/*  
  
# INSTALL SYNCTHING  
RUN set -x && \  
cd /app && \  
release=${release:-$(curl -s
https://api.github.com/repos/syncthing/syncthing/releases/latest | jq -r
.tag_name )} && \  
curl -s -L
https://github.com/syncthing/syncthing/releases/download/${release}/syncthing-
linux-amd64-${release}.tar.gz | tar -zx && \  
mv syncthing-linux-amd64-*/syncthing . && \  
rm -rf syncthing-linux-amd64-*  
  
# PORTS  
EXPOSE 8384/TCP  
EXPOSE 21027/TCP  
EXPOSE 22000/TCP  
  
# VOLUMES  
VOLUME ["/config"]  
VOLUME ["/data"]  
  
# CHANGE TO USER AND RUN  
USER $SYNCTHING_USER  
CMD ["-home", "/config", "-gui-address", "0.0.0.0:8384"]  
ENTRYPOINT ["/app/syncthing"]  

