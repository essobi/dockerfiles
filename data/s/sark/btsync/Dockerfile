FROM google/debian:wheezy  
MAINTAINER Robin <robin@naas.io>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN mkdir /btsync  
  
ADD http://download.getsyncapp.com/endpoint/btsync/os/linux-x64/track/stable
/btsync/bittorrent_sync_x64.tar.gz  
ADD bootstrap.sh /bootstrap.sh  
  
RUN cd /btsync && tar xvf bittorrent_sync_x64.tar.gz  
RUN mv /btsync/btsync /usr/local/bin/btsync  
RUN rm -fr /btsync/*  
  
RUN chmod a+x /usr/local/bin/btsync  
RUN chmod +x /bootstrap.sh  
  
VOLUME ["/data"]  
EXPOSE 3369/udp  
  
CMD ["/bootstrap.sh"]  

