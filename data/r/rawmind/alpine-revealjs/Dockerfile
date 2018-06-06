FROM rawmind/alpine-nginx:1.12.2-0  
MAINTAINER Raul Sanchez <rawmind@gmail.com>  
  
# Set environment  
ENV SERVICE_NAME=reveal.js \  
SERVICE_SITE=${SERVICE_HOME}/www/reveal.js \  
SERVICE_VERSION=3.6.0 \  
SERVICE_URL=https://github.com/hakimel/reveal.js/archive \  
SERVICE_USER=nginx \  
SERVICE_UID=10004 \  
SERVICE_GROUP=nginx \  
SERVICE_GID=10004  
  
# Adding nginx site configuration  
ADD root /  
  
# Download and install reveal.js into /opt/nginx/www/reveal.js  
RUN cd ${SERVICE_HOME}/www && \  
curl -sSL ${SERVICE_URL}/${SERVICE_VERSION}.tar.gz | gunzip -c - | tar -xf -
&& \  
mv reveal.js-${SERVICE_VERSION} reveal.js && \  
rm -rf reveal.js/test reveal.js/.git && \  
mkdir reveal.js/slides && \  
addgroup -g ${SERVICE_GID} ${SERVICE_GROUP} && \  
adduser -g "${SERVICE_NAME} user" -D -h ${SERVICE_HOME} -G ${SERVICE_GROUP} -s
/sbin/nologin -u ${SERVICE_UID} ${SERVICE_USER} && \  
chown -R ${SERVICE_USER}:${SERVICE_GROUP} ${SERVICE_HOME} /opt/monit  
  
EXPOSE 8080  
USER ${SERVICE_USER}  
WORKDIR ${SERVICE_SITE}  

