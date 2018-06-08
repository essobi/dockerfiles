FROM rawmind/alpine-monit:0.5.20-2  
MAINTAINER Raul Sanchez <rawmind@gmail.com>  
  
ENV SERVICE_NAME=skydns \  
SERVICE_HOME=/opt/skydns \  
SERVICE_CONF=/opt/skydns/etc/skydns-source \  
SERVICE_VERSION=2.5.3a \  
SERVICE_USER=skydns \  
SERVICE_UID=10006 \  
SERVICE_GROUP=skydns \  
SERVICE_GID=10006 \  
GOMAXPROCS=2 \  
GOROOT=/usr/lib/go \  
GOPATH=/opt/src \  
GOBIN=/gopath/bin \  
PATH=/opt/skydns/bin:${PATH} \  
SERVICE_URL=github.com/skynetservices/skydns  
  
RUN mkdir -p ${SERVICE_HOME}/bin ${SERVICE_HOME}/logs ${SERVICE_HOME}/etc && \  
apk --update add bind-tools && \  
apk add go git gcc musl-dev && \  
mkdir -p ${GOPATH}; cd ${GOPATH} && \  
go get ${SERVICE_URL} && \  
cd ${GOPATH}/src/github.com/skynetservices/skydns && \  
CGO_ENABLED=0 go build -v -installsuffix cgo -ldflags '-extld ld -extldflags
-static' -a -x . && \  
mv skydns ${SERVICE_HOME}/bin/ && \  
chmod +x ${SERVICE_HOME}/bin/skydns && \  
apk del go git gcc musl-dev && \  
rm -rf /var/cache/apk/* /opt/src && \  
chmod +x ${SERVICE_HOME}/bin/skydns && \  
addgroup -g ${SERVICE_GID} ${SERVICE_GROUP} && \  
adduser -g "${SERVICE_NAME} user" -D -h ${SERVICE_HOME} -G ${SERVICE_GROUP} -s
/sbin/nologin -u ${SERVICE_UID} ${SERVICE_USER}  
  
ADD root /  
RUN chmod +x ${SERVICE_HOME}/bin/*.sh && \  
chown -R ${SERVICE_USER}:${SERVICE_GROUP} ${SERVICE_HOME} /opt/monit && \  
setcap 'cap_net_bind_service=+ep' ${SERVICE_HOME}/bin/skydns  
  
USER $SERVICE_USER  
WORKDIR $SERVICE_HOME  
  
EXPOSE 53  

