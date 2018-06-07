FROM debian:jessie  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y unzip wget build-essential \  
cmake git pkg-config libswscale-dev \  
python2.7 python2.7-dev \  
libtbb2 libtbb-dev libjpeg-dev \  
libpng-dev libtiff-dev libjasper-dev libeigen3-dev  
  
RUN wget https://bootstrap.pypa.io/get-pip.py && python2.7 get-pip.py  
RUN pip install bottle  
RUN pip install numpy  
  
RUN cd \  
&& wget https://github.com/Itseez/opencv/archive/2.4.12.zip \  
&& unzip 2.4.12.zip \  
&& cd opencv-2.4.12 \  
&& mkdir build \  
&& cd build \  
&& cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D
BUILD_NEW_PYTHON_SUPPORT=ON -D WITH_XINE=ON -D WITH_TBB=ON .. \  
# && cmake .. \  
&& make -j3 \  
&& make install \  
&& cd \  
&& rm 2.4.12.zip \  
&& rm -r opencv-2.4.12  
  

