FROM ubuntu:trusty  
  
VOLUME /app  
WORKDIR /app  
  
VOLUME /ccache  
ENV CCACHE_DIR="/ccache"  
# Install requried libraries for C++ build  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
ca-certificates \  
wget \  
gcc \  
g++ \  
gcc-multilib \  
g++-multilib \  
make \  
cmake \  
ccache \  
python-dev \  
libi2c-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install boost  
RUN cd /tmp \  
&& wget -q -O boost_1_57_0.tar.gz
http://sourceforge.net/projects/boost/files/boost/1.57.0/boost_1_57_0.tar.gz/download
\  
&& tar xzf boost_1_57_0.tar.gz \  
&& mv boost_1_57_0 /opt  
  
# Install google test  
RUN cd /tmp \  
&& wget -q -O gtest-1.7.0.tar.gz
https://github.com/google/googletest/archive/release-1.7.0.tar.gz \  
&& tar xzf gtest-1.7.0.tar.gz \  
&& mv googletest-release-1.7.0 /opt/gtest_1_7_0  
  
ENV BOOST_PATH="/opt/boost_1_57_0"  
ENV GTEST_PATH="/opt/gtest_1_7_0"  
ADD build.sh /build.sh  
  
CMD /build.sh  

