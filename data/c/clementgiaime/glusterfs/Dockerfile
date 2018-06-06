FROM ubuntu:16.04  
ENV RC_VERSION 3.11  
RUN apt-get update && \  
apt-get install -y apt-utils debconf-utils python-software-properties
software-properties-common && \  
add-apt-repository ppa:gluster/glusterfs-${RC_VERSION} && \  
apt-get update && \  
apt-get install -y glusterfs-server && \  
mkdir /srv/gluster  
  
RUN glusterd  
  
COPY entrypoint.sh /  
  
EXPOSE 111 24007 24008 49152 49153 49154 49155 49156 49157 49158 49159  
ENTRYPOINT ["/entrypoint.sh"]  

