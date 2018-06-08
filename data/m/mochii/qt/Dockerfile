FROM ubuntu:16.04  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
RUN apt-get update && apt-get install -y software-properties-common python-
software-properties && add-apt-repository ppa:beineri/opt-qt561-xenial  
RUN apt-get update && apt-get install -y git qt56-meta-full build-essential
mesa-common-dev libglu1-mesa-dev && rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
curl \  
make \  
poppler-utils \  
vlc \  
libvlc-dev \  
libvlccore-dev  
  
# Install cmake  
RUN curl -sSL https://cmake.org/files/v3.4/cmake-3.4.0-Linux-x86_64.tar.gz |
tar -xzC /opt  
RUN ln -s /opt/cmake-3.4.0-Linux-x86_64/bin/cmake /usr/bin/cmake  
  
ENV QT_BASE_DIR=/opt/qt56  
ENV QTDIR=$QT_BASE_DIR  
ENV PATH=$QT_BASE_DIR/bin:$PATH  
ENV LD_LIBRARY_PATH=$QT_BASE_DIR/lib/x86_64-linux-
gnu:$QT_BASE_DIR/lib:$LD_LIBRARY_PATH  
ENV PKG_CONFIG_PATH=$QT_BASE_DIR/lib/pkgconfig:$PKG_CONFIG_PATH  
  
# Install vlc-qt  
RUN mkdir -p /usr/src/  
RUN cd /usr/src/ && git clone \--branch 1.1.0 https://github.com/vlc-qt/vlc-
qt.git  
RUN cd /usr/src/vlc-qt && mkdir build && cd build && cmake ..
-DCMAKE_BUILD_TYPE=Debug && make -j8 && make install  
  
VOLUME ["/home/workspace"]

