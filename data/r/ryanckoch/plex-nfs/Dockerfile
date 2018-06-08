FROM ryanckoch/plex  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV HOME /root  
  
RUN apt-get update && \  
apt-get install -y nfs-common inotify-tools && \  
rm -rf /var/lib/apt/lists/*  
  
ADD nfs-configure.sh /usr/local/bin/nfs-configure  
  
RUN chmod +x /usr/local/bin/nfs-configure  
  
EXPOSE 32400  
ENTRYPOINT ["/usr/local/bin/nfs-configure"]  

