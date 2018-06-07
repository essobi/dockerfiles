FROM ubuntu:trusty  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y live-build git-core syslinux squashfs-tools \  
genisoimage unzip dctrl-tools lzma uuid-runtime \  
qt5-default libqt5webkit5-dev build-essential  
  
ADD .ssh/id_rsa /root/.ssh/  
ADD .ssh/id_rsa.pub /root/.ssh/  
ADD bin/build /usr/local/bin/build  
  
RUN chmod 0700 /root/.ssh/id_rsa  
RUN chmod 0700 /root/.ssh/id_rsa.pub  
RUN ssh-keyscan bitbucket.org >> /root/.ssh/known_hosts  
  
ADD live /live  
  
WORKDIR /live  
  
CMD ["lb", "build"]  
  

