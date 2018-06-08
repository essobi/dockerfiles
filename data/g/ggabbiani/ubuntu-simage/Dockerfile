###############################################################################  
# simage@ubuntu:18.04  
###############################################################################  
# /  
# |-- build  
# | `-- simage <\-- build directory  
# |-- [rw] export <\-- output package directory  
# |-- [ro] import <\-- input source repository  
###############################################################################  
FROM ubuntu:18.04  
MAINTAINER Giampiero Gabbiani "giampiero@gabbiani.org"  
  
###############################################################################  
# simage building environment setup  
RUN apt-get update -y \  
&& apt-get dist-upgrade -y  
RUN apt-get install -y \  
apt-utils \  
vim build-essential \  
cmake \  
doxygen \  
graphviz \  
mercurial \  
lintian  
  
###############################################################################  
# simage pre requisites install  
RUN apt-get install -y \  
libgif-dev \  
libjpeg-dev \  
zlib1g-dev \  
libpng-dev \  
libtiff5-dev \  
libvorbis-dev \  
libsndfile1-dev \  
libxvidcore-dev \  
libquicktime-dev \  
qtbase5-dev \  
qttools5-dev-tools \  
qt5-default  
  
###############################################################################  
# directory structure setup  
RUN mkdir -p /build/simage  
WORKDIR /build/simage  
  
###############################################################################  
# defaults for building from a mounted project source  
CMD cmake /import -DCMAKE_BUILD_TYPE=MinSizeRel \  
&& make -j8 \  
&& make test \  
&& cpack --config cpack.d/debian.cmake \  
&& dpkg -i $(cat cpack.d/artifacts.list) \  
&& cp $(cat cpack.d/artifacts.list) /export/  

