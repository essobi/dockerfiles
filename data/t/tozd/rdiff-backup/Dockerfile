FROM tozd/cron:ubuntu-xenial  
  
VOLUME /source/host  
VOLUME /source/data  
VOLUME /backup  
VOLUME /etc/backup.d  
  
ENV RDIFF_BACKUP_EXPIRE 12M  
  
RUN apt-get update -q -q && \  
apt-get install rdiff-backup apt-transport-https ca-certificates curl
software-properties-common --yes --force-yes && \  
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - && \  
add-apt-repository "deb https://download.docker.com/linux/ubuntu $(lsb_release
-cs) stable" && \  
apt-get update -q -q && \  
apt-get install docker-ce --yes --force-yes  
  
COPY ./etc /etc  

