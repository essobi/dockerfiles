FROM ubuntu  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update -qq && apt-get install -y nfs-kernel-server runit inotify-
tools -qq && \  
apt-get remove -y --auto-remove fgetty && \  
apt-get purge -y --auto-remove fgetty  
RUN mkdir -p /exports  
  
RUN mkdir -p /etc/sv/nfs  
ADD nfs.init /etc/sv/nfs/run  
ADD nfs.stop /etc/sv/nfs/finish  
ADD services /etc/services  
  
ADD nfs_setup.sh /usr/local/bin/nfs_setup  
  
VOLUME /exports  
  
EXPOSE 111/udp 2049/tcp  
  
ENTRYPOINT ["/usr/local/bin/nfs_setup"]  

