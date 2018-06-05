FROM debian:jessie  
MAINTAINER "The Doalitic Team" <devops@doalitic.com>  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y install \  
cron \  
ca-certificates \  
wget \  
curl \  
apt-transport-https \  
\--no-install-recommends \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/*  
  
ENV PERCONA_RELEASE_VERSION 0.1-4  
ENV PERCONA_XTRABACKUP_VERSION 22  
RUN wget https://repo.percona.com/apt/percona-
release_${PERCONA_RELEASE_VERSION}.jessie_all.deb \  
&& DEBIAN_FRONTEND=noninteractive dpkg -i \  
percona-release_${PERCONA_RELEASE_VERSION}.jessie_all.deb \  
&& rm percona-release_${PERCONA_RELEASE_VERSION}.jessie_all.deb \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y install \  
percona-xtrabackup-${PERCONA_XTRABACKUP_VERSION} \  
\--no-install-recommends \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/*  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y install \  
groff \  
less \  
libffi-dev \  
libssl-dev \  
libpython-dev \  
python-pip \  
build-essential \  
\--no-install-recommends \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/*  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y install \  
mysql-client \  
\--no-install-recommends \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/*  
  
ENV CLOUD_SDK_REPO cloud-sdk-jessie  
RUN echo "deb https://packages.cloud.google.com/apt ${CLOUD_SDK_REPO} main" |
tee -a /etc/apt/sources.list.d/google-cloud-sdk.list \  
&& curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
\  
&& apt-get update \  
&& apt-get -y install \  
google-cloud-sdk \  
\--no-install-recommends \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/*  
  
RUN pip install pyasn1 --upgrade  
  
RUN pip install awscli  
  
RUN touch /var/log/mysql-backup-complete.log \  
&& touch /var/log/mysql-backup-incremental.log \  
&& touch /var/log/mysql-backup-logical.log  
  
RUN mkdir -p /etc/container/templates  
  
ADD ./boto.tpl /etc/container/templates/  
  
ADD ./backups.cron.tpl /etc/container/templates/  
  
ADD ./backups.default.tpl /etc/container/templates/  
  
ADD mysql-backup-complete.sh /root/mysql-backup-complete.sh  
  
ADD mysql-backup-incremental.sh /root/mysql-backup-incremental.sh  
  
ADD mysql-backup-logical.sh /root/mysql-backup-logical.sh  
  
# The following environment variables are available:  
# \---------------------------  
# MySQL connection parameters  
# \---------------------------  
#  
# DBHOST MySQL host address (required)  
# DBPORT MySQL host port. default = 3306  
# DBUSER MySQL username (required)  
# DBPASSWORD MySQL Password (required)  
# DBNAME MySQL Database (required for logical backup)  
# BACKUPS_DSTDIR MySQL Backups destination directory. default = /backups  
#  
# \---------------------------  
# MySQL complete backup cron  
# \---------------------------  
#  
# MYSQL_COMPLETE_CRON_MINUTE (0-59) default = 0  
# MYSQL_COMPLETE_CRON_HOUR (0-23, 0 = midnight) default = 3  
# MYSQL_COMPLETE_CRON_DAY (1-31) default = *  
# MYSQL_COMPLETE_CRON_MONTH (1-12) default = *  
# MYSQL_COMPLETE_CRON_WEEKDAY (0-6, 0 = Sunday) default = 1  
# MYSQL_COMPLETE_CRON_USER default = root  
# MYSQL_COMPLETE_CRON_COMMAND default = /root/mysql-backup-complete.sh >>
/var/log/mysql-backup-complete.log 2>&1  
#  
# \-----------------------------  
# MySQL incremental backup cron  
# \-----------------------------  
#  
# MYSQL_INCREMENTAL_CRON_MINUTE (0-59) default = 0  
# MYSQL_INCREMENTAL_CRON_HOUR (0-23, 0 = midnight) default = 3  
# MYSQL_INCREMENTAL_CRON_DAY (1-31) default = *  
# MYSQL_INCREMENTAL_CRON_MONTH (1-12) default = *  
# MYSQL_INCREMENTAL_CRON_WEEKDAY (0-6, 0 = Sunday) default = 0,2,3,4,5,6  
# MYSQL_INCREMENTAL_CRON_USER default = root  
# MYSQL_INCREMENTAL_CRON_COMMAND default = /root/mysql-backup-incremental.sh
>> /var/log/mysql-backup-incremental.log 2>&1  
#  
# \-------------------------  
# MySQL logical backup cron  
# \-------------------------  
#  
# MYSQL_LOGICAL_CRON_MINUTE (0-59) default = 0  
# MYSQL_LOGICAL_CRON_HOUR (0-23, 0 = midnight) default = 5  
# MYSQL_LOGICAL_CRON_DAY (1-31) default = 1-7  
# MYSQL_LOGICAL_CRON_MONTH (1-12) default = *  
# MYSQL_LOGICAL_CRON_WEEKDAY (0-6, 0 = Sunday) default = *  
# MYSQL_LOGICAL_BACKUP_WEEKDAY (0-6, 0 = Sunday) default = 1 (Monday)  
# MYSQL_LOGICAL_CRON_USER default = root  
# MYSQL_LOGICAL_CRON_COMMAND default = /root/mysql-backup-logical.sh >>
/var/log/mysql-backup-logical.log 2>&1  
#  
# \--------------------------------  
# Storage configuration parameters  
# \--------------------------------  
#  
# STORAGE_PROVIDER Storage Provider name (aws or gcloud, required)  
# PROVIDER_DST_BUCKET Google Storage destination bucket for MySQL backups
(required)  
#  
# \--------------------------------  
# AWS configuration  
# \--------------------------------  
#  
# AWS_ACCESS_KEY_ID AWS Access Key Identifier (required if provider is set to
'aws')  
# AWS_SECRET_ACCESS_KEY AWS Secret Access Key (required if provider is set to
'aws')  
#  
# \-----------------------------  
# Google Cloud configuration  
# \-----------------------------  
#  
# GCLOUD_OAUTH2_REFRESH_TOKEN OAuth 2 refresh_token for Google Storage
(required if provider is set to 'gcloud')  
# GCLOUD_DEFAULT_PROJECT_ID Project Id in Google Cloud (required if provider
is set to 'gcloud')  
#  
  
RUN wget
https://github.com/jwilder/dockerize/releases/download/v0.0.4/dockerize-linux-
amd64-v0.0.4.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-v0.0.4.tar.gz \  
&& rm -f dockerize-linux-amd64-v0.0.4.tar.gz  
  
CMD ["dockerize", "-template",
"/etc/container/templates/boto.tpl:/root/.boto", "-template",
"/etc/container/templates/backups.cron.tpl:/etc/cron.d/backups", "-template",
"/etc/container/templates/backups.default.tpl:/etc/default/backups",
"-stdout", "/var/log/mysql-backup-complete.log", "-stdout", "/var/log/mysql-
backup-incremental.log", "-stdout", "/var/log/mysql-backup-logical.log",
"cron", "-f"]  

