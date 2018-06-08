# muxer/base  
#  
# VERSION 0.1.0  
FROM ubuntu:12.04  
MAINTAINER Fletcher Nichol "fnichol@nichol.ca"  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv 63844AC3  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
RUN echo "deb http://ppa.launchpad.net/kalakris/tmux/ubuntu precise main" >>
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get upgrade  
  
RUN locale-gen en_US en_US.UTF-8  
  
RUN apt-get install -y openssh-server && mkdir -p /var/run/sshd && rm -f
/etc/ssh/ssh_host_*  
  
RUN apt-get install -y sudo && echo '%muxer ALL=(ALL) NOPASSWD:ALL' >
/etc/sudoers.d/muxer && chmod 0440 /etc/sudoers.d/muxer  
  
RUN groupadd muxer  
RUN useradd -d /home/muxer -g muxer -m -s /bin/bash muxer && passwd --lock
muxer && chmod 0700 /home/muxer  
  
RUN apt-get install -y autoconf bison build-essential curl git emacs less man-
db mercurial nano netcat-openbsd telnet tmux tree vim  
RUN apt-get -y autoremove  
  
ADD profile_d_muxer.sh /etc/profile.d/zzz_muxer.sh  
ADD sshd_config /etc/ssh/sshd_config  
ADD tmux.conf /etc/tmux.conf  
ADD muxer-init /sbin/muxer-init  
  
EXPOSE 22  
ENTRYPOINT ["/sbin/muxer-init"]  
CMD ["-e"]  

