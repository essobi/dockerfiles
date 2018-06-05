FROM openjdk:8u111-jre-alpine  
MAINTAINER pogoprzem@gmail.com  
  
ARG APP_VERSION=2017.4  
ARG APP_BUILD=38030  
ENV APP_SRC_NAME="youtrack-${APP_VERSION}.${APP_BUILD}" \  
APP_DEST_NAME=youtrack \  
WORK_DIR=/usr/local/jetbrains  
  
ENV APP_SRC_FILE="${APP_SRC_NAME}.zip" \  
APP_DIR=${WORK_DIR}/${APP_DEST_NAME}  
  
ENV APP_BASE_URL=http://localhost/ \  
APP_LISTEN_PORT=80 \  
APP_BACKUPS_DIR="${APP_DIR}/backups" \  
APP_DATA_DIR="${APP_DIR}/data" \  
APP_LOGS_DIR="${APP_DIR}/logs" \  
APP_TEMP_DIR="${APP_DIR}/temp"  
WORKDIR $WORK_DIR  
  
RUN apk add --no-cache --virtual .build-deps wget unzip && \  
wget -q https://download.jetbrains.com/charisma/$APP_SRC_FILE && \  
unzip -q $APP_SRC_FILE -x */internal/java/* && \  
mv $APP_SRC_NAME $APP_DEST_NAME && \  
rm $APP_SRC_FILE && \  
apk del .build-deps  
  
WORKDIR $APP_DIR  
  
RUN bin/youtrack.sh configure \  
\--base-url $APP_BASE_URL \  
\--listen-port $APP_LISTEN_PORT \  
\--backups-dir $APP_BACKUPS_DIR \  
\--data-dir $APP_DATA_DIR \  
\--logs-dir $APP_LOGS_DIR \  
\--temp-dir $APP_TEMP_DIR  
  
EXPOSE $APP_LISTEN_PORT  
  
VOLUME ["$APP_BACKUPS_DIR", "$APP_DATA_DIR", "$APP_LOGS_DIR"]  
  
ENTRYPOINT ["bin/youtrack.sh"]  
CMD ["run"]  

