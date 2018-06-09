FROM debian  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update -qq -y  
RUN apt-get install -qq -y -o Dpkg::Options::=--force-confdef -o
Dpkg::Options::=--force-confold --purge nfs-kernel-server runit inotify-tools  
RUN mkdir -p /export  
  
RUN mkdir -p /etc/sv/nfs  
ADD nfs.init /etc/sv/nfs/run  
ADD nfs.stop /etc/sv/nfs/finish  
  
ADD nfs_setup.sh /usr/local/bin/nfs_setup  
  
VOLUME /export  
  
EXPOSE 111/udp 2049/tcp  
  
ENTRYPOINT ["/usr/local/bin/nfs_setup"]  

