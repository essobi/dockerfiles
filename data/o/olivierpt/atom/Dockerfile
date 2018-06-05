# USAGE:  
#  
#PULL the image:  
# docker pull olivierpt/atom  
#  
# docker run -v /tmp/.X11-unix:/tmp/.X11-unix \  
# -v /dev/shm:/dev/shm \  
# -v ${HOME}:/home/atom \  
# -e DISPLAY=${DISPLAY} olivierpt/atom &  
#  
# BASE IMAGE: Centos LSB  
FROM olivierpt/centos-lsb  
  
MAINTAINER olivier.pillaudtirard@gmail.com  
  
ENV ATOM_VERSION v1.5.4  
RUN yum update -y && \  
yum install -y git \  
curl \  
ca-certificates \  
libgtk2.0-0 \  
libxtst6 \  
libnss3 \  
libasound2 \  
fakeroot \  
GConf2 \  
gconf-service \  
libcap2 \  
libnotify4 \  
libxtst6 \  
libnss3 \  
gvfs-bin \  
xdg-utils  
  
RUN curl -L
https://github.com/atom/atom/releases/download/${ATOM_VERSION}/atom.x86_64.rpm
> /tmp/atom.rpm  
  
RUN yum localinstall -y /tmp/atom.rpm && \  
rm -f /tmp/atom.rpm  
  
RUN useradd -d /home/atom -m atom  
  
RUN dbus-uuidgen > /etc/machine-id  
  
USER atom  
  
CMD /usr/bin/atom -f  

