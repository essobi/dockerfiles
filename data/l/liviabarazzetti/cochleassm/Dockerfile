FROM ubuntu:xenial  
#for ssh see https://docs.docker.com/engine/examples/running_ssh_service/  
RUN apt-get update && apt-get install -y \  
build-essential \  
bzip2 \  
ca-certificates \  
cmake \  
cmake-curses-gui \  
curl \  
expect \  
git \  
libhdf5-dev \  
libeigen3-dev \  
libboost-date-time-dev \  
libboost-dev \  
libboost-system-dev \  
libboost-thread-dev \  
libboost-filesystem-dev \  
libboost-program-options-dev \  
libglu1-mesa-dev \  
#libglib2.0-0 libxext6 libsm6 libxrender1 \  
libinsighttoolkit4-dev libpng12-dev libtiff5-dev \  
subversion\  
vim \  
wget \  
paraview paraview-dev paraview-python hdf5-tools h5utils python-pip \  
openssh-server && \  
apt-get clean && \  
mkdir /var/run/sshd && \  
echo 'root:screencast' | chpasswd && \  
sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes /'
/etc/ssh/sshd_config  
  
RUN pip install virtualenvwrapper scipy pyyaml jupyter  
  
  
  

