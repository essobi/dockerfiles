############################################################  
# Dockerfile to bulid container images containing the requirements for
mandelbulber2  
# Based on Ubuntu  
############################################################  
  
FROM ubuntu:zesty  
MAINTAINER Martin F. acidhunter <npanic@kmpt.nz>  
  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y build-essential && \  
apt-get install -y software-properties-common openssh-client rsync && \  
apt-add-repository -y ppa:ubuntu-toolchain-r/test && \  
add-apt-repository -y ppa:ubuntu-sdk-team/ppa  
RUN \  
apt-get update && \  
apt-get install -y libncurses5-dev libglib2.0-dev libgeoip-dev
libtokyocabinet-dev zlib1g-dev libncursesw5-dev libbz2-dev && \  
apt-get install -y \  
curl \  
g++-6 \  
libc6-i386 \  
mesa-common-dev \  
libgl1-mesa-dev \  
qtbase5-dev \  
qt5-qmake \  
qtbase5-dev-tools \  
qt5-style-plugins \  
qt5-default \  
qtmultimedia5-dev \  
qttools5-dev-tools \  
qttools5-dev \  
libpng-dev \  
libgsl0-dev \  
libgsl2 \  
libgomp1 \  
liblzo2-2 \  
liblzo2-dev \  
libtiff5 \  
libsndfile1-dev \  
libqt5gui5 \  
libpng16-16 \  
libqt5multimedia5 \  
libqt5multimedia5-plugins \  
extra-cmake-modules  
  
RUN \  
update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-6 100 && \  
update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-6 100 && \  
update-alternatives --set g++ /usr/bin/g++-6 && \  
update-alternatives --set gcc /usr/bin/gcc-6  
  
ENV HOME /root  
WORKDIR /root  
CMD ["bash"]  

