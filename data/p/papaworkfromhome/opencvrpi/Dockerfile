FROM python:2.7  
  
MAINTAINER Papaworkfromhome  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Various Python and C/build deps  
RUN apt-get update && apt-get install -y \  
wget \  
build-essential \  
cmake \  
git \  
unzip \  
pkg-config \  
python-dev \  
python-opencv \  
libopencv-dev \  
libav-tools \  
libjpeg-dev \  
libpng-dev \  
libtiff-dev \  
libjasper-dev \  
libgtk2.0-dev \  
python-numpy \  
python-pycurl \  
libatlas-base-dev \  
gfortran \  
webp \  
python-opencv \  
qt5-default \  
libvtk6-dev \  
zlib1g-dev  
  
# Install Open CV - Warning, this takes absolutely forever  
RUN mkdir -p ~/opencv cd ~/opencv && \  
wget https://github.com/Itseez/opencv/archive/3.0.0.zip && \  
unzip 3.0.0.zip && \  
rm 3.0.0.zip && \  
mv opencv-3.0.0 OpenCV && \  
cd OpenCV && \  
mkdir build && \  
cd build && \  
cmake \  
-DWITH_QT=ON \   
-DWITH_OPENGL=ON \   
-DFORCE_VTK=ON \  
-DWITH_TBB=ON \  
-DWITH_GDAL=ON \  
-DWITH_XINE=ON \  
-DBUILD_EXAMPLES=ON .. && \  
make -j4 && \  
make install && \  
ldconfig  
  
#RUN pip install --no-cache-dir -r requirements.txt  
  

