#use fixed armv7hf compatible raspbian OS version from group resin.io as base
image  
FROM resin/armv7hf-debian:stretch-20171118  
#enable building ARM container on x86 machinery on the web (comment out next
line if built on Raspberry)  
RUN [ "cross-build-start" ]  
  
#execute all commands as root  
USER root  
  
#labeling  
LABEL maintainer="netpi@hilscher.com" \  
version="V0.9.1.0" \  
description="Debian stretch with SSH and Linux RT patch tests"  
  
#version  
ENV HILSCHERNETPI_LINUX_RTPATCH_TEST 0.9.1.0  
#install ssh, give user "root" a password  
RUN apt-get update \  
&& apt-get install -y openssh-server \  
&& echo 'root:root' | chpasswd \  
&& sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config \  
&& sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd \  
&& mkdir /var/run/sshd  
# && sed -i -e 's;Port 22;Port 23;' /etc/ssh/sshd_config \ #Comment in if
other SSH port (22->23) is needed  
#get, compile and install RT tests  
RUN apt-get install build-essential git wget \  
&& git clone git://git.kernel.org/pub/scm/utils/rt-tests/rt-tests.git \  
&& cd rt-tests \  
&& git checkout stable/v1.0 \  
&& make all \  
&& make install  
  
#SSH port  
EXPOSE 22  
#start SSH as service  
ENTRYPOINT ["/usr/sbin/sshd", "-D"]  
  
#set STOPSGINAL  
STOPSIGNAL SIGTERM  
  
#stop processing ARM emulation (comment out next line if built on Raspberry)  
RUN [ "cross-build-end" ]  

