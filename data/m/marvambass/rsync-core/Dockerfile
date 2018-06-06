FROM ubuntu:16.04  
ENV rsync_version 3.1.2  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get -q -y update && \  
apt-get -q -y install build-essential \  
wget && \  
apt-get -q -y install libpopt0 \  
zlib1g  
  
RUN wget https://www.samba.org/ftp/rsync/src/rsync-${rsync_version}.tar.gz &&
\  
tar xvf rsync-${rsync_version}.tar.gz && \  
rm rsync-${rsync_version}.tar.gz && \  
cd rsync-${rsync_version} && \  
./configure && \  
make && \  
make install && \  
cd \- && \  
rm -rf rsync-${rsync_version} && \  
echo -e "log file = /dev/stdout\nuse chroot = yes" > /etc/rsyncd.conf  
  
EXPOSE 873  
CMD [ "/usr/local/bin/rsync", "--no-detach", "--daemon", "--config",
"/etc/rsyncd.conf" ]  

