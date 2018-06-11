FROM nvidia/cuda:9.0-cudnn7-runtime-ubuntu16.04  
  
MAINTAINER yummy.bian@gmail.com  
  
ENV OPENCV_DIR /opt/opencv  
ENV CUDNN_VERSION 7  
ENV OPENCV_VERSION=3.4.0  
LABEL com.nvidia.cudnn.version="${CUDNN_VERSION}"  
# build and install opencv  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
ca-certificates \  
wget \  
libopencv-dev \  
cmake \  
g++ \  
unzip \  
x264 \  
curl \  
git ;\  
mkdir -p /src && \  
cd /src && \  
mkdir -p $OPENCV_DIR && \  
wget https://github.com/opencv/opencv/archive/$OPENCV_VERSION.zip && \  
unzip $OPENCV_VERSION.zip && \  
mv /src/opencv-$OPENCV_VERSION/ $OPENCV_DIR/ && \  
rm -rf /src/$OPENCV_VERSION.zip && \  
wget https://github.com/opencv/opencv_contrib/archive/$OPENCV_VERSION.zip -O
$OPENCV_VERSION-contrib.zip && \  
unzip $OPENCV_VERSION-contrib.zip && \  
mv /src/opencv_contrib-$OPENCV_VERSION $OPENCV_DIR/ && \  
rm -rf /src/$OPENCV_VERSION-contrib.zip && \  
mkdir -p $OPENCV_DIR/opencv-$OPENCV_VERSION/build && \  
cd $OPENCV_DIR/opencv-$OPENCV_VERSION/build && \  
cmake \  
-D CMAKE_BUILD_TYPE=RELEASE \  
-D CMAKE_INSTALL_PREFIX=/usr/local \  
-D INSTALL_PYTHON_EXAMPLES=ON \  
-D INSTALL_C_EXAMPLES=OFF \  
-D OPENCV_EXTRA_MODULES_PATH=/home/bxb/opencv/opencv_contrib-3.3.0/modules \  
-D PYTHON_EXECUTABLE=/usr/bin/python3 \  
-D BUILD_EXAMPLES=ON .. && \  
make -j4 && \  
make install && \  
ldconfig && \  
rm -rf $OPENCV_DIR ;\  
apt-get autoremove && apt-get autoclean ;\  
rm -rf /var/lib/apt/lists/*  

