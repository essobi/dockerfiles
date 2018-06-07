FROM greatbsky/centos7:latest  
MAINTAINER architect.bian  
LABEL name="rsync" license="MIT" build-date="20170221"  
  
ENV RSYNC_VERSION 3.1.2  
RUN yum update -y && cd /data/softs && wget
https://download.samba.org/pub/rsync/src/rsync-$RSYNC_VERSION.tar.gz && tar
-zxf rsync-$RSYNC_VERSION.tar.gz && cd rsync-$RSYNC_VERSION && ./configure &&
make && make install && rm -rf /data/softs/rsync-*  
  
COPY rsyncd.conf /etc/rsyncd.conf  
COPY rsyncd.passwd /etc/rsyncd.passwd  
RUN ln -sf /dev/stdout /var/log/rsync.log && chmod 600 /etc/rsyncd.passwd  
  
CMD ["rsync", "--no-detach", "--daemon"]  

