# Start with Ubuntu base image  
FROM ubuntu:14.04  
MAINTAINER Haoming Wang <haoming.exe@gmail.com>  
  
# Install OpenCV3  
# this is needed as libfaac-dev comes from multiverse, according to:  
# http://superuser.com/questions/467774/how-to-install-libfaac-dev  
RUN echo "deb http://us.archive.ubuntu.com/ubuntu/ precise multiverse\n\  
deb-src http://us.archive.ubuntu.com/ubuntu/ precise multiverse\n\  
deb http://us.archive.ubuntu.com/ubuntu/ precise-updates multiverse\n\  
deb-src http://us.archive.ubuntu.com/ubuntu/ precise-updates multiverse\n"\  
>> /etc/apt/sources.list  
  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \  
software-properties-common  
RUN add-apt-repository ppa:george-edison55/cmake-3.x  
RUN apt-get update -qq  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \  
curl \  
cmake \  
wget \  
unzip \  
libopencv-dev \  
build-essential \  
git \  
libgtk2.0-dev \  
pkg-config \  
libdc1394-22 \  
libdc1394-22-dev \  
libjpeg-dev \  
libpng12-dev \  
libtiff4-dev \  
libjasper-dev \  
libavcodec-dev \  
libavformat-dev \  
libswscale-dev \  
libxine-dev \  
libgstreamer0.10-dev \  
libgstreamer-plugins-base0.10-dev \  
libv4l-dev \  
libtbb-dev \  
libqt4-dev \  
libfaac-dev \  
libmp3lame-dev \  
libopencore-amrnb-dev \  
libopencore-amrwb-dev \  
libtheora-dev \  
libvorbis-dev \  
libxvidcore-dev \  
x264 \  
v4l-utils  
  
# Install Caffe dependencies  
RUN apt-get update && apt-get install -y --no-install-recommends \  
libatlas-base-dev \  
libboost-all-dev \  
libgflags-dev \  
libgoogle-glog-dev \  
libhdf5-serial-dev \  
libleveldb-dev \  
liblmdb-dev \  
libprotobuf-dev \  
libsnappy-dev \  
protobuf-compiler && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Install Anaconda2  
RUN wget --quiet
http://repo.continuum.io/archive/Anaconda2-4.1.1-Linux-x86_64.sh && \  
/bin/bash Anaconda2-4.1.1-Linux-x86_64.sh -b -p /opt/anaconda2 && \  
rm Anaconda2-4.1.1-Linux-x86_64.sh  
ENV PATH /opt/anaconda2/bin:$PATH  
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/lib/x86_64-linux-
gnu/:/usr/lib/x86_64-linux-gnu/:/opt/anaconda2/lib  
  
  
RUN mkdir opencv  
WORKDIR opencv  
  
RUN git clone https://github.com/Itseez/opencv.git && cd opencv && git
checkout 3.1.0  
RUN cd opencv && wget https://patch-
diff.githubusercontent.com/raw/Itseez/opencv/pull/6009.diff && \  
git apply 6009.diff  
RUN git clone https://github.com/Itseez/opencv_contrib.git && cd
opencv_contrib && git checkout 3.1.0  
  
RUN mkdir opencv/build  
WORKDIR opencv/build  
  
RUN cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D
WITH_TBB=ON -D WITH_V4L=ON -D WITH_QT=ON -D WITH_OPENGL=ON -D WITH_IPP=OFF -D
PYTHON_EXECUTABLE=/opt/anaconda2/bin/python -D
PYTHON_INCLUDE_DIR=/opt/anaconda2/include/python2.7/ -D
PYTHON_INCLUDE_DIR2=/opt/anaconda2/include/python2.7 -D
PYTHON_PACKAGES_PATH=/opt/anaconda2/lib/python2.7/site-packages -D
PYTHON2_LIBRARY=/opt/anaconda2/lib/libpython2.7.so -D BUILD_opencv_python2=ON
-D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules ..  
  
RUN make -j $(nproc) && make install  
RUN echo "/usr/local/lib" > /etc/ld.so.conf.d/opencv.conf  
RUN ldconfig  
  
RUN make clean && \  
cp /usr/local/lib/python2.7/site-packages/cv2.so
/opt/anaconda2/lib/python2.7/site-packages && \  
cd ../../.. && rm -rf opencv  
  
# Clone Caffe repo and move into it  
RUN cd /root && git clone https://github.com/BVLC/caffe.git && cd caffe && \  
# Install python dependencies  
cat python/requirements.txt | xargs -n1 pip install && \  
# fix "Failed to initialize libdc1394" error  
ln /dev/null /dev/raw1394

