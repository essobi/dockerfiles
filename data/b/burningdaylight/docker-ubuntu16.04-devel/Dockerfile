FROM ubuntu:16.04  
MAINTAINER Mykola Dimura <mykola.dimura@gmail.com>  
  
RUN apt-get update && apt-get install -y build-essential cmake git qt5-default
\  
libqt5serialport5-dev qtmultimedia5-dev libboost-all-dev libcaf-dev
libeigen3-dev \  
python-numpy python-dev python3-dev python-pytest python3-pytest  
#add eigen to include dir to work around the bug in eigen3 package  
RUN ln -s /usr/include/eigen3/Eigen /usr/local/include/Eigen  
  
RUN export BUILDDIR=$(mktemp -d -t build-XXXX);  
  
RUN cd "${BUILDDIR}"; \  
git clone https://github.com/pybind/pybind11.git; \  
cd "${BUILDDIR}/pybind11"; rm -rf build; mkdir build; cd build; \  
cmake -DPYBIND11_INSTALL=1 -DPYBIND11_TEST=0 ..; \  
make install  
  
RUN cd "${BUILDDIR}"; \  
git clone https://github.com/yesint/pteros.git pteros; \  
cd "${BUILDDIR}/pteros"; rm -rf build; mkdir build; cd build; \  
cmake -DEIGEN3_INCLUDE_DIR=/usr/include/eigen3 -DMAKE_PACKAGE=ON
-DCMAKE_BUILD_TYPE=Release ..; \  
make package; dpkg -i pteros-*.deb  
  
RUN cd "${BUILDDIR}"; git clone https://github.com/efficient/libcuckoo.git
libcuckoo; \  
cd libcuckoo; rm -rf build; mkdir build; cd build; \  
cmake -DBUILD_TESTS=1 -DBUILD_UNIVERSAL_BENCHMARK=1 -DCMAKE_BUILD_TYPE=Release
.. ; \  
make all; make install  
  
RUN cd "${BUILDDIR}"; git clone https://github.com/Amanieu/asyncplusplus.git
asyncplusplus; \  
cd asyncplusplus; rm -rf build; mkdir build; cd build; \  
cmake -DBUILD_SHARED_LIBS=1 -USE_CXX_EXCEPTIONS=1 -DCMAKE_BUILD_TYPE=Release
.. ; \  
make package; dpkg -i Async++-*.deb  
  
RUN cd "${BUILDDIR}"; git clone
https://github.com/cameron314/readerwriterqueue.git readerwriterqueue; \  
cd readerwriterqueue; INCLUDE_INSTALL_DIR=/usr/local/include/;
INSTALL_PREFIX=/opt/readerwriterqueue/; \  
mkdir -p "${INSTALL_PREFIX}"; cp readerwriterqueue.h atomicops.h
"${INSTALL_PREFIX}"; \  
ln -s "${INSTALL_PREFIX}" "${INCLUDE_INSTALL_DIR}/readerwriterqueue"  
  
#cleanup the build directory  
RUN rm -rf "${BUILDDIR}"  

