FROM debian:jessie  
  
MAINTAINER Valentin Pesendorfer <valentin.pesendorfer@wfp.org>  
  
ENV OTBversion 6.0  
  
RUN apt-get update -y && apt-get upgrade -y && apt-get install -y \  
nano \  
cmake-curses-gui build-essential \  
qt4-dev-tools libqt4-core \  
libqt4-dev libboost1.55-dev \  
zlib1g-dev libopencv-dev curl \  
libcurl4-openssl-dev swig \  
libpython-dev \  
git \  
&& apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /OTB && mkdir /OTB/build && mkdir /OTB/install  
WORKDIR /OTB  
RUN git clone -b release-$OTBversion --single-branch https://git@git.orfeo-
toolbox.org/git/otb.git  
WORKDIR /OTB/build  
RUN cmake -DCMAKE_INSTALL_PREFIX=/OTB/install -DCMAKE_CXX_FLAGS=-std=c++11
-DOTB_USE_QT4=OFF -DOTB_WRAP_PYTHON=ON -DBUILD_EXAMPLES=OFF
-DBUILD_TESTING=OFF ../otb/SuperBuild  
RUN make -j 4  
  
ENV PATH=$PATH:/OTB/install/bin  
ENV LD_LIBRARY_PATH=/OTB/install/lib:$LD_LIBRARY_PATH  
ENV OTB_APPLICATION_PATH=/OTB/install/lib/otb/applications  
ENV PYTHONPATH /OTB/install/lib/otb/python  
  
RUN rm -rf /OTB/otb && rm -rf /OTB/build  
WORKDIR /home/root  

