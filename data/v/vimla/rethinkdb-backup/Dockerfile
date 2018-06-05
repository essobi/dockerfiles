FROM alpine:3.7  
ARG RETHINK_VERSION="2.3.0"  
ARG RETHINK_HOST="localhost"  
ARG RETHINK_PORT="28015"  
ARG PGP_FILE="/run/secrets/pgp-key"  
ARG CRON_TIME="0 4 */2 * *"  
ARG VERSION="0.0.1"  
ENV \  
RETHINK_VERSION=${RETHINK_VERSION} \  
RETHINK_HOST=${RETHINK_HOST} \  
RETHINK_PORT=${RETHINK_PORT} \  
RETHINK_PASSWORD_FILE= \  
RETHINK_EXPORT_ARGS= \  
RETHINK_RESTORE_ARGS= \  
BACKUP_NAME= \  
PGP_FILE=${PGP_FILE} \  
CRON_TIME=${CRON_TIME} \  
AWS_ACCESS_KEY_ID= \  
AWS_SECRET_ACCESS_KEY= \  
AWS_DEFAULT_REGION= \  
S3_BUCKET_URL=  
  
LABEL \  
se.vimla.version=${VERSION} \  
vendor="vimla.se"  
  
RUN \  
apk -Uuv add python2 py2-pip bash gnupg file tar \  
&& pip install "rethinkdb<${RETHINK_VERSION}" awscli \  
&& apk --purge -v del py-pip \  
&& rm /var/cache/apk/*  
  
COPY ./entrypoint.sh /entrypoint.sh  
  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

