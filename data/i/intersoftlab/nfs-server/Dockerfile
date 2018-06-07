FROM ubuntu  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update -qq && apt-get install -y nfs-kernel-server runit inotify-
tools -qq  
RUN sed -i 's/^STATDOPTS=.*/STATDOPTS="--port 4000"/' /etc/default/nfs-common  
RUN sed -i 's/^NEED_STATD=.*/NEED_STATD=yes/' /etc/default/nfs-common  
RUN sed -i 's/^RPCMOUNTDOPTS="\\(.*\\)"/RPCMOUNTDOPTS="\1 --port 5000"/'
/etc/default/nfs-kernel-server  
RUN mkdir -p /exports  
  
RUN mkdir -p /etc/sv/nfs  
ADD nfs.init /etc/sv/nfs/run  
ADD nfs.stop /etc/sv/nfs/finish  
  
ADD nfs_setup.sh /usr/local/bin/nfs_setup  
  
VOLUME /exports  
  
EXPOSE 111/udp 111/tcp 2049/udp 2049/tcp 4000/tcp 5000/tcp  
  
ENTRYPOINT ["/usr/local/bin/nfs_setup"]  

