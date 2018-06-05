FROM fedora  
  
RUN dnf install -y nfs-ganesha nfs-ganesha-vfs glusterfs  
EXPOSE 2049/tcp  
ADD vfs.conf /vfs.conf  
ENTRYPOINT ["ganesha.nfsd", "-F", "-L", "/var/log/ganesha.log", "-f",
"/vfs.conf"]  

