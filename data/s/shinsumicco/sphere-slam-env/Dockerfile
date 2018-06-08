FROM ubuntu:16.04  
ENV CPATH=/usr/local/include:${CPATH}  
ENV LIBRARY_PATH=/usr/local/lib:${LIBRARY_PATH}  
ENV LD_LIBRARY_PATH=/usr/local/lib:${LD_LIBRARY_PATH}  
  
RUN \  
apt update -y && apt update -y  
RUN \  
apt install -y \  
build-essential \  
pkg-config \  
cmake \  
git \  
wget \  
unzip  
RUN \  
apt install -y \  
libboost-all-dev \  
ffmpeg \  
libavcodec-dev \  
libavformat-dev \  
libavutil-dev \  
libswscale-dev \  
libavresample-dev  
RUN \  
apt install -y \  
libgoogle-glog-dev \  
libgflags-dev \  
libatlas-base-dev \  
libsuitesparse-dev  
RUN \  
apt install -y \  
libyaml-cpp-dev  
  
# Eigen  
WORKDIR /tmp  
RUN wget http://bitbucket.org/eigen/eigen/get/3.3.4.tar.bz2 && tar -xf
3.3.4.tar.bz2  
WORKDIR /tmp/eigen-eigen-5a0156e40feb  
RUN mkdir build  
WORKDIR /tmp/eigen-eigen-5a0156e40feb/build  
RUN \  
cmake \  
-DCMAKE_BUILD_TYPE=Release \  
-DCMAKE_INSTALL_PREFIX=/usr/local \  
-DCMAKE_CXX_FLAGS=-std=c++11 \  
..  
RUN make -j"$(nproc)" && make install  
  
# Install Ceres from source  
WORKDIR /tmp  
RUN wget http://ceres-solver.org/ceres-solver-1.13.0.tar.gz && tar xvzf ceres-
solver-1.13.0.tar.gz  
WORKDIR /tmp/ceres-solver-1.13.0 && \  
RUN mkdir build  
WORKDIR /tmp/ceres-solver-1.13.0/build  
RUN \  
cmake \  
-DCMAKE_BUILD_TYPE=Release \  
-DCMAKE_INSTALL_PREFIX=/usr/local \  
-DCXX11=YES \  
-DBUILD_EXAMPLES=NO \  
-DBUILD_TESTING=NO \  
..  
RUN make -j"$(nproc)" && make install  
ENV Ceres_DIR /usr/local/lib/cmake/Ceres  
  
# opengv  
WORKDIR /tmp  
RUN git clone https://github.com/shinsumicco/opengv  
WORKDIR /tmp/opengv  
RUN mkdir build  
WORKDIR /tmp/opengv/build  
RUN \  
cmake \  
-DCMAKE_BUILD_TYPE=Release \  
-DCMAKE_INSTALL_PREFIX=/usr/local \  
-DCMAKE_CXX_FLAGS=-std=c++11 \  
-DBUILD_SHARED_LIBS=ON \  
-DBUILD_TESTS=OFF \  
..  
RUN make -j"$(nproc)" && make install  
ENV opengv_DIR=/usr/local/lib/cmake/opengv  
  
# OpenCV  
WORKDIR /tmp  
RUN wget https://github.com/opencv/opencv/archive/3.4.0.zip -O
opencv-3.4.0.zip && unzip opencv-3.4.0.zip  
WORKDIR /tmp/opencv-3.4.0  
RUN mkdir build  
WORKDIR /tmp/opencv-3.4.0/build  
RUN \  
cmake \  
-DCMAKE_BUILD_TYPE=Release \  
-DCMAKE_INSTALL_PREFIX=/usr/local \  
-DCMAKE_CXX_FLAGS=-std=c++11 \  
-DWITH_FFMPEG=YES \  
-DWITH_OPENMP=YES \  
-DWITH_EIGEN=YES \  
-DBUILD_PERF_TESTS=NO \  
-DBUILD_TESTS=NO \  
-DBUILD_opencv_objdetect=OFF \  
-DBUILD_opencv_dnn=OFF \  
-DBUILD_opencv_stitching=OFF \  
..  
RUN make -j"$(nproc)" && make install  
ENV OpenCV_DIR=/usr/local/share/OpenCV  
  
# Cleaning  
WORKDIR /tmp  
RUN rm -rf *  
RUN apt autoremove  
RUN rm -rf /var/lib/apt/lists/*  
  
WORKDIR /  
CMD ["/bin/bash"]  

