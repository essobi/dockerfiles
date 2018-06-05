FROM debian:jessie  
MAINTAINER "The Doalitic Team" <devops@doalitic.com>  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y install \  
cron \  
wget \  
ca-certificates \  
build-essential \  
libpython-dev \  
python-pip \  
\--no-install-recommends \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/*  
  
RUN pip install -U crcmod  
  
RUN cd /opt \  
&& wget https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-
cloud-sdk-126.0.0-linux-x86_64.tar.gz \  
&& tar xvf google-cloud-sdk-126.0.0-linux-x86_64.tar.gz \  
&& ./google-cloud-sdk/install.sh --quiet  
  
RUN touch /var/log/bucket-backups.log  
  
RUN mkdir -p /etc/container/templates  
  
ADD ./backups.cron.tpl /etc/container/templates/  
  
ADD ./backups.default.tpl /etc/container/templates/  
  
ADD backup-bucket.sh /root/backup-bucket.sh  
  
# The following environment variables are available:  
# ------------------  
# Backup parameters  
# ------------------  
#  
# BACKUPS_SOURCE_BUCKET Backups source bucket name (required)  
# BACKUPS_DEST_BUCKET Backups destination bucket name (required)  
#  
# ----------------  
# Backups cronjob  
# ----------------  
#  
# BACKUPS_CRON_MINUTE (0-59) default = 0  
# BACKUPS_CRON_HOUR (0-23, 0 = midnight) default = 4  
# BACKUPS_CRON_DAY (1-31) default = *  
# BACKUPS_CRON_MONTH (1-12) default = *  
# BACKUPS_CRON_WEEKDAY (0-6, 0 = Sunday) default = *  
# BACKUPS_CRON_USER default = root  
# BACKUPS_CRON_COMMAND default = /root/backup-bucket.sh >> /var/log/bucket-
backups.log 2>&1  
#  
# ---------------------------------------  
# Google Cloud authentication parameters  
# ---------------------------------------  
#  
# BACKUPS_PROJECT_ID Project Id in Google Cloud (required)  
# BACKUPS_SERVICE_ACCOUNT_JSON_KEY Google Cloud Service Account Key in JSON
format (required)  
#  
RUN wget
https://github.com/jwilder/dockerize/releases/download/v0.0.4/dockerize-linux-
amd64-v0.0.4.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-v0.0.4.tar.gz \  
&& rm -f dockerize-linux-amd64-v0.0.4.tar.gz  
  
COPY ./docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["dockerize", "-template",
"/etc/container/templates/backups.cron.tpl:/etc/cron.d/backups", "-template",
"/etc/container/templates/backups.default.tpl:/etc/default/backups",
"-stdout", "/var/log/bucket-backups.log", "cron", "-f"]  

