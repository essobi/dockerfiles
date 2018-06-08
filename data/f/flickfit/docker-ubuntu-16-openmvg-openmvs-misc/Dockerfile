FROM ubuntu:16.04  
  
MAINTAINER John Wu <john.wu@mail.mcgill.ca>  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
# Install Dependencies  
RUN apt-get update && \  
apt-get install -y \--no-install-recommends git && \  
apt-get install -y \--no-install-recommends make cmake build-essential && \  
apt-get install -y \--no-install-recommends nodejs nodejs-legacy npm && \  
apt-get install -y \--no-install-recommends apt-utils && \  
apt-get install -y \--no-install-recommends libpcl-dev && \  
apt-get install -y \--no-install-recommends libopencv-dev && \  
apt-get install -y \--no-install-recommends libboost-all-dev && \  
apt-get install -y \--no-install-recommends libproj-dev && \  
apt-get install -y \--no-install-recommends xvfb && \  
apt-get install -y \--no-install-recommends libpng-dev && \  
apt-get install -y \--no-install-recommends libjpeg-dev && \  
apt-get install -y \--no-install-recommends libtiff-dev && \  
apt-get install -y \--no-install-recommends libxxf86vm1 && \  
apt-get install -y \--no-install-recommends libxxf86vm-dev && \  
apt-get install -y \--no-install-recommends libxi-dev && \  
apt-get install -y \--no-install-recommends libxrandr-dev && \  
apt-get install -y \--no-install-recommends mercurial && \  
apt-get install -y \--no-install-recommends libglu1-mesa-dev && \  
apt-get install -y \--no-install-recommends libboost-iostreams-dev libboost-
program-options-dev libboost-system-dev libboost-serialization-dev && \  
apt-get install -y \--no-install-recommends libcgal-dev libcgal-qt5-dev && \  
apt-get install -y \--no-install-recommends libatlas-base-dev libsuitesparse-
dev && \  
apt-get clean && \  
rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/* && \  
  
# Install libaries  
mkdir build && cd build && \  
# Store build folder path in a variable  
build_folder_path=`pwd` && \  
# OpenMVG  
git clone --recursive https://github.com/openMVG/openMVG.git openMVG && \  
cd openMVG && \  
mkdir build && cd build && \  
cmake -DCMAKE_BUILD_TYPE=RELEASE . ../src && \  
make && \  
cd ../../ && \  
# Eigen  
hg clone https://bitbucket.org/eigen/eigen#3.2 eigen && cd eigen && \  
mkdir build && cd build && \  
cmake -DCMAKE_BUILD_TYPE=RELEASE . ../ && \  
make && make install && \  
cd ../../ && \  
# Ceres  
git clone https://ceres-solver.googlesource.com/ceres-solver ceres-solver &&
cd ceres-solver && \  
mkdir build && cd build && \  
cmake . ../ -DMINIGLOG=ON -DBUILD_TESTING=OFF -DBUILD_EXAMPLES=OFF && \  
make && make install && \  
cd ../../ && \  
# VCGLib  
git clone https://github.com/cdcseacave/VCG.git vcglib && \  
# OpenMVS  
git clone https://github.com/cdcseacave/openMVS.git openMVS && cd openMVS &&\  
mkdir release && cd release && \  
cmake . ../ -DCMAKE_BUILD_TYPE=Release -DVCG_DIR="$build_folder_path/vcglib"
&& \  
make && \  
cd ../../  

