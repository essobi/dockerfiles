FROM rawmind/alpine-base:3.5-1  
MAINTAINER Raul Sanchez <rawmind@gmail.com>  
  
#Set environment  
ENV SERVICE_NAME=rancher-catalog-stats \  
SERVICE_HOME=/opt/rancher-catalog-stats \  
SERVICE_USER=rancher \  
SERVICE_UID=10012 \  
SERVICE_GROUP=rancher \  
SERVICE_GID=10012 \  
GOMAXPROCS=2 \  
GOROOT=/usr/lib/go \  
GOPATH=/opt/src \  
GOBIN=/gopath/bin  
ENV PATH=${PATH}:${SERVICE_HOME}  
  
# Add files  
ADD src /opt/src/  
RUN apk add --no-cache git mercurial bzr make go musl-dev && \  
cd /opt/src && \  
go get && \  
go build -o ${SERVICE_NAME} && \  
mkdir ${SERVICE_HOME} && \  
mv ${SERVICE_NAME} ${SERVICE_HOME}/ && \  
cd ${SERVICE_HOME} && \  
curl -sS
http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.tar.gz |
gunzip -c - | tar -xf - && \  
mv GeoLite2-City_*/GeoLite2-City.mmdb . && \  
rm -rf /opt/src GeoLite2-City_* && \  
apk del --no-cache git mercurial bzr make go musl-dev && \  
addgroup -g ${SERVICE_GID} ${SERVICE_GROUP} && \  
adduser -g "${SERVICE_NAME} user" -D -h ${SERVICE_HOME} -G ${SERVICE_GROUP} -s
/sbin/nologin -u ${SERVICE_UID} ${SERVICE_USER}  
  
USER $SERVICE_USER  
WORKDIR $SERVICE_HOME  

