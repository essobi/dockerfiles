FROM resin/armv7hf-debian  
  
RUN [ "cross-build-start" ]  
RUN apt-get update && \  
apt-get install -y --force-yes \  
python3 python3-dev python3-numpy python3-nose python3-pandas \  
python python-dev python-numpy python-nose python-pandas \  
pep8 python-pip python3-pip python-wheel \  
python-sphinx \  
wget \  
build-essential \  
cmake \  
pkg-config \  
libjpeg-dev \  
libtiff5-dev \  
libjasper-dev \  
libpng12-dev \  
libavcodec-dev \  
libavformat-dev \  
libswscale-dev \  
libv4l-dev \  
libgtk2.0-dev \  
libatlas-base-dev \  
gfortran \  
zip \  
unzip \  
sed && \  
pip install --upgrade setuptools numpy && \  
pip3 install --upgrade setuptools numpy  
  
RUN apt-get install -y --force-yes && \  
wget https://github.com/opencv/opencv/archive/3.3.0.zip \  
&& unzip 3.3.0.zip \  
# && sed -i 's/#if NPY_INTERNAL_BUILD/#ifndef NPY_INTERNAL_BUILD\n#define
NPY_INTERNAL_BUILD/g' /usr/local/lib/python3.4/site-
packages/numpy/core/include/numpy/npy_common.h \  
&& mkdir /opencv-3.3.0/cmake_binary \  
&& cd /opencv-3.3.0/cmake_binary \  
&& cmake -D CMAKE_BUILD_TYPE=RELEASE \  
-D CMAKE_INSTALL_PREFIX=/usr/local \  
-D INSTALL_PYTHON_EXAMPLES=ON \  
-D BUILD_EXAMPLES=ON .. \  
&& CORES=$(nproc --all) \  
&& make -j $CORES \  
&& make install \  
&& ldconfig \  
&& cd ../.. \  
&& rm /3.3.0.zip \  
&& rm -r /opencv-3.3.0  
RUN git clone https://github.com/arthurgeron/picamera \  
&& cd picamera \  
&& pip3 install -r requirements.txt \  
&& chmod +x main.py \  
&& cd ..  
  
RUN [ "cross-build-end" ]  
#Expose port 80  
EXPOSE 80  
#Default command  
CMD ["picamera/main.py"]  
  

