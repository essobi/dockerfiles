FROM debian:stretch  
  
RUN apt-get update && apt-get install -y \  
# required packages to compile OpenCV  
build-essential \  
cmake \  
git \  
pkg-config \  
libgtk2.0-dev \  
libavcodec-dev \  
libavformat-dev \  
libswscale-dev \  
# optional packages  
libtbb2 \  
libtbb-dev \  
libjpeg-dev \  
libpng-dev \  
libtiff-dev \  
libdc1394-22-dev \  
# python3 packages  
python-dev \  
python3.5-dev \  
python3-pip \  
python3-numpy \  
&& rm -rf /var/lib/apt/lists/* \  
&& pip3 install --upgrade pip  
  
WORKDIR /tmp  
  
RUN git clone --depth 1 https://github.com/opencv/opencv.git  
RUN git clone --depth 1 https://github.com/opencv/opencv_contrib.git  
  
WORKDIR opencv/build  
  
RUN cmake \  
-D CMAKE_BUILD_TYPE=RELEASE \  
-D CMAKE_INSTALL_PREFIX=/usr/local \  
-D OPENCV_EXTRA_MODULES_PATH=/tmp/opencv_contrib/modules/ \  
-D PYTHON_EXECUTABLE="$(which python3)" \  
-D PYTHON_INCLUDE_DIR=/usr/include/python3.5m \  
-D PYTHON_INCLUDE_DIR2=/usr/include/x86_64-linux-gnu/python3.5m \  
-D PYTHON_LIBRARY=/usr/lib/x86_640linux-gnu/libpython3.5m.so \  
-D PYTHON3_NUMPY_INCLUDE_DIRS=/usr/lib/python3/dist-packages/numpy/core/include/ \  
.. \  
&& make -j "$(nproc --all)" \  
&& make install \  
&& rm -rf /tmp/*  
  
RUN pip3 install \  
matplotlib \  
scipy \  
jupyter  
  
WORKDIR /root/workspace  
  
CMD ["jupyter", "notebook", "--ip", "0.0.0.0", "--no-browser", "--allow-root",
"--NotebookApp.token=''"]  

