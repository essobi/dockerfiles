FROM rawmind/alpine-monit:0.5.20-4  
MAINTAINER Raul Sanchez <rawmind@gmail.com>  
  
# Set environment  
ENV SERVICE_NAME=mesos-dns \  
SERVICE_HOME=/opt/mesos-dns \  
SERVICE_VERSION=v0.6.0 \  
SERVICE_USER=mesos \  
SERVICE_UID=10010 \  
SERVICE_GROUP=mesos \  
SERVICE_GID=10010 \  
SERVICE_URL=github.com/mesosphere/mesos-dns \  
GOROOT=/usr/lib/go \  
GOPATH=/opt/src  
ENV PATH=${PATH}:${SERVICE_HOME}/bin  
  
# Download and install mesos-dns  
RUN mkdir -p ${SERVICE_HOME}/bin ${SERVICE_HOME}/etc ${SERVICE_HOME}/log && \  
apk add --no-cache libcap go make git musl-dev iproute2 && \  
mkdir -p /opt/src; cd /opt/src && \  
go get ${SERVICE_URL} && \  
cd ${GOPATH}/src/${SERVICE_URL} && \  
git checkout ${SERVICE_VERSION} && \  
go build && \  
mv mesos-dns ${SERVICE_HOME}/bin/ && \  
cd ${SERVICE_HOME} && \  
chmod +x ${SERVICE_HOME}/bin/mesos-dns && \  
addgroup -g ${SERVICE_GID} ${SERVICE_GROUP} && \  
adduser -g "${SERVICE_NAME} user" -D -h ${SERVICE_HOME} -G ${SERVICE_GROUP} -s
/sbin/nologin -u ${SERVICE_UID} ${SERVICE_USER} && \  
apk del --no-cache go git gcc musl-dev make openssl-dev && \  
rm -rf /var/cache/apk/* /opt/src ${SERVICE_VOLUME}/*  
ADD root /  
RUN chmod +x ${SERVICE_HOME}/bin/*.sh && \  
chown -R ${SERVICE_USER}:${SERVICE_GROUP} ${SERVICE_HOME} /opt/monit && \  
setcap \  
'cap_net_bind_service=+ep' ${SERVICE_HOME}/bin/mesos-dns \  
'cap_net_admin=+ep' /sbin/ip  
  
EXPOSE 53  
USER ${SERVICE_USER}  
WORKDIR ${SERVICE_HOME}  
  

