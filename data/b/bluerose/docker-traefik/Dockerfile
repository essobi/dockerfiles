FROM traefik:1.5-alpine  
  
ADD ./env_secrets_expand.sh /usr/local/bin/env_secrets_expand.sh  
  
# install s3cmd, cron and supervisord  
ENV S3CMD_VERSION 1.6.1  
ENV SUPERVISOR_VERSION=3.3.1  
ENV DOCKERIZE_VERSION v0.6.0  
RUN apk update && \  
apk add --no-cache py-pip py-setuptools ca-certificates openssl dcron && \  
update-ca-certificates && \  
wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz && \  
tar -C /usr/local/bin -xzvf dockerize-alpine-linux-
amd64-$DOCKERIZE_VERSION.tar.gz && \  
rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz && \  
pip install python-magic && \  
pip install supervisor==$SUPERVISOR_VERSION && \  
cd /tmp && \  
wget
https://github.com/s3tools/s3cmd/releases/download/v${S3CMD_VERSION}/s3cmd-${S3CMD_VERSION}.tar.gz
&& \  
tar xzf s3cmd-${S3CMD_VERSION}.tar.gz && \  
cd s3cmd-${S3CMD_VERSION} && \  
python setup.py install && \  
rm -rf /var/cache/apk/* /tmp/s3cmd-${S3CMD_VERSION}
/tmp/s3cmd-${S3CMD_VERSION}.tar.gz && \  
mkdir -p /var/log/supervisord && \  
rm /entrypoint.sh && \  
mkdir -p /etc/cron.d  
  
ADD ./supervisord.conf /etc/supervisord.conf  
  
ADD ./entrypoint.sh /entrypoint.sh  
ADD ./.s3cfg.tmpl /root/.s3cfg.tmpl  
ADD ./backup.sh /usr/local/bin/backup.sh  
ADD ./restore.sh /usr/local/bin/restore.sh  
ADD ./shutdown-hook.sh /usr/local/bin/shutdown-hook.sh  
  
ADD traefik.toml.tmpl /etc/traefik/  

