FROM nownabe/python3  
MAINTAINER nownabe <nownabe@gmail.com>  
  
ENV OPENCV_VERSION 3.1.0  
  
RUN apk update --no-cache \  
&& apk add --no-cache libstdc++ \  
&& apk add --no-cache --virtual .build-deps \  
curl \  
make \  
cmake \  
gcc \  
g++ \  
pkgconf \  
linux-headers \  
&& ln -s /usr/include/locale.h /usr/include/xlocale.h \  
&& pip install numpy \  
&& curl -sLS -o opencv.zip
https://github.com/opencv/opencv/archive/${OPENCV_VERSION}.zip \  
&& unzip -d /usr/src opencv.zip \  
&& rm opencv.zip \  
&& mkdir /usr/src/opencv-${OPENCV_VERSION}/build \  
&& cd /usr/src/opencv-${OPENCV_VERSION}/build \  
  
# https://github.com/opencv/opencv/blob/master/CMakeLists.txt  
&& cmake \  
# optional 3rd party components  
-D WITH_FFMPEG=NO \  
-D WITH_IPP=NO \  
-D WITH_OPENEXR=NO \  
  
# OpenCV build components  
-D BUILD_TESTS=NO \  
-D BUILD_PERF_TESTS=NO \  
# 3rd party libs  
-D BUILD_TIFF=YES \  
  
# OpenCV installation options  
# OpenCV build options  
  
# Others  
-D BUILD_opencv_java=NO \  
-D CMAKE_BUILD_TYPE=RELEASE \  
-D CMAKE_INSTALL_PREFIX=/usr/local \  
-D PYTHON_EXECUTABLE=/usr/local/bin/python \  
  
.. \  
&& make -j $(getconf _NPROCESSORS_ONLN) \  
&& make install \  
&& apk del .build-deps \  
&& rm -r /usr/src/opencv-${OPENCV_VERSION} ~/.cache /var/cache/apk/*  

