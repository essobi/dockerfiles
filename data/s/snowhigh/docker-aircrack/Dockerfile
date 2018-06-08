FROM ubuntu:xenial  
  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y vim gcc make sqlite3 pkg-config
libnl-genl-3-dev libssl-dev net-tools iw ethtool usbutils pciutils wireless-
tools && \  
apt-get clean  
  
ADD run.sh /run.sh  
ADD aircrack-ng-1.2-rc4.tar.gz /  
  
WORKDIR /work/  
  
CMD ["/run.sh"]  

