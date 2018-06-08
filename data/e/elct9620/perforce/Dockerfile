###  
# Percona Server 4  
###  
FROM ubuntu:precise  
  
MAINTAINER 蒼時弦也 "docker@frost.tw"  
# Environnement  
ENV P4JOURNAL /perforce/journal  
ENV P4PORT 1666  
ENV P4ROOT /perforce  
ENV HOME /home/perforce  
  
# Setup Package  
RUN apt-get update && \  
apt-get install wget curl -y && \  
wget -q http://package.perforce.com/perforce.pubkey -O - | apt-key add - && \  
echo "deb http://package.perforce.com/apt/ubuntu precise release" >>
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install perforce-server -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Create directory  
RUN mkdir -p $P4ROOT && \  
mkdir -p $HOME/Perforce && \  
mkdir -p /var/log/perforce  
  
# Setup Perforce user  
RUN addgroup p4admin && \  
chown -R perforce:p4admin $P4ROOT && \  
chown -R perforce:p4admin $HOME && \  
chown -R perforce:p4admin /var/log/perforce  
  
# Expose Ports  
EXPOSE 1666  
# Setup entrypoint into p4d  
ENTRYPOINT p4d  
  
# Running Perforce Server  
CMD ["p4d", "-r", $P4DROOT]  

