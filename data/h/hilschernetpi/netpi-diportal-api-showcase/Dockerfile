#use latest armv7hf compatible debian version from group resin.io as base
image  
FROM resin/armv7hf-debian:jessie  
  
#enable building ARM container on x86 machinery on the web (comment out next
line if not built as automated build on docker hub)  
RUN [ "cross-build-start" ]  
  
#labeling  
LABEL maintainer="netpi@hilscher.com" \  
version="V0.9.1.0" \  
description="PROFINET device scanner pushing identified devices as JSON
objects to Microsoft Azure"  
  
#version  
ENV HILSCHERNETPI_DIPORTAL_API_SHOWCASE_VERSION 0.9.1.0  
#copy files  
COPY "./init.d/*" /etc/init.d/  
COPY "./scanner/*" "./driver/*" "./firmware/*" /tmp/  
  
#do installation  
RUN apt-get update \  
&& apt-get install -y openssh-server build-essential python3 git
python3-setuptools libboost-all-dev libpython3.4 network-manager \  
#do users root and pi  
&& useradd --create-home --shell /bin/bash pi \  
&& echo 'root:root' | chpasswd \  
&& echo 'pi:raspberry' | chpasswd \  
&& adduser pi sudo \  
&& mkdir /var/run/sshd \  
&& sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config \  
&& sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd \  
#install netX driver and netX ethernet supporting firmware  
&& dpkg -i /tmp/netx-docker-pi-drv-1.1.3.deb \  
&& dpkg -i /tmp/netx-docker-pi-pns-eth-3.12.0.8.deb \  
#compile netX network daemon  
&& gcc /tmp/cifx0daemon.c -o /opt/cifx/cifx0daemon -I/usr/include/cifx
-Iincludes/ -lcifx -pthread \  
#install iothub client python script(s)  
&& easy_install3 pip \  
&& pip3 install azure-iothub-device-client \  
#install profinet protocol python script(s) from official repo  
&& mkdir /opt/scan \  
&& git clone https://github.com/devkid/profinet /opt/scan/profinet \  
&& sed -i -e 's;, 0x012345, 0, len(block), payload=block);, 0x012345, 255,
len(block), payload=block);' /opt/scan/profinet/dcp.py \  
#install PROFINET device scan logic and push to Microsoft's Iot hub python
script  
&& cp ./tmp/scan-ot-devices-to-iot-hub.py /opt/scan \  
#clean up  
&& rm -rf /tmp/* \  
&& apt-get remove build-essential \  
&& apt-get -yqq autoremove \  
&& apt-get -y clean \  
&& rm -rf /var/lib/apt/lists/*  
  
#set the entrypoint  
ENTRYPOINT ["/etc/init.d/entrypoint.sh"]  
  
#set STOPSGINAL  
STOPSIGNAL SIGTERM  
  
#stop processing ARM emulation (comment out next line if not built as
automated build on docker hub)  
RUN [ "cross-build-end" ]  

