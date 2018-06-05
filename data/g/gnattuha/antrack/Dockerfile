# Pull base image.  
FROM ubuntu:14.04.4  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -yq install
software-properties-common  
RUN add-apt-repository -y ppa:ubuntu-toolchain-r/test  
RUN apt-get update && apt-get install -yq g++-4.9 gcc-4.9  
RUN ln -s gcc-4.9 gcc  
RUN ln -s g++-4.9 g++  
# Install.  
RUN apt-get update && apt-get install -yq libopencv-dev liblapack-dev libblas-
dev libboost-dev libarmadillo-dev libboost-all-dev libgoogle-glog-dev cmake
unzip build-essential wget git  
  
# install gflags  
RUN wget --no-check-certificate
https://github.com/schuhschuh/gflags/archive/master.zip && unzip master.zip  
WORKDIR gflags-master  
RUN mkdir build && cd build && export CXXFLAGS="-fPIC" && cmake .. && make
VERBOSE=1 && make install && cd ../..  
  
ADD ./src/ /Antrack/src/  
ADD CMakeLists.txt /Antrack/CMakeLists.txt  
ADD ./lib/ /Antrack/lib/  
  
# RUN git clone https://github.com/ibogun/Antrack.git  
# WORKDIR Antrack  
RUN cd /Antrack/ && mkdir build && cd build && cmake
-DCMAKE_CXX_COMPILER=g++-4.9 -DCMAKE_C_COMPILER=gcc-4.9 -Dtest=ON .. && make
&& ./bin/RunUnitTests  
  
# Define default command.  
CMD ["bash"]

