FROM kaixhin/caffe  
  
WORKDIR /root  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install dependencies for OpenCV3  
RUN apt-get update -y --force-yes && sudo apt-get upgrade -y --force-yes && \  
apt-get install -y --force-yes build-essential cmake git libgtk2.0-dev pkg-
config libavcodec-dev libavformat-dev libswscale-dev \  
libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev
libdc1394-22-dev libv4l-dev libatlas-base-dev gfortran \  
python-dev python-numpy python-tk && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/*  
  
RUN mkdir ~/opencv  
  
# Clone OpenCV repository and checkout  
RUN cd ~/opencv && git clone https://github.com/Itseez/opencv_contrib.git &&
cd opencv_contrib && git checkout 3.0.0  
RUN cd ~/opencv && git clone https://github.com/Itseez/opencv.git && cd opencv
&& git checkout 3.0.0  
  
# CMake OpenCV  
RUN cd ~/opencv/opencv && mkdir release && cd release && \  
cmake -D CMAKE_BUILD_TYPE=RELEASE \  
-D CMAKE_INSTALL_PREFIX=/usr/local \  
-D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules \  
-D INSTALL_C_EXAMPLES=ON \  
-D INSTALL_PYTHON_EXAMPLES=ON \  
-D BUILD_EXAMPLES=ON ..  
  
RUN cd ~/opencv/opencv/release && make -j $(nproc) && make install && sudo
ldconfig  
  
WORKDIR /root/caffe/models  
  
# Download caffe models for AuditoryTracking  
RUN wget https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-
wiki/static/age.prototxt \  
https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/gender.prototxt \  
https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-
wiki/static/dex_chalearn_iccv2015.caffemodel \  
https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/gender.caffemodel
&& \  
mv dex_chalearn_iccv2015.caffemodel age.caffemodel

