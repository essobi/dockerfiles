FROM ubuntu:16.04  
  
MAINTAINER Alexander Onbysh <onbysh.a@gmail.com>  
  
# Pick up some TF dependencies  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
cmake \  
curl \  
wget \  
libfreetype6-dev \  
libpng12-dev \  
libzmq3-dev \  
pkg-config \  
python3.5 \  
python3.5-dev \  
python3-pip \  
python3-tk \  
rsync \  
software-properties-common \  
unzip \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN pip3 install setuptools  
  
RUN pip3 install --upgrade pip && pip3 --no-cache-dir install \  
setuptools \  
matplotlib \  
numpy \  
scipy \  
sklearn \  
pandas \  
Pillow \  
tensorflow  
  
WORKDIR /  
RUN wget https://github.com/Itseez/opencv/archive/3.2.0.zip \  
&& unzip 3.2.0.zip \  
&& mkdir /opencv-3.2.0/cmake_binary \  
&& cd /opencv-3.2.0/cmake_binary \  
&& cmake -DBUILD_TIFF=ON \  
-DBUILD_opencv_java=OFF \  
-DWITH_CUDA=OFF \  
-DENABLE_AVX=ON \  
-DWITH_OPENGL=ON \  
-DWITH_OPENCL=ON \  
-DWITH_IPP=ON \  
-DWITH_TBB=ON \  
-DWITH_EIGEN=ON \  
-DWITH_V4L=ON \  
-DBUILD_TESTS=OFF \  
-DBUILD_PERF_TESTS=OFF \  
-DCMAKE_BUILD_TYPE=RELEASE \  
-DCMAKE_INSTALL_PREFIX=$(python3.5 -c "import sys; print(sys.prefix)") \  
-DPYTHON_EXECUTABLE=$(which python3.5) \  
-DPYTHON_INCLUDE_DIR=$(python3.5 -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())") \  
-DPYTHON_PACKAGES_PATH=$(python3.5 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())") .. \  
&& make install \  
&& rm /3.2.0.zip \  
&& rm -r /opencv-3.2.0  
  
EXPOSE 6006  
  
RUN mkdir -p /root/logs  
  
WORKDIR "/root"  
CMD tensorboard --logdir=/root/logs &  
CMD ["/bin/bash"]  

