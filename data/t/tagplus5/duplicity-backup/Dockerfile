FROM ubuntu:latest  
  
RUN DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get install -y \--no-install-recommends ca-certificates git duplicity
locales && \  
locale-gen en_US.UTF-8 && \  
git clone https://github.com/zertrin/duplicity-backup.sh.git && \  
cd /duplicity-backup.sh && \  
git checkout master && \  
ln -s /duplicity-backup.sh/duplicity-backup.sh /usr/local/bin/duplicity-backup
&& \  
apt-get purge -y git && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/*  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
  
WORKDIR /duplicity-backup.sh  
  
ENTRYPOINT ["duplicity-backup"]  

