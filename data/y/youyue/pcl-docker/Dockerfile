#  
# pcl dockerfile  
# Author: Airsquire You Yue  
# Pull base image.  
FROM nvidia/cuda:8.0-devel  
  
# Install neccessary tools  
RUN apt-get update  
RUN apt-get install -y \  
software-properties-common \  
ca-certificates \  
wget  
RUN wget -O - http://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add -  
RUN apt-add-repository "deb http://apt.llvm.org/xenial/ llvm-toolchain-
xenial-4.0 main"  
RUN apt-get update  
RUN apt-get install -y \  
build-essential \  
g++ \  
python-dev \  
autotools-dev \  
libicu-dev \  
libbz2-dev \  
libboost-all-dev  
  
RUN apt-get install -y \  
mc \  
lynx \  
libqhull* \  
pkg-config \  
libxmu-dev \  
libxi-dev \  
\--no-install-recommends --fix-missing  
  
RUN apt-get install -y \  
mesa-common-dev \  
cmake \  
git \  
mercurial \  
freeglut3-dev \  
libflann-dev \  
\--no-install-recommends --fix-missing  
  
RUN apt-get autoremove  
  
# Install Eigen  
RUN cd /opt && hg clone -r 3.2 https://bitbucket.org/eigen/eigen eigen  
RUN mkdir -p /opt/eigen/build  
RUN cd /opt/eigen/build && cmake ..  
RUN cd /opt/eigen/build && make install  
  
# Install VTK  
RUN cd /opt && git clone git://vtk.org/VTK.git VTK  
RUN cd /opt/VTK && git checkout tags/v8.0.0  
RUN cd /opt/VTK && mkdir build  
RUN cd /opt/VTK/build && cmake -DCMAKE_BUILD_TYPE:STRING=Release -D
VTK_RENDERING_BACKEND=OpenGL ..  
RUN cd /opt/VTK/build && make -j 32 && make install  
  
# Install PCL  
RUN cd /opt && git clone https://github.com/Airsquire/pcl pcl  
RUN cd /opt/pcl && git checkout master  
RUN mkdir -p /opt/pcl/build  
RUN cd /opt/pcl/build && cmake -D WITH_CUDA=true -D BUILD_GPU=true -D
BUILD_visualization=true -D BUILD_CUDA=true -D VTK_DIR=/opt/VTK/build -D
BUILD_2d=true ..  
RUN cd /opt/pcl/build && make -j 32 && make install  
RUN cd /opt/pcl/build && make clean  

