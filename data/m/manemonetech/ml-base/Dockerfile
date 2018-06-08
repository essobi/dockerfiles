FROM tensorflow/tensorflow:1.2.1-gpu-py3  
  
# Auto upgrade  
ENV DEBIAN_FRONTEND "noninteractive"  
RUN apt-get update -y  
RUN apt-get -y \  
-o Dpkg::Options::="--force-confdef" \  
-o Dpkg::Options::="--force-confold" dist-upgrade  
  
# Install essentail / image processing libraries  
RUN apt-get update \  
&& apt-get install -y build-essential cmake pkg-config libjpeg8-dev
libtiff5-dev \  
libjasper-dev libpng12-dev libavcodec-dev libavformat-dev libswscale-dev
libv4l-dev \  
libxvidcore-dev libx264-dev libatlas-base-dev gfortran wget unzip tree
python3-tk tk-dev \  
&& apt-get clean -y \  
&& apt-get autoremove -y \  
&& apt-get update -y \  
&& apt-get upgrade -y \  
&& apt-get autoremove -y \  
&& apt-get autoclean -y \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*  
  
# Setup Python environments  
WORKDIR /root  
RUN wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py && rm -rf
~/get-pip.py ~/.cache/pip && pip install numpy scipy tqdm scikit-image seaborn
easydict  
  
# Download, Build and install opencv  
WORKDIR /tmp  
RUN wget -O /tmp/opencv.zip https://github.com/Itseez/opencv/archive/3.4.0.zip
&& unzip /tmp/opencv.zip \  
&& wget -O /tmp/opencv_contrib.zip
https://github.com/Itseez/opencv_contrib/archive/3.4.0.zip && unzip
/tmp/opencv_contrib.zip \  
&& mkdir -p /tmp/opencv-3.4.0/build \  
&& cd /tmp/opencv-3.4.0/build \  
&& cmake -D CMAKE_BUILD_TYPE=RELEASE \  
-D CMAKE_INSTALL_PREFIX=/usr/local \  
-D INSTALL_PYTHON_EXAMPLES=ON \  
-D INSTALL_C_EXAMPLES=OFF \  
-D OPENCV_EXTRA_MODULES_PATH=/tmp/opencv_contrib-3.4.0/modules \  
-D PYTHON_EXECUTABLE=/usr/bin/python \  
-D BUILD_EXAMPLES=ON .. \  
-DCMAKE_LIBRARY_PATH=/usr/local/cuda/lib64/stubs \  
&& make -j4 && make install && ldconfig \  
&& cd && rm -rf /tmp/opencv*  

