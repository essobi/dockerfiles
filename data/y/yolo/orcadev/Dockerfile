FROM centos:5  
RUN yum install -y git vim nano make gcc-c++ gdb wget libidn.x86_64 patch  
RUN wget --no-check-certificate
https://cmake.org/files/v3.4/cmake-3.4.0-Linux-x86_64.sh \--output-document
/dev/shm/cmake-installer.sh && \  
sh /dev/shm/cmake-installer.sh \--prefix=/usr/local --exclude-subdir  

