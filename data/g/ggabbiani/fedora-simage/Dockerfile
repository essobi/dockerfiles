###############################################################################  
# simage@fedora:27  
###############################################################################  
# /  
# |-- build  
# | `-- simage <\-- build directory  
# |-- [rw] export <\-- output package directory  
# |-- [ro] import <\-- input source repository  
###############################################################################  
FROM fedora:27  
MAINTAINER Giampiero Gabbiani "giampiero@gabbiani.org"  
  
###############################################################################  
# simage building environment setup  
RUN dnf install -y https://download1.rpmfusion.org/free/fedora/rpmfusion-free-
release-$(rpm -E %fedora).noarch.rpm \  
&& dnf update -y  
RUN dnf install -y \  
rpm-build \  
vim \  
make \  
cmake \  
doxygen \  
graphviz \  
gcc-c++ \  
mercurial \  
rpmlint  
  
###############################################################################  
# simage pre requisites install  
RUN dnf install -y \  
giflib-devel \  
libjpeg-turbo-devel \  
zlib-devel \  
libpng-devel \  
libtiff-devel \  
libvorbis-devel \  
libsndfile-devel \  
xvidcore-devel \  
libquicktime-devel \  
qt5-qtbase-devel \  
qt5-doctools  
  
###############################################################################  
# directory structure setup  
RUN mkdir -p /build/simage  
WORKDIR /build/simage  
  
###############################################################################  
# defaults for building from a mounted project source  
CMD cmake /import -DCMAKE_BUILD_TYPE=MinSizeRel \  
&& make -j8 \  
&& make test \  
&& cpack --config cpack.d/fedora.cmake \  
&& rpm -ivh $(cat cpack.d/artifacts.list) \  
&& cp $(cat cpack.d/artifacts.list) /export/  
  

