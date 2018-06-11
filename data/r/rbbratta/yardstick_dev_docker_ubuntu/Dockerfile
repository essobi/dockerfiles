##############################################################################  
# Copyright (c) 2015 Ericsson AB and others.  
#  
# All rights reserved. This program and the accompanying materials  
# are made available under the terms of the Apache License, Version 2.0  
# which accompanies this distribution, and is available at  
# http://www.apache.org/licenses/LICENSE-2.0  
##############################################################################  
  
FROM ubuntu:16.04  
  
  
  
# WHY? Is this workaround still needed?  
# https://wiki.debian.org/mmap_min_addr#apps  
# qemu, as shipped in Debian 5.0, requires low virtual memory mmaps.
mmap_min_addr must be set to 0 to run qemu as a non-root user. This limitation
has been removed upstream, so qemu should work with an increased mmap_min_addr
starting with Debian squeeze.  
#RUN echo "vm.mmap_min_addr = 0" > /etc/sysctl.d/mmap_min_addr.conf  
  
# This will prevent questions from being asked during the install  
ENV DEBIAN_FRONTEND=noninteractive  
RUN apt-get update && apt-get install -y \  
build-essential \  
qemu-user-static \  
wget \  
expect \  
curl \  
git \  
sshpass \  
qemu-utils \  
kpartx \  
parted \  
libffi-dev \  
openssl \  
libssl-dev \  
libzmq-dev \  
python \  
python-dev \  
libxml2-dev \  
libxslt1-dev \  
nginx \  
uwsgi \  
uwsgi-plugin-python \  
supervisor \  
python-minimal \  
screen \  
procps \  
socat \  
unzip \  
ccze \  
htop \  
dstat \  
iperf \  
iperf3 \  
libpcap-dev \  
ca-certificates \  
python-setuptools && \  
easy_install -U setuptools==30.0.0 && \  
apt-get -y autoremove && \  
apt-get clean  
  
  
# download the latest pip  
RUN curl -s "https://bootstrap.pypa.io/get-pip.py" | python2.7 -  
  
COPY requirements.txt /tmp  
  
RUN pip install -r /tmp/requirements.txt  
  
  
CMD ["/bin/bash"]  

