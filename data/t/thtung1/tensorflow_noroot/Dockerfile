FROM tensorflow/tensorflow:1.8.0-devel-gpu  
MAINTAINER TRAN Hoang Tung <tran-hoang.tung@usth.edu.vn>  
  
WORKDIR /home  
  
ENV OPENCV_VERSION='3.4.1'  
# Install dependencies  
RUN \  
# Update Ubuntu source files  
apt-get update && \  
# You should never upgrade!!!  
# apt-get upgrade -y && \  
# Build tools  
apt-get install -y build-essential cmake curl && \  
# GUI  
apt-get install -y qt5-default libvtk6-dev && \  
# Media I/O  
apt-get install -y zlib1g-dev libjpeg-dev libwebp-dev libpng-dev libtiff5-dev
libjasper-dev libopenexr-dev libgdal-dev && \  
# Video I/O  
apt-get install -y libdc1394-22-dev libavcodec-dev libavformat-dev libswscale-
dev libtheora-dev libvorbis-dev libxvidcore-dev libx264-dev yasm libopencore-
amrnb-dev libopencore-amrwb-dev libv4l-dev libxine2-dev && \  
# Parallelism and linear algebra libraries  
apt-get install -y libtbb-dev libeigen3-dev && \  
# support to HDF5  
apt-get install -y libhdf5-dev && \  
# Python  
apt-get install -y python-dev python-tk python-numpy python3-dev python3-tk
python3-numpy && \  
# Java  
apt-get install -y ant default-jdk && \  
# Documentation:  
apt-get install -y doxygen && \  
# sudo  
apt-get install -y sudo && \  
# jupyterlab to manage python easily  
pip install jupyterlab && \  
# Cleanup  
apt-get autoclean && apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Download OpenCV and install  
RUN \  
# Download OpenCV and OpenCV-contrib  
mkdir -p opencv/build && \  
curl -L https://github.com/opencv/opencv/archive/${OPENCV_VERSION}.tar.gz |
tar xz -C opencv --strip-components 1 && \  
mkdir opencv_contrib && \  
curl -L
https://github.com/opencv/opencv_contrib/archive/${OPENCV_VERSION}.tar.gz |
tar xz -C opencv_contrib --strip-components 1 && \  
cd opencv/build && \  
cmake -D CMAKE_BUILD_TYPE=RELEASE \  
-D WITH_QT=ON \  
-D WITH_CUDA=OFF \  
-D WITH_OPENGL=ON \  
-D FORCE_VTK=ON \  
-D WITH_TBB=ON \  
-D WITH_GDAL=ON \  
-D WITH_XINE=ON \  
-D BUILD_EXAMPLES=ON \  
-D ENABLE_PRECOMPILED_HEADERS=OFF \  
-D BUILD_PERF_TESTS=OFF \  
-D BUILD_TESTS=OFF \  
-D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules/ .. && \  
make -j $(getconf _NPROCESSORS_ONLN) && \  
make install && \  
ldconfig  

