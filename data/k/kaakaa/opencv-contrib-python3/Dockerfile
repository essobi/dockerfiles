FROM python:3.5  
  
MAINTAINER Yusuke Nemoto <stooner.hoe@gmail.com>  
  
RUN apt-get update && apt-get install -y build-essential \  
cmake \  
wget \  
git \  
unzip \  
yasm \  
pkg-config \  
libjpeg-dev \  
libtiff-dev \  
libjasper-dev \  
libpng-dev \  
libavcodec-dev \  
libavformat-dev \  
libswscale-dev \  
libv4l-dev \  
libatlas-base-dev \  
gfortran \  
libtbb2 \  
libtbb-dev \  
libpq-dev \  
tesseract-ocr \  
tesseract-ocr-dev \  
libgtk2.0-dev \  
&& apt-get -y clean all \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip install numpy  
  
WORKDIR /  
  
# download opencv and opencv_contrib  
RUN wget https://github.com/Itseez/opencv/archive/3.1.0.zip -O opencv.zip \  
&& unzip opencv.zip \  
&& wget https://github.com/Itseez/opencv_contrib/archive/3.1.0.zip -O
opencv_contrib.zip \  
&& unzip opencv_contrib \  
&& mkdir /opencv-3.1.0/cmake_binary  
# download and install leptonica for tesseract-ocr  
RUN wget http://www.leptonica.com/source/leptonica-1.73.tar.gz \  
&& tar xvf leptonica-1.73.tar.gz \  
&& cd leptonica-1.73 \  
&& ./configure \  
&& make \  
&& make install  
# make and install opencv  
RUN cd /opencv-3.1.0/cmake_binary \  
&& Tesseract_INCLUDE_DIR=/usr/include/tesseract \  
&& Tesseract_LIBRARY=/usr/lib \  
&& cmake -DOPENCV_EXTRA_MODULES_PATH=/opencv_contrib-3.1.0/modules \  
-DBUILD_TIFF=ON \  
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
-DBUILD_opencv_python3=ON \  
-DCMAKE_INSTALL_PREFIX=$(python3.5 -c "import sys; print(sys.prefix)") \  
-DPYTHON_EXECUTABLE=$(which python3.5) \  
-DPYTHON_INCLUDE_DIR=$(python3.5 -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())") \  
-DPYTHON_PACKAGES_PATH=$(python3.5 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())") .. \  
&& make install \  
&& rm /opencv.zip \  
&& rm /opencv_contrib.zip \  
&& rm -r /opencv-3.1.0 \  
&& rm -r /opencv_contrib-3.1.0 \  
&& rm -r /leptonica-1.73.tar.gz  
  
# add jpn trained data  
RUN curl -o /usr/share/tesseract-ocr/tessdata/jpn.traineddata
https://github.com/tesseract-ocr/tessdata/raw/master/jpn.traineddata  

