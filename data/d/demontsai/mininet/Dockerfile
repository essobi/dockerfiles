#######################################################  
# This dockerfile builds a mininet environment #  
# #  
# #  
# Author: Demon Tsai #  
# Repository: demontsai/mininet:2.2.1 #  
# Version: 1.0 #  
# #  
#######################################################  
  
FROM demontsai/ubuntu64:14.04  
  
MAINTAINER Demon Tsai demontsai@estinet.com  
  
  
##### Update system and install apps  
RUN apt-get -qq update  
RUN apt-get -qqy install openssh-server  
  
##### Environment  
ENV MININET_REPO git://github.com/mininet/mininet  
ENV MININET_VERSION 2.2.1  
ENV MININET_INSTALLER util/install.sh  
ENV MININET_OPT -nfv  
  
##### Mininet install  
RUN git clone $MININET_REPO /root/installation/mininet  
WORKDIR /root/installation/mininet  
RUN git checkout -b $MININET_VERSION $MININET_VERSION  
RUN $MININET_INSTALLER $MININET_OPT  
RUN echo "service openvswitch-switch start" >> $ENTRYPOINT  
RUN echo "/usr/sbin/sshd -D" >> $ENTRYPOINT  
WORKDIR /root  
  
##### Sync source code folder  
VOLUME ["/root/code"]  
  
##### SSH setting  
RUN sudo -u estinet /usr/bin/ssh-keygen -t ecdsa -N "" -f
/home/estinet/.ssh/id_ecdsa  
RUN sudo -u estinet /usr/bin/ssh-keygen -t rsa -N "" -f
/home/estinet/.ssh/id_rsa  
RUN mkdir -p /var/run/sshd  
EXPOSE 22  
  
##### Clean  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /root/installation/*  
  
##### Command  
ENTRYPOINT $ENTRYPOINT  

