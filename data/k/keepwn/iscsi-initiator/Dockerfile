FROM debian  
MAINTAINER keepwn <keepwn@gmail.com>  
  
RUN apt-get update  
RUN apt-get install -y open-iscsi  
  
RUN mkdir /mnt/storage  
WORKDIR /tmp  
COPY ./mount-iscsi.sh ./  
RUN chmod +x ./mount-iscsi.sh  
  
ENV IP 192.168.0.1  
ENV PORT 3260  
ENV TARGETNAME iqn.2005-10.org.freenas.ctl:mystorage  
ENV UUID uuid  
ENV MOUNTPOINT /mnt/storage  
  
ENTRYPOINT ["/bin/bash","/tmp/mount-iscsi.sh"]  

