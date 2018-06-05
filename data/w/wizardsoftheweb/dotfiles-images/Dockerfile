FROM fedora:27  
  
LABEL version=0.0.2  
  
RUN dnf update -y  
  
RUN dnf install -y \  
sudo \  
git \  
python2 \  
python-pip \  
python-devel  
  
RUN dnf install -y \  
gcc \  
gcc-c++ \  
automake \  
autoconf \  
cmake \  
pkg-config \  
openssh \  
libssh \  
libssh2 \  
libssh2-devel \  
openssl \  
openssl-devel \  
libgit2 \  
libgit2-devel \  
akmods \  
util-linux-user \  
libselinux-python  
  
RUN pip install ansible  
  
CMD ["/usr/sbin/init"]  

