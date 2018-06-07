FROM ubuntu:xenial  
  
RUN apt-get update \  
&& apt-get install -y \  
build-essential \  
checkinstall \  
cmake \  
pkg-config \  
yasm \  
gfortran \  
git \  
libjpeg8-dev \  
libjasper-dev \  
libpng12-dev \  
libtiff5-dev \  
libavcodec-dev \  
libavformat-dev \  
libswscale-dev \  
libdc1394-22-dev \  
libxine2-dev \  
libv4l-dev \  
libgstreamer0.10-dev \  
libgstreamer-plugins-base0.10-dev \  
libqt4-dev \  
libgtk2.0-dev \  
libtbb-dev \  
libatlas-base-dev \  
libfaac-dev \  
libmp3lame-dev \  
libtheora-dev \  
libvorbis-dev \  
libxvidcore-dev \  
libopencore-amrnb-dev \  
libopencore-amrwb-dev \  
x264 \  
v4l-utils \  
libgphoto2-dev \  
libeigen3-dev \  
libhdf5-dev \  
doxygen \  
&& mkdir -p /src \  
&& cd /src \  
&& git clone https://github.com/opencv/opencv.git \  
&& git clone https://github.com/opencv/opencv_contrib.git \  
&& cd opencv_contrib \  
&& git checkout 3.3.0 \  
&& cd ../opencv \  
&& git checkout 3.3.0 \  
&& mkdir -p build \  
&& cd build \  
&& cmake -D CMAKE_BUILD_TYPE=RELEASE \  
-D CMAKE_INSTALL_PREFIX=/usr/local \  
-D INSTALL_C_EXAMPLES=ON \  
-D INSTALL_PYTHON_EXAMPLES=ON \  
-D WITH_TBB=ON \  
-D WITH_V4L=ON \  
-D WITH_QT=ON \  
-D WITH_OPENGL=ON \  
-D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules \  
-D BUILD_EXAMPLES=ON .. \  
&& make -j4 \  
&& make install \  
&& sh -c 'echo "/usr/local/lib" >> /etc/ld.so.conf.d/opencv.conf' \  
&& ldconfig \  
&& rm -rf /src  

