FROM sergeyzh/centos6-epel  
  
MAINTAINER Sergey Zhukov, sergey@jetbrains.com  
  
ADD btsync_x64.tar.gz /  
ADD btsync.conf /  
  
# RUN /btsync --dump-sample-config > btsync.conf  
RUN sed -i 's/listening_port" : 0,/listening_port" : 8889,/' btsync.conf  
RUN sed -i 's|"dir" : "/home/user/bittorrent/sync_test",|"dir" :
"/mnt/storage",|' btsync.conf  
RUN sed -i 's|"storage_path" : "/home/user/.sync",|"storage_path" :
"/.sync",|' btsync.conf  
  
RUN mkdir -p /mnt/storage /.sync  
  
VOLUME ["/mnt/storage"]  
  
ADD run-services.sh /  
  
RUN chmod a+x /run-services.sh  
  
CMD /run-services.sh  
  
EXPOSE 8889  

