FROM qnib/terminal  
  
ADD etc/yum.repos.d/fhgfs.repo /etc/yum.repos.d/fhgfs.repo  
RUN dnf install -y fhgfs-mgmtd fhgfs-meta fhgfs-storage fhgfs-helperd fhgfs-
utils fhgfs-admon  
## Do not use init.d  
RUN rm -f /etc/init.d/fhgfs-admon && mkdir -p
/data/fhgfs/fhgfs_{meta,mgmtd,storage} /mnt/fhgfs  
ADD etc/supervisord.d/ /etc/supervisord.d/  
## configure  
ADD etc/fhgfs/fhgfs-admon.conf /etc/fhgfs/fhgfs-admon.conf  
ADD etc/fhgfs/fhgfs-meta.conf /etc/fhgfs/fhgfs-meta.conf  
ADD etc/fhgfs/fhgfs-mgmtd.conf /etc/fhgfs/fhgfs-mgmtd.conf  
ADD etc/fhgfs/fhgfs-mounts.conf /etc/fhgfs/fhgfs-mounts.conf  
ADD etc/fhgfs/fhgfs-storage.conf /etc/fhgfs/fhgfs-storage.conf  
  

