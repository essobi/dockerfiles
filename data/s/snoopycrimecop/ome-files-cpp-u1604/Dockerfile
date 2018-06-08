FROM ubuntu:16.04  
MAINTAINER ome-devel@lists.openmicroscopy.org.uk  
  
RUN apt-get update && apt-get -y install \  
build-essential \  
cmake \  
git \  
man \  
libboost-all-dev \  
libxerces-c-dev \  
libxalan-c-dev \  
libpng-dev \  
libgtest-dev \  
libtiff5-dev \  
locales \  
python-pip \  
&& locale-gen en_US.UTF-8  
  
ENV LC_ALL=en_US.UTF-8  
ENV LANG=en_US.UTF-8  
RUN pip install --upgrade pip  
RUN pip install Genshi  
RUN pip install Sphinx  
  
WORKDIR /git  
RUN git clone \--branch='v5.5.0' https://github.com/ome/ome-common-cpp.git  
RUN git clone \--branch='v5.6.0' https://github.com/ome/ome-model.git  
RUN git clone \--branch='v0.5.0' https://github.com/ome/ome-files-cpp.git  
RUN git clone \--branch='v5.4.3' https://github.com/ome/ome-qtwidgets.git  
RUN git clone \--branch='v0.5.0' https://github.com/ome/ome-cmake-
superbuild.git  
  
WORKDIR /build  
RUN cmake \  
-Dgit-dir=/git \  
-Dbuild-prerequisites=OFF \  
-Dome-superbuild_BUILD_gtest=ON \  
-Dbuild-packages=ome-files \  
-DCMAKE_BUILD_TYPE=Release \  
/git/ome-cmake-superbuild  
RUN make  
RUN make install  
RUN ldconfig  

