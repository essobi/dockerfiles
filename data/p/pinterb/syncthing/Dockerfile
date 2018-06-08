FROM pinterb/base:alpine  
  
MAINTAINER Brad Pinter <brad.pinter@gmail.com>  
  
LABEL vendor="Syncthing" \  
net.syncthing.version="0.14.7" \  
net.syncthing.release-date="2016-09-21"  
  
ENV SYNCTHING_VERSION 0.14.7  
ENV GLIBC_PKG_VERSION 2.23-r3  
ENV PUID 1000  
ENV PGID 1000  
RUN apk add --no-cache --update-cache ca-certificates bash sudo graphviz && \  
curl -Lo /etc/apk/keys/sgerrand.rsa.pub "https://github.com/sgerrand/alpine-
pkg-glibc/releases/download/${GLIBC_PKG_VERSION}/sgerrand.rsa.pub" && \  
curl -Lo glibc-${GLIBC_PKG_VERSION}.apk "https://github.com/sgerrand/alpine-
pkg-
glibc/releases/download/${GLIBC_PKG_VERSION}/glibc-${GLIBC_PKG_VERSION}.apk"
&& \  
curl -Lo glibc-bin-${GLIBC_PKG_VERSION}.apk
"https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_PKG_VERSION}/glibc-
bin-${GLIBC_PKG_VERSION}.apk" && \  
curl -Lo glibc-i18n-${GLIBC_PKG_VERSION}.apk
"https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_PKG_VERSION}/glibc-i18n-${GLIBC_PKG_VERSION}.apk"
&& \  
apk add glibc-${GLIBC_PKG_VERSION}.apk glibc-bin-${GLIBC_PKG_VERSION}.apk
glibc-i18n-${GLIBC_PKG_VERSION}.apk && \  
curl -Lo /syncthing.tar.gz
"https://github.com/syncthing/syncthing/releases/download/v${SYNCTHING_VERSION}/syncthing-
linux-amd64-v${SYNCTHING_VERSION}.tar.gz" && \  
gunzip /syncthing.tar.gz && tar -xvf /syncthing.tar && \  
mv /syncthing-linux-amd64-v${SYNCTHING_VERSION}/syncthing /bin/syncthing && \  
rm -rf /syncthing-linux-amd64-v${SYNCTHING_VERSION} && \  
rm -rf /syncthing.tar && \  
apk del --purge curl ca-certificates && \  
rm -rf /var/cache/apk/*  
  
# create dev user  
RUN addgroup -g $PGID dev && \  
adduser -h /home/dev -u $PUID -D -G dev -s /bin/bash dev && \  
sed -ri 's/(wheel:x:10:root)/\1,dev/' /etc/group && \  
sed -ri 's/# %wheel ALL=\\(ALL\\) NOPASSWD: ALL/%wheel ALL=\\(ALL\\) NOPASSWD:
ALL/' /etc/sudoers  
  
COPY node_id /bin/node_id  
  
# Create a shared data volume  
# We need to create an empty file, otherwise the volume will  
# belong to root.  
RUN mkdir /data/ /ops/ /state/ /config/  
RUN touch /data/.extra /ops/.extra /state/.extra /config/.extra  
RUN chown -R dev:dev /data && \  
chown -R dev:dev /ops && \  
chown -R dev:dev /state && \  
chown -R dev:dev /config  
  
VOLUME ["/data", "/ops", "/state", "/config"]  
EXPOSE 8080 8384 22000  
WORKDIR /config  
  
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["-version"]  

