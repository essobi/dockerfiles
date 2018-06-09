FROM ubuntu:xenial  
MAINTAINER Bruno Plamondon <plamondonb@sonatest.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# install tools for compiling projects  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends --no-install-suggests \  
ccache \  
cmake \  
g++ \  
git \  
libgsl0-dev \  
libqt4-opengl-dev \  
libvtk6-qt-dev \  
make \  
patch \  
python3-dev \  
qt4-qmake \  
qt4-default \  
unzip  
  
# user should be named tester  
RUN useradd --uid 1000 -G sudo --create-home tester \  
&& mkdir -p /home/tester/bin \  
&& chown -R tester:tester /home/tester/bin  
  
ADD bin /home/tester/bin  
  
ENV PATH=/home/tester/bin:$PATH  
  
ENV PATH=/usr/lib/ccache:$PATH  
ENV VTK_INC_PATH=/usr/include/vtk-6.2  
ENV VTK_LIB_PATH=/usr/lib/x86_64-linux-gnu/  
ENV VTK_LIB_SUFFIX=-6.2  
WORKDIR /home/tester/opt  
  
# Installing Eigen  
ADD eigen-eigen-67e894c6cd8f.tar.bz2 /home/tester/opt  
  
RUN mkdir -p /home/tester/opt/eigen-eigen-67e894c6cd8f/build \  
&& cd /home/tester/opt/eigen-eigen-67e894c6cd8f/build \  
&& cmake .. \  
&& make \  
&& make install \  
&& cd \- \  
&& rm -rf /home/tester/opt/eigen-eigen-67e894c6cd8f  
  
# installing Google Test & Mock  
# fetching source code  
ADD googletest-1.8.0.zip /home/tester/opt/googletest-1.8.0.zip  
  
RUN unzip googletest-1.8.0.zip \  
&& mv googletest-release-1.8.0 gtest \  
&& rm googletest-1.8.0.zip \  
&& mkdir -p /home/tester/opt/gtest/googletest \  
&& mkdir -p /home/tester/opt/gtest/googlemock  
  
ENV GTEST_DIR=/home/tester/opt/gtest/googletest  
ENV GMOCK_DIR=/home/tester/opt/gtest/googlemock  
  
# Compiling GMock and GTest  
# Version 1.7.0 expect library in GMOCK_DIR  
RUN g++ -isystem ${GTEST_DIR}/include -I${GTEST_DIR} -isystem
${GMOCK_DIR}/include -I${GMOCK_DIR} -pthread -c ${GTEST_DIR}/src/gtest-all.cc
\  
&& g++ -isystem ${GTEST_DIR}/include -I${GTEST_DIR} -isystem
${GMOCK_DIR}/include -I${GMOCK_DIR} -pthread -c ${GMOCK_DIR}/src/gmock-all.cc
\  
&& ar -rv /home/tester/opt/gtest/libgmock.a gtest-all.o gmock-all.o \  
&& cp /home/tester/opt/gtest/libgmock.a ${GMOCK_DIR}/ \  
&& rm -rf /home/tester/opt/*/*.o  
  
# Patch GMock  
ADD gmock_tokenize_public_slots.patch
/home/tester/opt/gtest/googlemock/scripts/generator/cpp/tokenize.patch  
WORKDIR /home/tester/opt/gtest/googlemock/scripts/generator/cpp  
RUN patch -p1 < ./tokenize.patch  
  
# cleanup  
# remove caches, documents, logs and examples  
# remove build temp files & unused packages  
# remove apt-(get/cache) package list  
RUN find /opt \\( -name "doc" -o -name "examples" \\) -type d -print0 | xargs
-0 --no-run-if-empty rm -rf \  
&& find /usr/share \\( -name doc -o -name fonts -o -name "[hH]elp" -o -name
man -o -name "[lL]ocale" \\) -type d -print0 | xargs -0 --no-run-if-empty rm
-rf \  
&& find /var/log -name "*" -type f -print0 | xargs -0 --no-run-if-empty rm -f
-- \  
&& find /var/cache -name "*" -type f -print0 | xargs -0 --no-run-if-empty rm
-f -- \  
&& rm -R /root/.ccache \  
&& apt-get purge -y locales unzip \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /var/lib/dpkg/info/*  
  
USER tester  
  
# Configuring ccache in user account  
RUN ccache --set-config=cache_dir=/cache --max-size=10G  
  
WORKDIR /devg3  
  

