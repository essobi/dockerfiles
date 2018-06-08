FROM node:8-alpine  
MAINTAINER STARTX "dev@startx.fr"  
  
ENV SQLUP_VERSION=0.1.0 \  
SX_ID="startx/sqlup" \  
SX_NAME="Startx SQLUP (alpine)" \  
SX_SUMMARY="open-source job container to apply sql patch to a database
following a sequentially versionned plan" \  
DESCRIPTION="SQLUP $SQLUP_VERSION will help you create, initialize and apply
an update strategy to your database containers" \  
SX_DEBUG=true \  
NODE_ENV=development \  
APP_PATH=/usr/src/app \  
CONF_PATH=/sqlup \  
DATA_PATH=/sqlup \  
APP_MAIN=/usr/src/app/app.js  
  
LABEL name="startx/sqlup-$SQLUP_VERSION" \  
summary="$SX_SUMMARY" \  
description="$DESCRIPTION." \  
version="$SQLUP_VERSION" \  
release="1" \  
maintainer="Startx <dev@startx.fr>" \  
help="For more information visit https://github.com/startxfr/sqlup" \  
io.k8s.description="$DESCRIPTION" \  
io.k8s.display-name="$SX_NAME" \  
io.openshift.tags="startx,nodejs,sqlup,sqlup-$SQLUP_VERSION" \  
io.openshift.non-scalable="false" \  
io.openshift.min-memory="100Mi" \  
io.openshift.min-cpu="1000m" \  
io.openshift.s2i.destination="/tmp" \  
io.openshift.s2i.scripts-url="image:///s2i" \  
fr.startx.component="$SX_ID:$SQLUP_VERSION"  
  
COPY ./s2i /s2i  
COPY ./core $APP_PATH/core  
COPY ./test $APP_PATH/test  
COPY ./app.js $APP_PATH/app.js  
COPY ./package.json $APP_PATH/package.json  
  
RUN apk update && apk upgrade \  
&& mkdir -p $APP_PATH $CONF_PATH $DATA_PATH /.npm /.config \  
&& cd $APP_PATH \  
&& npm install \  
&& npm dedupe \  
&& npm cache verify \  
&& npm cache clean --force \  
&& chgrp -R 0 $APP_PATH $CONF_PATH $DATA_PATH /s2i /.npm /.config \  
&& chown -R 1001:0 $APP_PATH $CONF_PATH $DATA_PATH /s2i /.npm /.config \  
&& chmod -R g=u $APP_PATH $CONF_PATH $DATA_PATH /s2i /.npm /.config  
  
USER 1001  
WORKDIR $APP_PATH  
CMD [ "npm" , "start" ]  

