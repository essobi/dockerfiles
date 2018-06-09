FROM ubuntu:16.04  
MAINTAINER tonka3000 <tonka3100@gmail.com>  
  
WORKDIR "/project"  
  
RUN apt-get update && \  
apt-get dist-upgrade -y && \  
apt-get install build-essential git-core wget python python3 python3-pip
cppcheck libx11-dev vim -y && \  
apt-get install mesa-common-dev libxt-dev libxmu-dev libxi-dev libgl1-mesa-dev
libglu1-mesa-dev -y && \  
# libs for conan  
apt-get install libssl-dev libffi6 libffi-dev -y && \  
apt-get clean autoclean && \  
apt-get autoremove -y && \  
wget https://cmake.org/files/v3.10/cmake-3.10.2-Linux-x86_64.sh && \  
chmod +x cmake-3.10.2-Linux-x86_64.sh && \  
./cmake-3.10.2-Linux-x86_64.sh \--skip-license --prefix=/usr && \  
rm cmake-3.10.2-Linux-x86_64.sh && \  
wget https://github.com/conan-io/conan/releases/download/1.2.1/conan-
ubuntu-64_1_2_1.deb && \  
dpkg -i conan-ubuntu-64_1_2_1.deb && \  
rm conan-ubuntu-64_1_2_1.deb && \  
conan user && \  
pip3 install conan_package_tools  
  
RUN cmake --version && \  
conan --version && \  
g++ --version

