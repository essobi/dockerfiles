FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y \  
autoconf \  
libtool \  
flex \  
g++ \  
gfortran \  
libstdc++6 \  
byacc \  
libexpat1-dev \  
uuid-dev \  
build-essential \  
wget \  
pkg-config \  
gedit  
  
RUN python3 -v  
  
RUN apt-get install -y \  
python3-pip \  
build-essential \  
libssl-dev \  
libffi-dev \  
python3-dev  
  
# g++ >= 6.0  
# https://gist.github.com/application2000/73fd6f4bf1be6600a2cf9f56315a2d91  
RUN apt-get update && apt-get install -y \  
build-essential \  
software-properties-common  
  
RUN add-apt-repository -y \  
ppa:ubuntu-toolchain-r/test  
  
RUN apt-get update && apt-get install -y \  
gcc-snapshot  
  
RUN apt-get update && apt-get install -y \  
gcc-6 \  
g++-6  
  
RUN update-alternatives \  
\--install /usr/bin/gcc gcc /usr/bin/gcc-6 60 \  
\--slave /usr/bin/g++ g++ /usr/bin/g++-6  
  
RUN apt-get update && apt-get install -y \  
cmake \  
git  
  
# gtest  
RUN git clone -q https://github.com/google/googletest.git /googletest \  
&& mkdir -p /googletest/build \  
&& cd /googletest/build \  
&& cmake .. && make && make install \  
&& cd / && rm -rf /googletest  
  
RUN pip3 install \  
numpy \  
mock \  
chainer  
  
RUN gcc --version  
RUN g++ --version  
RUN cmake --version  
RUN git --version  
  
# DeepCoder  
RUN df -h  
  
ADD DeepCoder /DeepCoder  
# RUN ["chmod", "+x", "/epanet/configure"]  
RUN cd /DeepCoder \  
&& mkdir -p build  
  
RUN cd /DeepCoder/build \  
&& cmake ..  
  
RUN cd /DeepCoder/build \  
&& make  
  
WORKDIR /DeepCoder  

