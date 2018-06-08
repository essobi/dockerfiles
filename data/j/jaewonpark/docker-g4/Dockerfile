FROM ubuntu:14.04  
MAINTAINER Jaewon Park <jaewon.park@vt.edu>  
  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install -y git dpkg-dev make g++ gcc cmake \  
binutils libx11-dev libxpm-dev libxft-dev \  
libxext-dev libpng12-dev libjpeg-turbo8-dev \  
python gfortran libssl-dev wget libgsl0ldbl libgsl0-dev \  
cmake-curses-gui build-essential \  
libqt4-opengl libqt4-opengl-dev qt4-qmake libqt4-dev libx11-dev \  
libxmu-dev libxpm-dev libxft-dev  
  
ENV ROOT_TAR="root_v6.05.02.Linux-ubuntu14-x86_64-gcc4.8.tar.gz"  
ENV ROOT_DL="https://root.cern.ch/download/$ROOT_TAR"  
ENV ROOTSYS="/cern/root/"  
ENV PATH="$ROOTSYS/bin:$PATH"  
ENV LD_LIBRARY_PATH="$ROOTSYS/lib:$LD_LIBRARY_PATH"  
RUN mkdir /cern \  
&& cd /cern \  
&& wget $ROOT_DL \  
&& tar xzfv $ROOT_TAR \  
&& rm -rf $ROOT_TAR  
  
RUN mkdir -p /sw \  
&& cd /sw \  
&& wget http://geant4.cern.ch/support/source/geant4.10.01.tar.gz \  
&& tar zxf geant4.10.01.tar.gz \  
&& rm -f geant4.10.01.tar.gz \  
&& mkdir -p geant4-build \  
&& cd geant4-build \  
&& cmake /sw/geant4.10.01 -DGEANT4_BUILD_MULTITHREADED=ON \  
-DGEANT4_USE_QT=ON -DGEANT4_USE_OPENGL_X11=ON \  
-DGEANT4_USE_RAYTRACER_X11=ON -DGEANT4_INSTALL_DATA=ON \  
-Wno-dev \  
&& make -j`grep -c processor /proc/cpuinfo` \  
&& make install  
  

