FROM dockcross/linux-armv7 as buildenv  
  
WORKDIR /opt  
  
ENV OPENCV_VERSION 3.3.1  
ENV OPENCV_PREFIX /opt  
  
RUN apt-get update && \  
apt-get -y install \  
cmake \  
git-core \  
unzip \  
libtbb2 \  
libtbb-dev \  
libjpeg-dev \  
libpng-dev \  
libtiff-dev \  
libjasper-dev \  
pkg-config \  
libavcodec-dev \  
libavformat-dev \  
libswscale-dev  
  
ADD https://codeload.github.com/opencv/opencv/zip/${OPENCV_VERSION}
opencv-${OPENCV_VERSION}.zip  
  
RUN unzip -x opencv-${OPENCV_VERSION}.zip && \  
mkdir -p opencv-${OPENCV_VERSION}/build && \  
cd opencv-${OPENCV_VERSION}/build && \  
mkdir -p ${OPENCV_PREFIX}/opencv-static && \  
cmake \  
-DBUILD_SHARED_LIBS=OFF \  
-DCMAKE_INSTALL_PREFIX=${OPENCV_PREFIX}/opencv-static ../ && \  
make install  
  
FROM dockcross/linux-armv7  
WORKDIR /opt  
ENV OPENCV_PREFIX /opt  
ENV PATH=$PATH:${OPENCV_PREFIX}/opencv-static/bin  
  
COPY \--from=buildenv /opt/opencv-static/ opencv-static/  

