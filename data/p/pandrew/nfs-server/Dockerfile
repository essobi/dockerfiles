FROM debian:jessie  
RUN apt-get update && apt-get install -y nfs-kernel-server inotify-tools  
RUN mkdir -p /nfsdata  
ADD setup /  
RUN echo ' \  
RPCNFSDCOUNT=8 \  
RPCNFSDPRIORITY=0 \  
RPCMOUNTDOPTS="--manage-gids -p 2048" \  
NEED_SVCGSSD="" \  
RPCSVCGSSDOPTS="" \  
' | tee /etc/default/nfs-kernel-server  
RUN echo ' \  
NEED_STATD=no \  
NEED_IDMAPD=yes \  
NEED_GSSD=no \  
STATDOPTS="-p 2046 -o 2047" \  
' | tee /etc/default/nfs-common  
VOLUME /nfsdata  
EXPOSE 111/udp 111/tcp 2046-2049/tcp 2046-2049/udp  
ENTRYPOINT ["/setup"]  

