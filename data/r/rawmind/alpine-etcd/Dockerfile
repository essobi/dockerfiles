FROM rawmind/alpine-monit:0.5.20-2  
MAINTAINER Raul Sanchez <rawmind@gmail.com>  
  
  
ENV SERVICE_NAME=etcd \  
SERVICE_HOME=/opt/etcd \  
SERVICE_CONF=/opt/etcd/etc/etcd-source \  
SERVICE_VERSION=2.3.7 \  
SERVICE_USER=etcd \  
SERVICE_UID=10005 \  
SERVICE_GROUP=etcd \  
SERVICE_GID=10005  
ENV PATH=${SERVICE_HOME}/bin:${PATH} \  
SERVICE_URL=https://github.com/coreos/etcd/releases/download/v${SERVICE_VERSION}
\  
SERVICE_RELEASE=etcd-v${SERVICE_VERSION}-linux-amd64  
  
RUN mkdir -p ${SERVICE_HOME}/data ${SERVICE_HOME}/logs ${SERVICE_HOME}/etc &&
\  
curl -jksSL ${SERVICE_URL}/${SERVICE_RELEASE}.tar.gz | gunzip -c - | tar -xf -
-C /opt && \  
mv /opt/${SERVICE_RELEASE} ${SERVICE_HOME}/bin && \  
chmod +x ${SERVICE_HOME}/bin/etcd* && \  
addgroup -g ${SERVICE_GID} ${SERVICE_GROUP} && \  
adduser -g "${SERVICE_NAME} user" -D -h ${SERVICE_HOME} -G ${SERVICE_GROUP} -s
/sbin/nologin -u ${SERVICE_UID} ${SERVICE_USER}  
  
ADD root /  
RUN chmod +x ${SERVICE_HOME}/bin/*.sh \  
&& chown -R ${SERVICE_USER}:${SERVICE_GROUP} ${SERVICE_HOME} /opt/monit  
  
USER $SERVICE_USER  
WORKDIR $SERVICE_HOME  
  
EXPOSE 2379 2380  

