FROM busybox:ubuntu-14.04  
MAINTAINER Ron Waldon <jokeyrhyme@gmail.com>  
  
WORKDIR /tmp  
RUN wget -O btsync_x64.tar.gz http://download-
lb.utorrent.com/endpoint/btsync/os/linux-x64/track/stable  
RUN tar zxf btsync_x64.tar.gz  
RUN cp btsync /bin  
RUN chown root:root /bin/btsync  
RUN rm -f /tmp/btsync* /tmp/LICENSE.*  
  
RUN mkdir -p /mnt/.sync  
ADD btsync.json /etc/btsync.json  
  
EXPOSE 3000 8888  
CMD btsync --nodaemon --config /etc/btsync.json  

