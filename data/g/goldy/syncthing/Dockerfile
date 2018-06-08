FROM alpine:3.4  
ENV GOROOT=/usr/lib/go \  
GOPATH=/go \  
PATH=$PATH:$GOROOT/bin:$GOPATH/bin \  
UID=1000 \  
GID=1000 \  
HOME=/var/syncthing/  
  
RUN apk add --no-cache libxml2 libxslt && \  
apk add --no-cache --virtual .build-dependencies curl jq git go ca-
certificates && \  
addgroup -g ${GID} syncthing && \  
adduser -D -u ${UID} -h ${HOME} -G syncthing syncthing && \  
  
# compile syncthing  
mkdir -p /go/src/github.com/syncthing && \  
cd /go/src/github.com/syncthing && \  
git clone https://github.com/syncthing/syncthing.git && \  
cd syncthing && \  
git checkout $(git tag -l --sort=-v:refname | head -n 1) && \  
(go run build.go || (git reset --hard master && go run build.go)) && \  
mkdir -p /go/bin && \  
mv bin/syncthing /usr/local/bin/syncthing && \  
chown syncthing:syncthing /usr/local/bin/syncthing && \  
  
# cleanup  
rm -rf /go/pkg && \  
rm -rf /go/src && \  
apk del .build-dependencies  
  
RUN apk add --no-cache python3 && \  
python3 -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
pip3 install --upgrade pip setuptools && \  
pip3 install pyentrypoint==0.5.0  
  
ADD entrypoint-config.yml /etc/entrypoint-config.yml  
ENV ENTRYPOINT_CONFIG /etc/entrypoint-config.yml  
  
WORKDIR /var/syncthing  
  
VOLUME ["/var/syncthing/.config/syncthing", "/var/syncthing/Sync"]  
  
EXPOSE 8384 22000 21027/udp  
  
ENTRYPOINT ["pyentrypoint"]  
  
CMD ["syncthing", "-gui-address=0.0.0.0:8384"]  

