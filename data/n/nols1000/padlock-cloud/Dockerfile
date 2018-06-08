FROM golang:alpine  
  
ARG WORKDIR=/opt/padlock-cloud  
  
ENV PC_CONFIG_PATH= \  
PC_LOG_FILE=${WORKDIR}/logs/info.log \  
PC_ERR_FILE=${WORKDIR}/logs/error.log \  
PC_NOTIFY_ERRORS= \  
PC_LEVELDB_PATH=${WORKDIR}/db \  
PC_EMAIL_SERVER= \  
PC_EMAIL_PORT= \  
PC_EMAIL_USER= \  
PC_EMAIL_PASSWORD= \  
PC_EMAIL_FROM= \  
PC_WHITELIST_PATH= \  
PC_PORT=8080 \  
PC_ASSETS_PATH=${WORKDIR}/assets \  
PC_TLS_CERT= \  
PC_TLS_KEY= \  
PC_BASE_URL=http://localhost:8080 \  
PC_CORS=1 \  
PC_TEST=0  
  
RUN addgroup -g 1000 -S padlock-cloud &&\  
adduser -u 1000 -D -S -G padlock-cloud padlock-cloud  
  
RUN mkdir -p ${WORKDIR} && mkdir -p ${WORKDIR}/db && \  
mkdir -p ${WORKDIR}/logs && mkdir -p ${WORKDIR}/ssl && \  
touch ${WORKDIR}/logs/info.log && \  
touch ${WORKDIR}/logs/error.log  
  
WORKDIR ${WORKDIR}  
  
RUN apk --update --no-cache add git su-exec && \  
go get github.com/maklesoft/padlock-cloud && \  
apk del git  
  
COPY . ${WORKDIR}  
  
VOLUME ["$WORKDIR/assets", "$WORKDIR/db", "$WORKDIR/logs", "$WORKDIR/ssl"]  
  
ENTRYPOINT ["/bin/sh", "./docker-entrypoint.sh"]  
  
EXPOSE 8080 8443  
CMD ["padlock-cloud", "runserver"]

