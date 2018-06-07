FROM dockcross/windows-x64 as opencvbuild  
  
WORKDIR /opt  
  
ENV OPENCV_VERSION 3.3.1  
ENV OPENCV_PREFIX /opt  
  
RUN apt-get update && \  
apt-get -y install \  
build-essential \  
cmake \  
git-core \  
unzip \  
libgtk2.0-dev \  
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
ADD https://github.com/opencv/opencv_contrib/archive/${OPENCV_VERSION}.zip
opencv_contrib-${OPENCV_VERSION}.zip  
  
# For local development of the image it is faster to copy locally. ADD is not
cached but COPY is.  
#COPY opencv-${OPENCV_VERSION}.zip opencv-${OPENCV_VERSION}.zip  
#COPY opencv_contrib-${OPENCV_VERSION}.zip
opencv_contrib-${OPENCV_VERSION}.zip  
RUN unzip -x opencv-${OPENCV_VERSION}.zip && \  
unzip -x opencv_contrib-${OPENCV_VERSION}.zip && \  
mkdir -p opencv-${OPENCV_VERSION}/build && \  
cd opencv-${OPENCV_VERSION}/build && \  
mkdir -p ${OPENCV_PREFIX}/opencv-static && \  
cmake \  
-DBUILD_SHARED_LIBS=OFF \   
-D CMAKE_BUILD_TYPE=Release \   
-DOPENCV_EXTRA_MODULES_PATH=/opt/opencv_contrib-${OPENCV_VERSION}/modules \   
-DCMAKE_INSTALL_PREFIX=${OPENCV_PREFIX}/opencv-static ../ && \   
make -j5 && \  
make install  
  
FROM dockcross/windows-x64  
WORKDIR /work  
ENV DEFAULT_DOCKCROSS_IMAGE buildenv  
ENV OPENCV_PREFIX /opt  
ENV PATH=$PATH:${OPENCV_PREFIX}/opencv-static/bin  
COPY \--from=opencvbuild /opt/opencv-static/ /opt/opencv-static/  

