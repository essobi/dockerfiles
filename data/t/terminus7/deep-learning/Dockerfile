FROM terminus7/gpu-py2-th-kr  
  
MAINTAINER Luis Mesas <luis.mesas@intelygenz.com>  
  
ARG OPENCV_VERSION=3.2.0-rc  
ARG CUDA_ARCHITECTURE="3.0"  
# required packages  
RUN apt-get update && \  
apt-get install -y build-essential cmake pkg-config libgtk2.0-dev libjpeg-dev
libpng-dev unzip && \  
apt-get clean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# rm -rf /var/lib/{apt,dpkg,cache,log}/ /tmp/* /var/tmp/*  
# OpenCV  
RUN curl -L https://github.com/opencv/opencv/archive/${OPENCV_VERSION}.zip -o
opencv.zip && \  
unzip opencv.zip && \  
rm opencv.zip && \  
mkdir opencv-${OPENCV_VERSION}/release && \  
cd opencv-${OPENCV_VERSION}/release && \  
cmake \  
-D WITH_CUDA=ON \  
-D CUDA_ARCH_BIN=${CUDA_ARCHITECTURE} \  
-D CUDA_ARCH_PTX="" \  
-D CUDA_FAST_MATH=ON \  
-D CMAKE_BUILD_TYPE=RELEASE \  
-D BUILD_TESTS=OFF \  
-D BUILD_PERF_TESTS=OFF \  
-D BUILD_EXAMPLES=OFF \  
-D CMAKE_INSTALL_PREFIX=/usr/local .. && \  
make -j2 && \  
make install && \  
cd ../.. && \  
rm -rf opencv*  
  
ENV LD_LIBRARY_PATH /usr/lib/x86_64-linux-gnu:${LD_LIBRARY_PATH}  
ENV LIBRARY_PATH /usr/lib/x86_64-linux-gnu:${LIBRARY_PATH}  
  
WORKDIR "/root"  
CMD ["/bin/bash"]  

