FROM ubuntu:14.04  
MAINTAINER "Piero Giusti <pierophp@gmail.com>"  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM xterm  
  
# Upgrade  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
# NFS Server  
RUN apt-get update && \  
apt-get install -y nfs-kernel-server && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
# Supervisor  
RUN apt-get update && \  
apt-get install -y supervisor && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
# Tools  
RUN apt-get update && \  
apt-get install -y nano wget curl && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /export/docker  
#RUN mount --bind /docker /export/docker  
  
ADD nfs-run.sh /usr/local/bin/nfs-run  
ADD nfs/exports /etc/exports  
  
RUN exportfs -a  
  
RUN chmod +x /usr/local/bin/nfs-run  
  
EXPOSE 111/udp 2049/tcp  
  
ADD supervisor/* /etc/supervisor/conf.d/  
CMD ["/usr/bin/supervisord", "--nodaemon", "-c",
"/etc/supervisor/supervisord.conf"]  

