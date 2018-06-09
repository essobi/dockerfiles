FROM teffcz/debian:latest  
MAINTAINER Tomas Effenberger <effik@effik.cz>  
ENV LANG en_US.UTF-8  
ENV ETCD_NODE 172.17.42.1:4001  
ENV confd_ver 0.7.1  
RUN locale-gen $LANG && \  
wget --retry-connrefused -t 5 http://download-
new.utorrent.com/endpoint/btsync/os/linux-x64/track/stable -O /btsync.tar.gz
&& \  
tar xvf /btsync.tar.gz && \  
rm /btsync.tar.gz && \  
wget --progress=bar:force --retry-connrefused -t 5
https://github.com/kelseyhightower/confd/releases/download/v${confd_ver}/confd-${confd_ver}-linux-
amd64 -O /bin/confd && \  
chmod +x /bin/confd  
  
ADD start.sh /start.sh  
ADD confd /etc/confd  
  
VOLUME ["/data"]  
EXPOSE 3369/udp  
EXPOSE 8888  
CMD ["/start.sh"]  

