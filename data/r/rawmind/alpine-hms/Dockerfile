FROM rawmind/alpine-nginx:1.11.9-1  
MAINTAINER Raul Sanchez <rawmind@gmail.com>  
  
# Set environment  
ENV SERVICE_NAME=hms \  
SERVICE_HOME=/opt/nginx \  
REVEAL_VERSION=3.4.1 \  
REVEAL_URL=https://github.com/hakimel/reveal.js.git \  
SERVICE_USER=nginx \  
SERVICE_UID=10004 \  
SERVICE_GROUP=nginx \  
SERVICE_GID=10004 \  
SERVICE_URL=https://github.com/4km3/hms.git  
  
# Download and install hms  
RUN apk add --no-cache git && \  
cd ${SERVICE_HOME}/www && \  
git clone ${SERVICE_URL} && \  
cd hms/docs && \  
git clone -b ${REVEAL_VERSION} ${REVEAL_URL} && \  
rm -rf reveal.js/test && \  
apk del --no-cache git && \  
addgroup -g ${SERVICE_GID} ${SERVICE_GROUP} && \  
adduser -g "${SERVICE_NAME} user" -D -h ${SERVICE_HOME} -G ${SERVICE_GROUP} -s
/sbin/nologin -u ${SERVICE_UID} ${SERVICE_USER}  
ADD root /  
RUN chmod +x ${SERVICE_HOME}/bin/*.sh && \  
chown -R ${SERVICE_USER}:${SERVICE_GROUP} ${SERVICE_HOME} /opt/monit  
  
USER $SERVICE_USER  
WORKDIR $SERVICE_HOME  
  

