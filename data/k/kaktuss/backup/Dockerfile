FROM alpine:3.6  
ENV CONSUL_TEMPLATE_VERSION=0.18.5  
ENV
CONSUL_TEMPLATE_SHA256=b0cd6e821d6150c9a0166681072c12e906ed549ef4588f73ed58c9d834295cd2  
  
RUN \  
apk add --no-cache --virtual .build-deps \  
curl \  
unzip \  
  
&& apk add \--no-cache \  
busybox-suid \  
duplicity \  
openssh-client \  
rsync \  
su-exec \  
tzdata \  
  
&& cd /usr/local/bin \  
&& curl -L https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip -o consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
&& echo -n "$CONSUL_TEMPLATE_SHA256 consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip" | sha256sum -c - \  
&& unzip consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
&& rm consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
  
&& apk del .build-deps  
  
ENV BACKUP_SOURCE=  
  
ENV BACKUP_TARGET_USER=  
ENV BACKUP_TARGET_HOST=  
ENV BACKUP_TARGET_MODULE=  
ENV BACKUP_TARGET_PATH=  
ENV BACKUP_TARGET_MODE=daemon  
  
ENV BACKUP_MODE=  
ENV BACKUP_HOUR=0  
ENV BACKUP_MINUTE=0  
ENV BACKUP_IS_RANDOM_DELAY=  
  
ENV SET_CONTAINER_TIMEZONE=true  
ENV CONTAINER_TIMEZONE=Europe/Moscow  
  
ENV BACKUP_USER_ROOT=  
ENV USER_UID=1000  
ENV USER_GID=1000  
COPY templates /etc/backup/templates  
COPY backup.sh /usr/local/bin/backup.sh  
COPY start.sh /usr/local/bin/start.sh  
  
CMD ["/usr/local/bin/start.sh"]  

