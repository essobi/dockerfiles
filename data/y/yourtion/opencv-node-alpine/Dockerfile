FROM node:6-alpine  
  
#2 Add Edge and bleeding repos  
# add the edge repositories  
RUN echo "@edge-testing http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
echo "@edge-community http://dl-cdn.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories  
  
ENV OPENCV_VERSION 3.2.0  
  
#3 update apk, install dependencies, build opencv, cleanup  
RUN apk update \  
&& apk upgrade \  
&& apk add --no-cache \  
build-base \  
clang \  
clang-dev \  
cmake \  
git \  
pkgconf \  
wget \  
libtbb@edge-testing \  
libtbb-dev@edge-testing \  
libjpeg \  
libjpeg-turbo-dev \  
libpng \  
libpng-dev \  
libwebp \  
libwebp-dev \  
tiff \  
tiff-dev \  
libjasper \  
jasper-dev \  
python \  
python-dev \  
py-numpy@edge-community \  
py-numpy-dev@edge-community \  
linux-headers\  
&& cd /tmp \  
&& wget -O opencv-$OPENCV_VERSION.tar.gz
https://github.com/opencv/opencv/archive/$OPENCV_VERSION.tar.gz \  
&& tar -xzf opencv-$OPENCV_VERSION.tar.gz \  
&& cd /tmp/opencv-$OPENCV_VERSION \  
&& mkdir build \  
&& cd build \  
&& CC=/usr/bin/clang CXX=/usr/bin/clang++ cmake \  
-D CMAKE_BUILD_TYPE=RELEASE \  
-D CMAKE_INSTALL_PREFIX=/usr \  
-D WITH_FFMPEG=NO \  
-D WITH_IPP=NO \  
-D WITH_OPENEXR=NO \  
-D WITH_TBB=YES \  
-D WITH_1394=NO \  
-D BUILD_PERF_TESTS=OFF \  
-D BUILD_TESTS=OFF .. \  
&& make -j2 \  
&& make install \  
&& cd / \  
&& rm -rf /tmp/opencv-$OPENCV_VERSION* /tmp/opencv_contrib-$OPENCV_VERSION* \  
&& apk del \  
build-base \  
clang \  
clang-dev \  
cmake \  
git \  
pkgconf \  
wget \  
libtbb-dev \  
libjpeg-turbo-dev \  
libpng-dev \  
tiff-dev \  
jasper-dev \  
python-dev \  
py-numpy-dev  

