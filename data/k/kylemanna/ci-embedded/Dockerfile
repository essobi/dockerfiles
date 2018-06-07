#  
# Embedded ARM build environment for use with gitlab-ci-multi-runner  
#  
# Author: Kyle Manna <kyle[at]kylemanna[d0t]com>  
#  
#  
# Ubuntu is selected due to its long support life.  
#  
FROM ubuntu:16.04  
#  
# Ubuntu 16.04 seems to lag behind by a lot from embedded compilers currently
at v4.9.3  
#  
# Instead, install upstream release from PPA and associated signing key.  
#  
RUN \  
echo 'deb http://ppa.launchpad.net/team-gcc-arm-embedded/ppa/ubuntu xenial
main' > /etc/apt/sources.list.d/gcc-arm-embedded.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys D1FAA6ECF64D33B0 && \  
apt-get update && \  
apt-get install -y \  
build-essential \  
clang \  
cmake \  
curl \  
gcc \  
git \  
ninja-build gcc-arm-embedded \  
openssh-client \  
protobuf-compiler \  
python \  
python-protobuf \  
qemu-user \  
valgrind \  
&& \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  

