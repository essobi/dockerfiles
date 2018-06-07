FROM ubuntu:xenial  
  
MAINTAINER alljoynsville  
  
RUN apt-get update && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install less sudo wget vim python build-essential subversion
libncurses5-dev unzip cmake \  
zlib1g-dev gawk gcc-multilib flex git-core gettext libssl-dev && \  
apt-get clean && \  
useradd -m builder && \  
echo 'builder ALL=NOPASSWD: ALL' > /etc/sudoers.d/builder && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
USER builder  
WORKDIR /home/builder  
CMD ["/bin/bash"]  

