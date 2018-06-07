FROM ubuntu:xenial  
MAINTAINER Mitchell Hewes <me@mitcdh.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -qq \  
&& apt-get install -y nfs-kernel-server runit inotify-tools netbase -qq \  
&& apt-get remove -y fgetty -qq \  
&& apt-get clean all \  
&& rm /var/log/apt/* /var/log/alternatives.log /var/log/bootstrap.log
/var/log/dpkg.log  
  
RUN mkdir -p /exports \  
&& mkdir -p /docker-entrypoint \  
&& mkdir -p /etc/sv/nfs  
  
ADD nfs.init /etc/sv/nfs/run  
ADD nfs.stop /etc/sv/nfs/finish  
ADD nfs_setup.sh /usr/local/bin/nfs_setup  
  
VOLUME /exports  
  
EXPOSE 111/udp 2049/tcp  
  
ENTRYPOINT ["/usr/local/bin/nfs_setup"]  

