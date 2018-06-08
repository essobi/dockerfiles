FROM jchavas/saucy-debootstrap  
  
#######################################  
# initialization  
#######################################  
ENV DEBIAN_FRONTEND noninteractive  
  
#######################################  
# some generic installs  
#######################################  
ENV TERM xterm  
ENV HOME /root  
RUN echo "cd ~" >> /root/.bashrc  
RUN grep -v rootfs /proc/mounts > /etc/mtab  
RUN echo "deb http://archive.ubuntu.com/ubuntu saucy universe" >>
/etc/apt/sources.list  
RUN apt-get -y update  
RUN apt-get -y install libterm-readline-gnu-perl dialog  
RUN apt-get -y install language-pack-en-base  
RUN dpkg-reconfigure locales  
RUN echo "export LANG=en_US.UTF-8 LANGUAGE=en_US.UTF-8 LC_ALL=en_US.UTF-8" >>
/etc/bash.bashrc  
RUN apt-get -y install locate && updatedb  
  
#######################################  
# Fake a fuse install  
#######################################  
RUN apt-get -y install libfuse2  
RUN cd /tmp ; apt-get -y download fuse && dpkg-deb -x fuse_* . && dpkg-deb -e
fuse_* && rm fuse_*.deb  
RUN cd /tmp ; echo '#!/bin/bash\nexit 0\n' > DEBIAN/postinst && dpkg-deb -b .
/fuse.deb && dpkg -i /fuse.deb  
  
#######################################  
# dbus related, workaround to make dbus work  
# the last line suppresses dbus warning due to X forwarding  
#######################################  
RUN dpkg-divert --local --rename --add /sbin/initctl && ln -s /bin/true
/sbin/initctl  
RUN apt-get -y install dbus-x11  
RUN echo "export NO_AT_BRIDGE=1" >> /etc/bash.bashrc  
  
#######################################  
# cleaning  
#######################################  
RUN unset DEBIAN_FRONTEND  

