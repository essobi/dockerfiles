FROM rawmind/alpine-monit:0.5.19-2  
MAINTAINER Raul Sanchez <rawmind@gmail.com>  
  
ENV SERVICE_NAME=postgres \  
SERVICE_HOME=/opt/pgsql \  
SERVICE_VERSION=9.5.5 \  
SERVICE_USER=postgres \  
SERVICE_UID=10008 \  
SERVICE_GROUP=postgres \  
SERVICE_GID=10008 \  
SERVICE_VOLUME=/opt/tools  
ENV PATH=${SERVICE_HOME}/bin:${PATH} \  
LANG=en_US.utf8 \  
SERVICE_CONF=${SERVICE_HOME}/etc/haproxy.cfg \  
SERVICE_URL=ftp://ftp.postgresql.org/pub/source/v${SERVICE_VERSION} \  
SERVICE_RELEASE=postgresql-${SERVICE_VERSION} \  
BUILD_OPTS="--enable-integer-datetimes --enable-thread-safety
--prefix=${SERVICE_HOME} --with-openssl" \  
PKGS="build-base readline-dev openssl-dev zlib-dev libxml2-dev glib-lang"  
RUN apk add --no-cache ${PKGS} && \  
mkdir -p /opt/src ${SERVICE_HOME}/log; cd /opt/src && \  
curl -O -sSL ${SERVICE_URL}/${SERVICE_RELEASE}.tar.bz2 && \  
curl -O -sSL ${SERVICE_URL}/${SERVICE_RELEASE}.tar.bz2.sha256 && \  
sha256sum -c ${SERVICE_RELEASE}.tar.bz2.sha256 && \  
tar -xjf ${SERVICE_RELEASE}.tar.bz2 && \  
cd ${SERVICE_RELEASE} && \  
./configure ${BUILD_OPTS} && \  
make -j2 && \  
make install && \  
apk del ${PKGS} && \  
rm -rf /opt/src/* \  
/tmp/* \  
/var/cache/apk/* && \  
deluser ${SERVICE_USER} && \  
addgroup -g ${SERVICE_GID} ${SERVICE_GROUP} && \  
adduser -g "${SERVICE_NAME} user" -D -h ${SERVICE_HOME} -G ${SERVICE_GROUP} -s
/sbin/nologin -u ${SERVICE_UID} ${SERVICE_USER}  
ADD root /  
RUN chmod +x ${SERVICE_HOME}/bin/*.sh && \  
chown -R ${SERVICE_USER}:${SERVICE_GROUP} ${SERVICE_HOME} /opt/monit  
  
USER $SERVICE_USER  
WORKDIR $SERVICE_HOME  
  
EXPOSE 5432

