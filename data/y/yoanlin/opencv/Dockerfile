FROM debian:jessie  
MAINTAINER Yo-An Lin <yoanlin93@gmail.com>  
  
ENV LC_ALL=C.UTF-8  
ENV LANG=C.UTF-8  
  
ARG AVX=ON  
ARG AVX2=ON  
ARG SSE41=ON  
ARG SSE42=ON  
ARG CUDA=OFF  
ARG OPENCL=OFF  
ARG OPENCL_SVM=OFF  
ARG OPENGL=ON  
ARG VERSION=3.3.0  
ARG GTK=OFF  
ARG QT=OFF  
  
# Intel Threading Building Blocks  
ARG TBB=ON  
  
RUN apt-get update && \  
apt-get install -y \  
build-essential \  
cmake \  
git \  
wget \  
unzip \  
yasm \  
pkg-config \  
libswscale-dev \  
libeigen3-dev \  
libtbb2 \  
libtbb-dev \  
libjpeg-dev \  
libpng-dev \  
libtiff-dev \  
libjasper-dev \  
libavformat-dev \  
libpq-dev \  
libboost-all-dev \  
&& apt-get clean  
  
WORKDIR /  
RUN wget https://github.com/opencv/opencv/archive/$VERSION.tar.gz  
RUN tar xzf $VERSION.tar.gz  
RUN mkdir -p /opencv-$VERSION/cmake_binary \  
&& ls \  
&& (cd /opencv-$VERSION/cmake_binary \  
&& cmake \  
-DBUILD_TIFF=ON \  
-DBUILD_opencv_java=OFF \  
-DCMAKE_BUILD_TYPE=RELEASE \  
-DWITH_CUDA=$CUDA \  
-DENABLE_AVX=$AVX \  
-DENABLE_AVX2=$AVX2 \  
-DENABLE_SSE41=$SSE41 \  
-DENABLE_SSE42=$SSE42 \  
-DENABLE_SSSE3=ON \  
-DWITH_OPENGL=$OPENGL \  
-DWITH_GTK=$GTK \  
-DWITH_QT=$QT \  
-DWITH_OPENCL=$OPENCL \  
-DWITH_OPENCL_SVM=$OPENCL_SVM \  
-DWITH_JPEG=ON \  
-DWITH_WEBP=ON \  
-DWITH_PNG=ON \  
-DWITH_IPP=ON \  
-DWITH_TBB=$TBB \  
-DWITH_EIGEN=ON \  
-DWITH_V4L=ON \  
-DWITH_FFMPEG=ON \  
-DENABLE_PRECOMPILED_HEADERS=ON \  
-DBUILD_PERF_TESTS=OFF \  
-DBUILD_TESTS=OFF \  
-DINSTALL_C_EXAMPLES=OFF \  
.. && make install ) \  
&& rm -rf $VERSION.tar.gz /opencv-$VERSION  

