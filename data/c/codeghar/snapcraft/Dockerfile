FROM ubuntu:xenial  
  
WORKDIR /root  
  
ENV LC_ALL=C.UTF-8 LANG=C.UTF-8 SNAPCRAFT_SETUP_CORE=1 container=docker
PATH=/snap/bin:$PATH  
  
RUN apt update &&\  
apt install -y fuse make snapd snap-confine squashfuse sudo snapcraft &&\  
dpkg-divert --local \--rename --add /sbin/udevadm &&\  
ln -s /bin/true /sbin/udevadm &&\  
systemctl enable snapd  
  
VOLUME ["/sys/fs/cgroup"]  
  
STOPSIGNAL SIGRTMIN+3  
CMD ["/sbin/init"]  

