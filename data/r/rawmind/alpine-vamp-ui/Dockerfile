FROM rawmind/alpine-nginx:1.10.2-1  
MAINTAINER Raul Sanchez <rawmind@gmail.com>  
  
ENV SERVICE_NAME=vamp-ui \  
SERVICE_VERSION=0.9.2 \  
SERVICE_REPO=https://github.com/magneticio/vamp-ui.git \  
SERVICE_SRC=/opt/src/vamp-ui \  
SERVICE_WWW=/opt/nginx/www \  
SERVICE_USER=vamp \  
SERVICE_UID=10006 \  
SERVICE_GROUP=vamp \  
SERVICE_GID=10006  
# Compile and install vamp-ui  
RUN apk add --update nodejs git python make gcc g++ \  
&& mkdir -p /opt/src; cd /opt/src \  
&& git clone -b "$SERVICE_VERSION" ${SERVICE_REPO} \  
&& cd ${SERVICE_SRC} \  
&& npm install bower \  
&& npm install gulp \  
&& npm install \  
&& ./node_modules/.bin/bower --allow-root install \  
&& ./environment.sh \  
&& ./node_modules/.bin/gulp build \  
&& cd / && cp -rp ${SERVICE_SRC}/dist/* ${SERVICE_WWW} \  
&& apk del nodejs git python make gcc g++ \  
&& rm -rf /var/cache/apk/* /opt/src \  
&& addgroup -g ${SERVICE_GID} ${SERVICE_GROUP} \  
&& adduser -g "${SERVICE_NAME} user" -D -h ${SERVICE_HOME} -G ${SERVICE_GROUP}
-s /sbin/nologin -u ${SERVICE_UID} ${SERVICE_USER}  
  
# Adding files  
ADD root /  
RUN chown -R ${SERVICE_USER}:${SERVICE_GROUP} ${SERVICE_HOME} /opt/monit  
  
USER $SERVICE_USER  
WORKDIR $SERVICE_HOME  
  

