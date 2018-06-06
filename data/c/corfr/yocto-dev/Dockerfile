FROM ubuntu:14.04  
## Mirror  
RUN sed -i
"s^http://archive.ubuntu.com/ubuntu^http://mirror.it.ubc.ca/ubuntu^g"
/etc/apt/sources.list  
  
RUN ( \  
apt-get update && \  
apt-get --yes \--assume-yes install -y \  
gawk wget git-core diffstat unzip texinfo gcc-multilib \  
build-essential chrpath socat python-git python-jinja2 \  
git subversion libsdl-dev \  
diffstat texinfo gawk chrpath wget cpio \  
vim icecc bash ninja-build screen sshpass \  
bc unzip libxml2-utils autoconf openjdk-7-jdk lbzip2 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
ln -sf /bin/bash /bin/sh \  
)  
  
## UTF8 support  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  

