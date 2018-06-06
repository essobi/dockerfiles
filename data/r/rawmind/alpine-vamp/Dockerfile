FROM rawmind/alpine-jvm8:1.8.112  
MAINTAINER Raul Sanchez <rawmind@gmail.com>  
  
#Set environment  
ENV SERVICE_NAME=vamp \  
SERVICE_VERSION=0.9.2 \  
SERVICE_REPO=https://dl.bintray.com/magnetic-io/downloads \  
SERVICE_REPO_UI=https://github.com/magneticio/vamp-ui.git \  
SERVICE_HOME=/opt/vamp \  
SERVICE_SRC=/opt/src/vamp-ui \  
SERVICE_USER=vamp \  
SERVICE_UID=10006 \  
SERVICE_GROUP=vamp \  
SERVICE_GID=10006  
ENV SERVICE_RELEASE=vamp-${SERVICE_VERSION}.jar  
  
RUN mkdir -p ${SERVICE_HOME}/logs ${SERVICE_HOME}/conf ${SERVICE_HOME}/jar
${SERVICE_HOME}/ui && cd ${SERVICE_HOME}/jar \  
&& wget ${SERVICE_REPO}/${SERVICE_RELEASE} \  
&& apk add --update nodejs git python make gcc g++ \  
&& mkdir -p /opt/src; cd /opt/src \  
&& git clone -b "$SERVICE_VERSION" ${SERVICE_REPO_UI} \  
&& cd ${SERVICE_SRC} \  
&& npm install bower \  
&& npm install gulp \  
&& npm install \  
&& ./node_modules/.bin/bower --allow-root install \  
&& ./environment.sh \  
&& ./node_modules/.bin/gulp build \  
&& cp -rp ${SERVICE_SRC}/dist/* ${SERVICE_HOME}/ui \  
&& apk del nodejs git python make gcc g++ \  
&& cd / && rm -rf /var/cache/apk/* /opt/src \  
&& addgroup -g ${SERVICE_GID} ${SERVICE_GROUP} \  
&& adduser -g "${SERVICE_NAME} user" -D -h ${SERVICE_HOME} -G ${SERVICE_GROUP}
-s /sbin/nologin -u ${SERVICE_UID} ${SERVICE_USER}  
  
# Adding files  
ADD root /  
RUN chmod +x ${SERVICE_HOME}/bin/*.sh \  
&& chown -R ${SERVICE_USER}:${SERVICE_GROUP} ${SERVICE_HOME} /opt/monit  
  
USER $SERVICE_USER  
WORKDIR $SERVICE_HOME  
  
EXPOSE 8080

