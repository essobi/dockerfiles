FROM golang:1.6  
WORKDIR /tmp  
  
ENV PROTON_VERSION 0.13.1  
ENV CMAKE_VERSION 3.6.1  
RUN wget -O - http://apache-
mirror.rbc.ru/pub/apache/qpid/proton/${PROTON_VERSION}/qpid-
proton-${PROTON_VERSION}.tar.gz > /tmp/qpid-proton.tar.gz && \  
wget -O - https://cmake.org/files/v3.6/cmake-${CMAKE_VERSION}.tar.gz >
/tmp/cmake.tar.gz  
  
RUN apt-get update  
RUN apt-get install -y \  
#build deps  
gcc uuid-dev \  
# dependencies needed for ssl support  
libssl-dev \  
# dependencies needed for Cyrus SASL support  
libsasl2-2 libsasl2-dev  
  
#install cmake  
RUN tar xf /tmp/cmake.tar.gz && \  
cd cmake-${CMAKE_VERSION} && \  
./bootstrap && make && make install  
  
RUN tar xf /tmp/qpid-proton.tar.gz && \  
cd qpid-proton-${PROTON_VERSION} && \  
#following is according to PROTON INSTALL manual  
mkdir build && cd build && \  
# Set the install prefix. You may need to adjust depending on your system.  
cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DSYSINSTALL_BINDINGS=OFF \  
-DBUILD_PHP=OFF \  
-DBUILD_PERL=OFF \  
-DBUILD_PYTHON=OFF \  
-DBUILD_JAVA=OFF \  
-DBUILD_RUBY=OFF && \  
# Omit the docs target if you do not wish to build or install documentation.  
make all && make install

