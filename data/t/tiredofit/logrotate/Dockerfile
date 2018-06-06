FROM tiredofit/alpine:3.6  
LABEL maintainer="Dave Conroy (dave at tiredofit dot ca)"  
  
ARG LOGROTATE_VERSION=latest  
ARG CONTAINER_UID=1000  
ARG CONTAINER_GID=1000  
# environment variable for this container  
ENV LOGROTATE_OLDDIR= \  
LOGROTATE_COMPRESSION= \  
LOGROTATE_INTERVAL= \  
LOGROTATE_COPIES= \  
LOGROTATE_SIZE= \  
LOGS_DIRECTORIES= \  
LOG_FILE_ENDINGS= \  
LOGROTATE_LOGFILE= \  
LOGROTATE_CRONSCHEDULE= \  
LOGROTATE_PARAMETERS= \  
LOGROTATE_STATUSFILE= \  
LOG_FILE=  
  
  
## Install Development Tools  
RUN adduser -u $CONTAINER_UID -h /usr/bin/logrotate.d -s /bin/bash -S
logrotate && \  
  
apk add \--update \  
tar \  
gzip \  
wget && \  
if [ "${LOGROTATE_VERSION}" = "latest" ]; \  
then apk add logrotate ; \  
else apk add "logrotate=${LOGROTATE_VERSION}" ; \  
fi && \  
  
mkdir -p /usr/bin/logrotate.d && \  
wget --no-check-certificate -O /tmp/go-cron.tar.gz
https://github.com/michaloo/go-cron/releases/download/v0.0.2/go-cron.tar.gz &&
\  
tar xvf /tmp/go-cron.tar.gz -C /usr/bin && \  
apk del \  
wget && \  
rm -rf /var/cache/apk/* && rm -rf /tmp/*  
  
## Add Files  
COPY install/run.sh /usr/bin/logrotate.d/run.sh  
COPY install/update-logrotate.sh /usr/bin/logrotate.d/update-logrotate.sh  
  
## Entrypoint Configuration  
ENTRYPOINT ["/usr/bin/logrotate.d/run.sh"]  
VOLUME ["/logrotate-status"]  
CMD ["cron"]  

