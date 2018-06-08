FROM alpine:3.6  
MAINTAINER THRON Devops <devops@thron.com>  
  
ENV TERM=xterm \  
MONGODB_MMS_MONITORING_ARCH=x86_64 \  
MONGODB_MMS_MONITORING_VERSION=6.1.0.387-1 \  
MONGODB_MMS_BACKUP_BASEURL=https://api-agents.mongodb.com \  
SITENAME=NOSITE  
  
RUN apk \--update add ca-certificates wget cyrus-sasl-dev libintl &&\  
apk add \--virtual build_deps gettext &&\  
apk add dos2unix \--update-cache \--repository
http://dl-3.alpinelinux.org/alpine/edge/community/ \--allow-untrusted &&\  
cp /usr/bin/envsubst /usr/local/bin/envsubst &&\  
mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2
&& ln -s /usr/lib/libsasl2.so.3 /usr/lib/libsasl2.so.2 &&\  
mkdir -p /opt /etc/mongodb-mms &&\  
wget \--no-check-certificate -O /opt/mongodb-mms-monitoring-agent-
latest.linux_${MONGODB_MMS_MONITORING_ARCH}.tar.gz
https://cloud.mongodb.com/download/agent/monitoring/mongodb-mms-monitoring-
agent-${MONGODB_MMS_MONITORING_VERSION}.linux_${MONGODB_MMS_MONITORING_ARCH}.tar.gz
&&\  
tar zxvf /opt/mongodb-mms-monitoring-agent-
latest.linux_${MONGODB_MMS_MONITORING_ARCH}.tar.gz -C /opt/ &&\  
ln /opt/mongodb-mms-monitoring-
agent-*.linux_${MONGODB_MMS_MONITORING_ARCH}/mongodb-mms-monitoring-agent
/usr/bin/mongodb-mms-monitoring-agent &&\  
rm /opt/mongodb-mms-monitoring-agent-
latest.linux_${MONGODB_MMS_MONITORING_ARCH}.tar.gz &&\  
rm -rf /var/cache/apk/* &&\  
apk del build_deps  
  
COPY files/ /  
  
RUN dos2unix /etc/docker/start && chmod +x /etc/docker/*  
  
CMD ["/etc/docker/start"]

