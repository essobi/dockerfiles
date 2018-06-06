FROM ubuntu:xenial  
  
MAINTAINER luxaeterna  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install git wget cron -y && \  
update-rc.d cron defaults && update-rc.d cron enable && \  
wget
https://github.com/jgm/pandoc/releases/download/1.19.1/pandoc-1.19.1-1-amd64.deb
&& \  
dpkg -i pandoc-1.19.1-1-amd64.deb && \  
git clone https://github.com/imarin2/Opentotum.wiki.git /root/Opentotum.wiki
&& \  
mkdir /root/output && \  
crontab -l | { cat; echo "*/30 * * * * bash /root/clone.sh"; } | crontab -  
  
ADD /scripts/clone.sh /root/clone.sh  
WORKDIR /root/  
RUN chmod +x /root/clone.sh  
VOLUME /root/output  

