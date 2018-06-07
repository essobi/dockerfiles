FROM alpine  
MAINTAINER Mike Sheldon <mike@bloomsbury.ai>  
  
ARG DUPLICITY_VERSION=0.7.15  
  
ENV DST='' \  
EMAIL_FROM='' \  
EMAIL_SUBJECT='Backup report: {hostname} - {periodicity} - {result}' \  
EMAIL_TO='' \  
JOB_300_WHAT='backup' \  
JOB_300_WHEN='daily weekly' \  
OPTIONS='' \  
OPTIONS_EXTRA='' \  
SMTP_HOST='smtp' \  
SMTP_PORT='25' \  
SRC='/data' \  
S3_ACCESS_KEY='' \  
S3_ACCESS_TOKEN='' \  
S3_SECRET_KEY='' \  
S3_BUCKET='' \  
S3_OPTIONS='' \  
JOB_100_WHAT='s3cmd $S3_OPTIONS --access_key=$S3_ACCESS_KEY
--access_token=$S3_ACCESS_TOKEN --secret_key=$S3_SECRET_KEY sync
s3://$S3_BUCKET $SRC' \  
JOB_100_WHEN='daily weekly' \  
MYSQL_HOST='mysql' \  
MYSQL_USER='root' \  
MYSQL_PASSWORD='' \  
JOB_200_WHAT='mysqldump -A -u $MYSQL_USER --password=$MYSQL_PASSWORD -h
$MYSQL_HOST --single-transaction --routines --triggers --events --add-drop-
database > "$SRC/all-databases.sql"' \  
JOB_200_WHEN='daily weekly' \  
JOB_700_WHAT='rm $SRC/all-databases.sql' \  
JOB_700_WHEN='daily weekly'  
  
CMD ["/usr/sbin/crond", "-fd8"]  
  
# Link the job runner in all periodicities available  
RUN ln -s /usr/local/bin/jobrunner /etc/periodic/15min/jobrunner  
RUN ln -s /usr/local/bin/jobrunner /etc/periodic/hourly/jobrunner  
RUN ln -s /usr/local/bin/jobrunner /etc/periodic/daily/jobrunner  
RUN ln -s /usr/local/bin/jobrunner /etc/periodic/weekly/jobrunner  
RUN ln -s /usr/local/bin/jobrunner /etc/periodic/monthly/jobrunner  
  
# Runtime dependencies and database clients  
RUN apk add --no-cache \  
ca-certificates \  
dbus \  
gnupg \  
krb5-libs \  
lftp \  
libffi \  
librsync \  
ncftp \  
openssh \  
openssl \  
py2-gobject3 \  
python \  
mariadb-client \  
ca-certificates \  
py-setuptools \  
&& rm -rf /var/cache/apk/*  
  
# Default backup source directory  
RUN mkdir -p "$SRC"  
# Build dependencies  
RUN apk add --no-cache --virtual .build \  
build-base \  
krb5-dev \  
libffi-dev \  
librsync-dev \  
linux-headers \  
openssl-dev \  
py2-pip \  
python-dev \  
git \  
&& pip install --no-cache-dir \  
azure-storage \  
boto \  
dropbox \  
gdata \  
lockfile \  
mediafire \  
mega.py \  
paramiko \  
pexpect \  
pycryptopp \  
PyDrive \  
pykerberos \  
pyrax \  
python-keystoneclient \  
python-swiftclient \  
requests \  
requests-oauthlib \  
urllib3 \  
python-magic \  
https://code.launchpad.net/duplicity/$(echo $DUPLICITY_VERSION | sed -r
's/^([0-9]+\\.[0-9]+)([0-9\\.]*)$/\1/')-series/$DUPLICITY_VERSION/+download/duplicity-$DUPLICITY_VERSION.tar.gz
\  
&& git clone https://github.com/s3tools/s3cmd.git /tmp/s3cmd \  
&& cd /tmp/s3cmd \  
&& python setup.py install \  
&& rm -rf /tmp/s3cmd \  
&& apk del .build  
COPY bin/* /usr/local/bin/  
RUN chmod a+rx /usr/local/bin/* && sync  
  
# Metadata  
ARG VCS_REF  
ARG BUILD_DATE  
LABEL org.label-schema.schema-version="1.0" \  
org.label-schema.vendor="Bloomsbury AI" \  
org.label-schema.license=Apache-2.0 \  
org.label-schema.build-date="$BUILD_DATE" \  
org.label-schema.vcs-ref="$VCS_REF" \  
org.label-schema.vcs-url="https://github.com/Elleo/docker-duplicity"  

