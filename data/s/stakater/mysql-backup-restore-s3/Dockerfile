FROM phusion/baseimage:0.9.19  
MAINTAINER Rasheed Amir <rasheed@aurorasolutions.io>  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu xenial main universe" >
/etc/apt/sources.list && \  
apt-get -y update && \  
apt-get install -y --no-install-recommends mysql-client && \  
apt-get install -y python-pip && \  
apt-get -y install sudo nano git sudo zip bzip2 fontconfig wget && \  
pip install --upgrade pip && \  
pip install awscli && \  
mkdir /backup  
  
ENV CRON_TIME="00 00 * * *" \  
MYSQL_DB="--all-databases" \  
S3_BUCKET_NAME="docker-backups.example.com" \  
AWS_ACCESS_KEY_ID="**DefineMe**" \  
AWS_SECRET_ACCESS_KEY="**DefineMe**" \  
AWS_DEFAULT_REGION="us-east-1" \  
PATHS_TO_BACKUP="/paths/to/backup" \  
BACKUP_NAME="backup" \  
LAST_BACKUP="" \  
RESTORE="true"  
ADD run.sh /run.sh  
  
VOLUME ["/backup"]  
  
CMD ["/run.sh"]  

