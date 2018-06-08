FROM ubuntu:14.04  
MAINTAINER Masato Shimizu <ma6ato@gmail.com>  
  
ENV LANG ja_JP.UTF-8  
RUN locale-gen $LANG && update-locale $LANG && \  
ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime  
  
ADD http://download-lb.utorrent.com/endpoint/btsync/os/linux-x64/track/stable
/btsync.tar.gz  
RUN tar xzf /btsync.tar.gz -C /usr/bin && \  
rm /btsync.tar.gz && mkdir -p /btsync/.sync  
  
EXPOSE 55555  
ADD run.sh /run.sh  
  
VOLUME ["/data"]  
ENTRYPOINT ["/run.sh"]  

