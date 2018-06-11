##############################################################################  
# Copyright (c) 2017 Intel Corporation  
#  
# All rights reserved. This program and the accompanying materials  
# are made available under the terms of the Apache License, Version 2.0  
# which accompanies this distribution, and is available at  
# http://www.apache.org/licenses/LICENSE-2.0  
##############################################################################  
  
FROM centos:7.3.1611  
  
  
  
  
  
  
RUN yum -y install\  
deltarpm \  
wget \  
expect \  
curl \  
git \  
sshpass \  
qemu-kvm \  
qemu-utils \  
kpartx \  
parted \  
libffi-devel \  
openssl-devel \  
zeromq2-devel \  
python \  
python-devel \  
libxml2-devel \  
libxslt-devel \  
nginx \  
uwsgi \  
uwsgi-plugin-python \  
supervisor \  
ansible \  
deltarpm \  
wget \  
iptables-services \  
lvm2 \  
lvm2-libs \  
libselinux-python \  
screen \  
psacct \  
git \  
socat \  
vim-enhanced \  
vim \  
libxslt-devel \  
libffi-devel \  
autoconf \  
automake \  
binutils \  
bison \  
flex \  
gcc \  
gcc-c++ \  
gettext \  
libtool \  
make \  
patch \  
pkgconfig \  
redhat-rpm-config \  
rpm-build \  
rpm-sign \  
diffstat \  
elfutils \  
git \  
intltool \  
patchutils \  
strace \  
python-devel \  
libpcap-devel \  
ccze \  
ca-certificates \  
python-setuptools && \  
easy_install -U setuptools==30.0.0 && \  
yum clean all  
  
  
# download the latest pip  
RUN curl -s "https://bootstrap.pypa.io/get-pip.py" | python2.7 -  
  
COPY requirements.txt /tmp  
  
RUN pip install -r /tmp/requirements.txt  
  
  
CMD ["/bin/bash"]  

