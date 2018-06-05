FROM ubuntu:14.04  
RUN apt-get update && apt-get upgrade -y && apt-get clean  
  
#nfs install  
RUN apt-get install -y nfs-kernel-server  
RUN update-rc.d rpcbind enable  
VOLUME /mnt  
RUN chown nobody:nogroup /mnt  
RUN echo "/mnt *(rw,sync,fsid=0,no_root_squash,no_subtree_check)" >>
/etc/exports  
RUN exportfs -a  
RUN service nfs-kernel-server start  
RUN touch "/mnt/created_$(date +'%m%d%y')"  
CMD /etc/init.d/rpcbind start  

