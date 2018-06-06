FROM ubuntu:14.04  
MAINTAINER Matt DeBoer <matt.deboer@gmail.com>  
  
ENV MESOS_RELEASE_VERSION=1.0.3 \  
PROTOBUF_VERSION=2.6.1 \  
BUILD_DIR="./build" \  
CMAKE_ARGS=""  
  
RUN apt-get update -q --fix-missing \  
&& apt-get -qy install software-properties-common \  
&& apt-get update -qy \  
&& apt-get -qy install \  
linux-libc-dev \  
build-essential \  
autoconf \  
automake \  
ca-certificates \  
gdb \  
wget \  
git-core \  
libcurl4-nss-dev \  
libsasl2-dev \  
libtool \  
libsvn-dev \  
libapr1-dev \  
libgoogle-glog-dev \  
libboost-dev \  
make \  
python \  
python2.7 \  
libpython-dev \  
python-dev \  
python-setuptools \  
heimdal-clients \  
libsasl2-modules-gssapi-heimdal \  
unzip \  
\--no-install-recommends \  
&& wget
https://github.com/google/protobuf/releases/download/v${PROTOBUF_VERSION}/protobuf-${PROTOBUF_VERSION}.tar.gz
\  
&& tar -xvzf protobuf-${PROTOBUF_VERSION}.tar.gz \  
&& cd protobuf-${PROTOBUF_VERSION}/ \  
&& ./configure --prefix=/usr \  
&& make && make install \  
&& rm -rf /protobuf-${PROTOBUF_VERSION} \  
&& rm -f /protobuf-${PROTOBUF_VERSION}.tar.gz \  
&& wget https://raw.githubusercontent.com/kazuho/picojson/v1.3.0/picojson.h -O
/usr/local/include/picojson.h \  
&& wget http://www.cmake.org/files/v3.6/cmake-3.6.1.tar.gz -O
/cmake-3.6.1.tar.gz \  
&& cd / \  
&& tar -xvzf cmake-3.6.1.tar.gz \  
&& cd /cmake-3.6.1 \  
&& ./configure \  
&& make && make install \  
&& update-alternatives --install /usr/bin/cmake cmake /usr/local/bin/cmake 1
--force \  
&& cmake --version \  
&& mkdir -p /mesos \  
&& mkdir -p /tmp \  
&& mkdir -p /usr/share/java/ \  
&& wget
http://search.maven.org/remotecontent?filepath=com/google/protobuf/protobuf-
java/2.5.0/protobuf-java-2.5.0.jar -O protobuf.jar \  
&& mv protobuf.jar /usr/share/java/ \  
&& git clone git://git.apache.org/mesos.git /mesos \  
&& cd /mesos && git checkout tags/${MESOS_RELEASE_VERSION} \  
&& git log -n 1 \  
&& ./bootstrap \  
&& mkdir build \  
&& cd build \  
&& ../configure --disable-java --disable-python --disable-optimize --without-
included-zookeeper --with-glog=/usr/local --with-protobuf=/usr --with-
boost=/usr/local \  
&& make -j 2 install \  
&& apt-get install -qy libgtest-dev \  
&& cd /usr/src/gtest \  
&& cmake CMakeLists.txt \  
&& make \  
&& cp *.a /usr/local/lib/ \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& printf "#!/bin/sh\n\  
rm -rf \${BUILD_DIR} && \n\  
mkdir -p \${BUILD_DIR} && \n\  
cd ${BUILD_DIR} && \n\  
cmake -DMESOS_VERSION:STRING=${MESOS_RELEASE_VERSION} \${CMAKE_ARGS} .. && \n\  
make\n"\  
>> /bin/build \  
&& chmod +x /bin/build  
  
VOLUME /src  
WORKDIR /src  
  
CMD ["/bin/build"]

