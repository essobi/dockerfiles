FROM rawmind/alpine-monit:0.5.20-2  
MAINTAINER Raul Sanchez <rawmind@gmail.com>  
  
ENV HAPROXY_HOME /opt/haproxy  
ENV PATH=$PATH:${HAPROXY_HOME}/bin  
  
ENV SERVICE_NAME=haproxy \  
SERVICE_HOME=/opt/haproxy \  
SERVICE_VERSION=1.6.10 \  
SERVICE_URL=http://www.haproxy.org/download/1.6/src \  
SERVICE_USER=haproxy \  
SERVICE_UID=10007 \  
SERVICE_GROUP=haproxy \  
SERVICE_GID=10007 \  
SERVICE_VOLUME=/opt/tools  
ENV PATH=${SERVICE_HOME}/bin:${PATH} \  
SERVICE_CONF=${SERVICE_HOME}/etc/haproxy.cfg \  
SERVICE_RELEASE=haproxy-${SERVICE_VERSION}  
  
  
  
  
# Build and install haproxy  
RUN set -ex && \  
apk --update add libnl3-cli musl-dev linux-headers gcc pcre-dev make zlib-dev
openssl-dev && \  
mkdir -p /opt/src ${SERVICE_HOME}/etc/ssl ${SERVICE_HOME}/bin && \  
curl -fL ${SERVICE_URL}/${SERVICE_RELEASE}.tar.gz | tar xzf - -C /opt/src && \  
cd /opt/src/${SERVICE_RELEASE} && \  
make TARGET=linux2628 USE_PCRE=1 USE_ZLIB=1 USE_OPENSSL=1 && \  
cp -p haproxy ${SERVICE_HOME}/bin && \  
cd ${SERVICE_HOME} && \  
rm -rf /opt/src && \  
apk del musl-dev linux-headers gcc pcre-dev make zlib-dev openssl-dev && \  
apk add musl pcre zlib && rm /var/cache/apk/* && \  
addgroup -g ${SERVICE_GID} ${SERVICE_GROUP} && \  
adduser -g "${SERVICE_NAME} user" -D -h ${SERVICE_HOME} -G ${SERVICE_GROUP} -s
/sbin/nologin -u ${SERVICE_UID} ${SERVICE_USER}  
  
ADD root /  
RUN chmod +x ${SERVICE_HOME}/bin/*.sh \  
&& chown -R ${SERVICE_USER}:${SERVICE_GROUP} ${SERVICE_HOME} /opt/monit  
  
USER $SERVICE_USER  
WORKDIR $SERVICE_HOME  
  
EXPOSE 8000 8080 8443

