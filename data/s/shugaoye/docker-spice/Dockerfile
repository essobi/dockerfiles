# Copyright (C) 2017 AOSP/QEMU/SPICE/OP-TEE build environment in docker  
#  
# Licensed under the Apache License, Version 2.0 (the "License");  
# you may not use this file except in compliance with the License.  
# You may obtain a copy of the License at  
#  
# http://www.apache.org/licenses/LICENSE-2.0  
#  
# Unless required by applicable law or agreed to in writing, software  
# distributed under the License is distributed on an "AS IS" BASIS,  
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
# See the License for the specific language governing permissions and  
# limitations under the License.  
#  
#******************************************************************************  
#  
# Dockerfile - build environment for AOSP/QEMU/SPICE/OP-TEE  
# This docker image can be used to build Android, QEMU, SPICE  
# and OP-TEE.  
#  
# Copyright (c) 2017 Roger Ye. All rights reserved.  
#  
#******************************************************************************  
#  
FROM shugaoye/docker-aosp:ubuntu16.04-JDK7  
  
MAINTAINER Roger Ye <shugaoye@yahoo.com>  
  
# This is needed on later Ubuntu distros to be able to install the i386  
# packages.  
RUN dpkg --add-architecture i386  
  
COPY utils/sources.list /etc/apt/sources.list  
  
ENV PACKAGES autoconf ccache clang cscope gcc gdisk genisoimage gettext gtk-
doc-tools \  
iputils-ping iasl \  
kmod \  
libc6:i386 \  
libcap-dev \  
libepoxy-dev \  
libfdt-dev \  
libftdi-dev \  
libgbm-dev \  
libgles2-mesa-dev \  
libglib2.0-dev \  
libgnutls-dev \  
libgtk-3-dev \  
libhidapi-dev \  
libiscsi-dev \  
libjpeg-dev \  
libnss3-dev \  
libogg-dev \  
libpixman-1-dev \  
libpng12-dev \  
librados-dev \  
libsdl2-dev \  
libseccomp-dev \  
libssh2-1-dev \  
libssl-dev \  
libstdc++6:i386 \  
libtext-csv-perl \  
libtool \  
libusb-1.0-0-dev \  
libvte-2.91-dev \  
libxml2-dev \  
libz1:i386 \  
make mc mtools net-tools netcat openssh-server \  
python python-crypto python-mako python-pip python-serial python-wand python-
yaml \  
sparse telnet tmux unzip uuid-dev \  
valac vim xdg-utils xterm xz-utils  
  
RUN apt-get update && apt-get -y install $PACKAGES && apt-get build-dep -y
spice-gtk  
  
ENV FEATURES clang pyyaml  
  
RUN mkdir /var/run/sshd  
RUN export LC_ALL=C  
  
RUN echo 'root:root' | chpasswd  
  
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  
  
# The persistent data will be in these two directories, everything else is  
# considered to be ephemeral  
VOLUME ["/tmp/ccache", "/home/aosp"]  
  
# Improve rebuild performance by enabling compiler cache  
ENV USE_CCACHE 1  
ENV CCACHE_DIR /tmp/ccache  
  
# Work in the build directory, repo is expected to be init'd here  
WORKDIR /home/aosp  
  
COPY utils/bash.bashrc /root/bash.bashrc  
RUN chmod 755 /root /root/bash.bashrc  
COPY utils/setup_build.sh /root/setup_build.sh  
RUN chmod 755 /root/setup_build.sh  
COPY utils/docker_entrypoint.sh /root/docker_entrypoint.sh  
ENTRYPOINT ["/root/docker_entrypoint.sh"]  

