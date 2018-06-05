FROM ubuntu:14.04  
MAINTAINER Frank Wong, Amy Motta <devops@vigorsystemsinc.com>  
RUN apt-get update && \  
apt-get install -y curl && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
curl -o /usr/bin/btsync.tar.gz http://download-
lb.utorrent.com/endpoint/btsync/os/linux-x64/track/stable && \  
cd /usr/bin && \  
tar -xzvf btsync.tar.gz && \  
rm -f btsync.tar.gz  
RUN mkdir -p /btsync/.sync  
RUN mkdir -p /var/run/btsync  
RUN mkdir -p /data  
EXPOSE 8888  
EXPOSE 55555  
ADD start-btsync /usr/bin/start-btsync  
RUN chmod +x /usr/bin/start-btsync  
VOLUME ["/data"]  
ENTRYPOINT ["start-btsync"]  

