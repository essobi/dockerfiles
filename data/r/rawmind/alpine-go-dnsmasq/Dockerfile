FROM rawmind/alpine-monit:0.5.19-2  
MAINTAINER Raul Sanchez <rawmind@gmail.com>  
  
ENV SERVICE_NAME=go-dnsmasq \  
SERVICE_HOME=/opt/go-dnsmasq \  
SERVICE_VERSION=1.0.6 \  
SERVICE_USER=go-dnsmasq \  
SERVICE_UID=10009 \  
SERVICE_GROUP=go-dnsmasq \  
SERVICE_GID=10009 \  
GOMAXPROCS=2 \  
GOROOT=/usr/lib/go \  
GOPATH=/opt/src \  
GOBIN=/gopath/bin  
ENV PATH=${SERVICE_HOME}/bin:${PATH} \  
SERVICE_CONF=${SERVICE_HOME}/etc/go-dnsmasq-source \  
SERVICE_URL=https://github.com/janeczku/go-
dnsmasq/releases/download/${SERVICE_VERSION}/ \  
SERVICE_RELEASE=go-dnsmasq_linux-amd64  
  
# Install and configure go-dnsmasq  
RUN mkdir -p ${SERVICE_HOME}/bin ${SERVICE_HOME}/log ${SERVICE_HOME}/etc && \  
apk add --no-cache libcap && \  
cd ${SERVICE_HOME}/bin && \  
curl -O -sSL ${SERVICE_URL}/${SERVICE_RELEASE} && \  
curl -O -sSL ${SERVICE_URL}/${SERVICE_RELEASE}.sha256 && \  
sha256sum -c ${SERVICE_RELEASE}.sha256 && \  
mv ${SERVICE_RELEASE} go-dnsmasq && \  
addgroup -g ${SERVICE_GID} ${SERVICE_GROUP} && \  
adduser -g "${SERVICE_NAME} user" -D -h ${SERVICE_HOME} -G ${SERVICE_GROUP} -s
/sbin/nologin -u ${SERVICE_UID} ${SERVICE_USER}  
  
ADD root /  
RUN chmod +x ${SERVICE_HOME}/bin/go-dnsmasq ${SERVICE_HOME}/bin/*.sh && \  
chown -R ${SERVICE_USER}:${SERVICE_GROUP} ${SERVICE_HOME} /opt/monit && \  
setcap 'cap_net_bind_service=+ep' ${SERVICE_HOME}/bin/go-dnsmasq  
  
USER $SERVICE_USER  
WORKDIR $SERVICE_HOME  
  
EXPOSE 53

