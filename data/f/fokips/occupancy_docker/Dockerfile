FROM ubuntu:16.10  
MAINTAINER Foka foka@posteo.de  
  
RUN export LC_ALL=C.UTF-8 && echo "deb-src http://archive.ubuntu.com/ubuntu/
yakkety multiverse" >> /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y install build-essential python3 python3-pip cmake git pkg-config
wget libjpeg8-dev libtiff5-dev libjasper-dev libpng-dev \  
libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libatlas-base-dev
libdc1394-22-dev unzip \  
gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly libavcodec-extra \  
&& pip3 install paho-mqtt simplejson numpy  
  
RUN ln -fs /usr/share/zoneinfo/Europe/Bratislava /etc/localtime && dpkg-
reconfigure -f noninteractive tzdata  
  
WORKDIR /  
RUN wget https://github.com/Itseez/opencv/archive/3.2.0.zip \  
&& unzip 3.2.0.zip \  
&& rm /3.2.0.zip \  
&& wget https://github.com/opencv/opencv_contrib/archive/3.2.0.zip \  
&& unzip 3.2.0.zip \  
&& rm /3.2.0.zip \  
&& mkdir /opencv-3.2.0/build \  
&& cd /opencv-3.2.0/build \  
&& cmake -D CMAKE_BUILD_TYPE=RELEASE \  
-D CMAKE_INSTALL_PREFIX=/usr/local \  
-D INSTALL_C_EXAMPLES=OFF \  
-D INSTALL_PYTHON_EXAMPLES=OFF \  
-D OPENCV_EXTRA_MODULES_PATH=/opencv_contrib-3.2.0/modules \  
-D BUILD_EXAMPLES=OFF \  
-DENABLE_AVX=ON \  
-DWITH_OPENGL=ON \  
-DWITH_OPENCL=ON \  
-DWITH_IPP=ON \  
-DWITH_TBB=ON \  
-DWITH_EIGEN=ON \  
-DWITH_V4L=ON .. && \  
make -j4 && make install && ldconfig && rm -r /opencv-3.2.0/ && rm -r
/opencv_contrib-3.2.0/  
  
COPY *.py /occupancy/  
COPY *.json /occupancy/  
  
EXPOSE 8000  
  
CMD ["python3","/occupancy/main.py","-l DEBUG"]  

