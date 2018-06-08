# Minimal docker container to build project  
# Image: tstumm/qt-opencv:551.30  
FROM ubuntu:14.04  
MAINTAINER tstumm  
  
ENV DEBIAN_FRONTEND noninteractive  
  
  
# Install updates & requirements:  
# * git, openssh-client - for Drone  
# * curl, p7zip - to download & unpack Qt bundle  
# * build-essential, pkg-config, libgl1-mesa-dev - basic Qt build requirements  
# * libsm6, libice6, libxext6, libxrender1, libfontconfig1 - dependencies of
Qt bundle run-file  
RUN apt-get -qq update && apt-get -qq dist-upgrade && apt-get install -qq -y
--no-install-recommends \  
git \  
openssh-client \  
ca-certificates \  
curl \  
p7zip \  
build-essential \  
pkg-config \  
libgl1-mesa-dev \  
libsm6 \  
libice6 \  
libxext6 \  
libxrender1 \  
libfontconfig1 \  
&& apt-get -qq clean  
  
RUN apt-get update && apt-get install -y software-properties-common python-
software-properties && add-apt-repository ppa:beineri/opt-qt55-trusty  
RUN apt-get update && apt-get install -y git qt55-meta-full build-essential
mesa-common-dev libglu1-mesa-dev && rm -rf /var/lib/apt/lists/*  
  
ENV QT_BASE_DIR=/opt/qt55  
ENV QTDIR=$QT_BASE_DIR  
ENV PATH=$QT_BASE_DIR/bin:$PATH  
ENV LD_LIBRARY_PATH=$QT_BASE_DIR/lib/x86_64-linux-
gnu:$QT_BASE_DIR/lib:$LD_LIBRARY_PATH  
ENV PKG_CONFIG_PATH=$QT_BASE_DIR/lib/pkgconfig:$PKG_CONFIG_PATH  
  
# Reconfigure locale  
RUN locale-gen en_US.UTF-8 && dpkg-reconfigure locales  
  
RUN echo "deb http://us.archive.ubuntu.com/ubuntu/ trusty multiverse" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get -y install libopencv-dev build-essential cmake \  
libgtk2.0-dev pkg-config python-dev python-numpy libdc1394-22 \  
libdc1394-22-dev libjpeg-dev libpng12-dev libtiff4-dev \  
libjasper-dev libavcodec-dev libavformat-dev libswscale-dev \  
libxine-dev libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev \  
libv4l-dev libtbb-dev libqt4-dev libfaac-dev libmp3lame-dev \  
libopencore-amrnb-dev libopencore-amrwb-dev libtheora-dev \  
libvorbis-dev libxvidcore-dev x264 v4l-utils unzip ssh openssh-server  
  
RUN cd /opt \  
&& wget https://github.com/Itseez/opencv/archive/3.0.0.zip \  
&& unzip 3.0.0.zip \  
&& cd opencv-3.0.0 \  
&& mkdir release \  
&& cd release \  
&& cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D
WITH_TBB=ON -D BUILD_NEW_PYTHON_SUPPORT=ON -D WITH_V4L=ON -D
INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON -D BUILD_EXAMPLES=ON -D
WITH_QT=ON -D WITH_OPENGL=ON .. \  
&& make -j4 \  
&& make install \  
&& bash -c 'echo "/usr/local/lib" > /etc/ld.so.conf.d/opencv.conf' \  
&& ldconfig \  
&& rm /opt/3.0.0.zip \  
&& rm -R /opt/opencv-3.0.0  
  
RUN mkdir /var/run/sshd \  
&& echo 'root:root' | chpasswd \  
&& sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config \  
&& echo "export VISIBLE=now" >> /etc/profile  
  
# SSH login fix. Otherwise user is kicked off after login  
#RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
ENV NOTVISIBLE "in users profile"  
CMD ["/usr/sbin/sshd", "-D"]  
  
EXPOSE 22  

