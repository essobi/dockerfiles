FROM ubuntu:14.04  
RUN echo "deb http://archive.canonical.com/ubuntu/ trusty partner" >>
/etc/apt/sources.list && \  
dpkg --add-architecture i386 && \  
apt-get update && \  
apt-get install -y vmware-view-client  
  
CMD /usr/bin/vmware-view  

