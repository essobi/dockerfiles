FROM nvidia/cuda:8.0-cudnn6-devel-ubuntu16.04  
  
LABEL maintainer="kamil.bobrowski@gmail.com"  
  
ARG OPENCV_VERSION=3.3.1  
ARG TENSORFLOW_VERSION=1.3.0  
ARG
PYTORCH_LINK='http://download.pytorch.org/whl/cu80/torch-0.2.0.post3-cp35-cp35m-manylinux1_x86_64.whl'  
  
WORKDIR /  
  
# tensorflow dependencies  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
curl \  
libfreetype6-dev \  
libpng12-dev \  
libzmq3-dev \  
pkg-config \  
python3 \  
python3-dev \  
rsync \  
software-properties-common \  
unzip \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# pip  
#RUN curl -O https://bootstrap.pypa.io/get-pip.py && \  
# python3 get-pip.py && \  
# rm get-pip.py  
RUN apt-get update && apt-get install -y \  
python-pip python3-pip \  
&& pip2 install --upgrade pip \  
&& pip3 install --upgrade pip  
  
# tensorflow python dependencies  
RUN pip3 --no-cache-dir install \  
Pillow \  
h5py \  
ipykernel \  
jupyter \  
matplotlib \  
numpy \  
pandas \  
scipy \  
sklearn \  
&& \  
python3 -m ipykernel.kernelspec  
  
# tensorflow  
RUN pip3 --no-cache-dir install \  
https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-${TENSORFLOW_VERSION}-cp35-cp35m-linux_x86_64.whl  
  
# For CUDA profiling, TensorFlow requires CUPTI.  
ENV LD_LIBRARY_PATH /usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH  
  
# OpenCV dependencies  
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
libtbb2 \  
libtbb-dev \  
libjpeg-dev \  
libpng-dev \  
libtiff-dev \  
libjasper-dev \  
libavformat-dev \  
libpq-dev \  
libgtk2.0-dev \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# OpenCV compilation  
RUN wget https://github.com/opencv/opencv/archive/${OPENCV_VERSION}.zip \  
&& unzip ${OPENCV_VERSION}.zip \  
&& mkdir /opencv-${OPENCV_VERSION}/cmake_binary \  
&& cd /opencv-${OPENCV_VERSION}/cmake_binary \  
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
-DWITH_GTK=ON \  
-DWITH_GTK_2_X=ON \  
-DBUILD_TESTS=OFF \  
-DBUILD_PERF_TESTS=OFF \  
-DCMAKE_BUILD_TYPE=RELEASE \  
-DCMAKE_INSTALL_PREFIX=$(python3 -c "import sys; print(sys.prefix)") \  
-DPYTHON_EXECUTABLE=$(which python3) \  
-DPYTHON_INCLUDE_DIR=$(python3 -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())") \  
-DPYTHON_PACKAGES_PATH=$(python3 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())") .. \  
&& make install \  
&& rm /${OPENCV_VERSION}.zip \  
&& rm -r /opencv-${OPENCV_VERSION}  
  
# pytorch  
RUN pip3 install ${PYTORCH_LINK} \  
&& pip3 install torchvision  
  
# keras  
RUN pip3 install keras  
  
# image and video processing  
RUN apt-get update && apt-get install -y \  
ffmpeg \  
libav-tools \  
python3-tk \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN pip3 install --no-cache-dir \  
scikit-image \  
sk-video  

