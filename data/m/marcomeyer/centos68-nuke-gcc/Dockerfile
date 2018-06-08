# Nuke gcc build environment  
FROM centos:6.8  
RUN yum -y install wget curl cmake unzip zlib-devel mesa-libGLU-devel  
RUN wget -O /etc/yum.repos.d/slc6-devtoolset.repo
http://linuxsoft.cern.ch/cern/devtoolset/slc6-devtoolset.repo  
RUN yum -y install devtoolset-2-binutils devtoolset-2-gcc devtoolset-2-gcc-c++
--nogpgcheck

