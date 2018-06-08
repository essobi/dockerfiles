FROM ubuntu:precise  
RUN apt-get update  
RUN apt-get install -y python-software-properties  
RUN add-apt-repository -y ppa:ubuntu-toolchain-r/test  
RUN add-apt-repository -y ppa:kalakris/cmake  
RUN apt-get update  
RUN for package in busybox-initramfs dmsetup initramfs-tools initscripts
plymouth udev; do echo "$package hold"; done | dpkg --set-selections  
RUN apt-get upgrade -y  
RUN apt-get install -y build-essential ccache git gcc-4.8 g++-4.8 cmake
zlib1g-dev libboost1.48-dev libboost-filesystem1.48-dev libboost-program-
options1.48-dev libboost-system1.48-dev libboost-thread1.48-dev libpcap-dev
libpcre3-dev libssl-dev libreadline-dev debhelper devscripts buildbot-slave
valgrind  
WORKDIR /data  
CMD buildslave start && tail -f twistd.log  

