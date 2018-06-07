FROM python:2.7-alpine  
  
ARG
DUPLICITY_URL=https://code.launchpad.net/duplicity/0.7-series/0.7.12/+download/duplicity-0.7.12.tar.gz  
ARG DUPLICITY_CSUM=29519f89f3e80d580c2b91a14be75cd9  
ARG DUPLICITY_BACKUP_VERSION=v1.3.0  
ARG DUPLICITY_BACKUP_CSUM=bc26f071a98048eebae3fea759ae709a  
  
ADD root /  
  
RUN apk -U --no-cache add \  
alpine-sdk \  
ca-certificates \  
coreutils \  
bash \  
gnupg \  
libffi \  
libffi-dev \  
librsync \  
librsync-dev \  
mailx \  
mariadb-client \  
openssl \  
openssl-dev \  
tar \  
tini \  
wget \  
&& wget -O /tmp/duplicity.tgz ${DUPLICITY_URL} \  
&& if [ "$DUPLICITY_CSUM" != "$(md5sum /tmp/duplicity.tgz | awk
'{print($1)}')" ]; then echo "Wrong md5sum of downloaded file!"; exit 1; fi \  
&& wget -O /tmp/duplicity-backup.tgz https://github.com/zertrin/duplicity-
backup.sh/archive/${DUPLICITY_BACKUP_VERSION}.tar.gz \  
&& if [ "$DUPLICITY_BACKUP_CSUM" != "$(md5sum /tmp/duplicity-backup.tgz | awk
'{print($1)}')" ]; then echo "Wrong md5sum of downloaded file!"; exit 1; fi \  
&& mkdir -p /tmp/duplicity \  
&& tar -xvzf /tmp/duplicity.tgz --strip-components=1 -C /tmp/duplicity \  
&& pip install -r /tmp/requirements.txt \  
&& cd /tmp/duplicity \  
&& python setup.py install \  
&& mkdir -p /tmp/duplicity-backup \  
&& tar -xvzf /tmp/duplicity-backup.tgz --strip-components=1 -C /tmp/duplicity-
backup \  
&& cp /tmp/duplicity-backup/duplicity-backup.sh /usr/local/bin/duplicity-
backup.sh \  
&& touch /etc/duplicity-backup.conf \  
&& apk --no-cache del \  
alpine-sdk \  
libffi-dev \  
librsync-dev \  
openssl-dev \  
tar \  
wget \  
&& rm -rf \  
/tmp/* \  
/var/cache/apk/* \  
/root/* \  
/root/.cache \  
&& chmod +x /usr/local/bin/*.sh \  
&& mkdir -p /var/log/duplicity  
  
VOLUME ["/data"]  
  
ENV ROOT=/data \  
STATIC_OPTIONS="--allow-source-mismatch" \  
LOGDIR="/var/log/duplicity/" \  
LOG_FILE="duplicity.log" \  
LOG_FILE_OWNER="nobody:nogroup"  
ENTRYPOINT ["/sbin/tini", "--", "/usr/local/bin/docker-entrypoint.sh"]  

