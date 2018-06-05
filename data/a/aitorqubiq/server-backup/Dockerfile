FROM tecnativa/cron:latest  
MAINTAINER Tecnativa <info@tecnativa.com>  
  
# Install everything required  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get upgrade -y && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
zip \  
python-dateutil \  
python-magic \  
wget \  
net-tools \  
vim-common \  
bzip2 && \  
echo deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main \  
> /etc/apt/sources.list.d/pgdg.list && \  
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc \  
| apt-key add \- && \  
DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y postgresql-client && \  
apt-get clean -y && apt-get autoclean -y && apt-get autoremove -y && \  
rm -rf /var/cache/apt/archives/* /var/cache/apt/*.bin /var/lib/apt/lists/* &&
\  
echo "Downloading s3cmd ..." && \  
wget -qO- https://github.com/s3tools/s3cmd/archive/master.tar.gz | tar -xzC
/opt && \  
ln -s /opt/s3cmd-master/s3cmd /usr/bin/s3cmd && \  
echo "Downloading s3md5 ..." && \  
wget -qO- https://github.com/antespi/s3md5/archive/master.tar.gz | tar -xzC
/opt && \  
ln -s /opt/s3md5-master/s3md5 /usr/bin/s3md5 && \  
echo "Downloading server-backup ..." && \  
wget -qO- https://github.com/antespi/server-backup/archive/docker.tar.gz | tar
-xzC /opt && \  
mv /opt/server-backup-docker /opt/server-backup && \  
mkdir -p /opt/backupdata && \  
mkdir -p /opt/source  
  
VOLUME ["/opt/backupdata", "/opt/source"]  
  
COPY ./docker_files/config/.s3cfg /root  
COPY ./docker_files/config/backup.sh /opt/server-backup/  
  
ADD config /opt/server-backup/config  
ADD backup /etc/cron.d/  
ADD croninit restore /usr/local/bin/  
RUN chmod a+rx /usr/local/bin/*  
  
ENTRYPOINT ["/usr/local/bin/entrypoint"]  
CMD ["tail", "-f", "/var/log/syslog"]  

