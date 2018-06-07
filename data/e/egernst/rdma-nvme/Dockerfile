#  
# Copyright (C) 2016 Intel Corporation  
#  
# This program is free software; you can redistribute it and/or  
# modify it under the terms of the GNU General Public License  
# as published by the Free Software Foundation; either version 2  
# of the License, or (at your option) any later version.  
#  
# This program is distributed in the hope that it will be useful,  
# but WITHOUT ANY WARRANTY; without even the implied warranty of  
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  
# GNU General Public License for more details.  
#  
# You should have received a copy of the GNU General Public License  
# along with this program; if not, write to the Free Software  
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301,
USA.  
#  
FROM ubuntu:16.04  
# Ensure packages are current, then install dependencies  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y vim procps wget libmnl0  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
ethtool \  
ibutils \  
ibverbs-utils \  
infiniband-diags \  
iproute2 \  
pciutils \  
libnl-route-3-200 \  
kmod \  
libmlx4-1 \  
libnuma1 \  
lsb-release \  
lsof \  
net-tools \  
open-iscsi \  
perftest \  
perl \  
python-libxml2 \  
rdmacm-utils \  
targetcli \  
tgt \  
wget && \  
rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update  
  
RUN apt-get install -y autoconf dpatch debhelper tcl chrpath autotools-dev
graphviz libgfortran3 automake flex pkg-config gfortran m4 swig tk bison
libltdl-dev  
  
# Set MOFED directory, image and working directory  
ENV MOFED_DIR MLNX_OFED_LINUX-4.2-1.0.0.0-ubuntu16.04-x86_64  
ENV MOFED_SITE_PLACE MLNX_OFED-4.2-1.0.0.0  
ENV MOFED_IMAGE MLNX_OFED_LINUX-4.2-1.0.0.0-ubuntu16.04-x86_64.tgz  
WORKDIR /tmp/  
  
# Download and install Mellanox OFED 4.2.1 for Ubuntu 16.04  
RUN wget http://content.mellanox.com/ofed/${MOFED_SITE_PLACE}/${MOFED_IMAGE}
&& \  
tar -xzvf ${MOFED_IMAGE}  
RUN ${MOFED_DIR}/mlnxofedinstall --user-space-only --force --without-fw-update
--all -q && \  
cd .. && \  
rm -rf ${MOFED_DIR} && \  
rm -rf *.tgz  

