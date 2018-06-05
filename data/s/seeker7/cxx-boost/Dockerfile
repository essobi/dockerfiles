FROM ubuntu:17.04  
# Install all required packages  
RUN DEBIAN_FRONTEND=noninteractive apt-get update \  
&& apt-get upgrade \  
&& apt-get install -y p7zip-full curl wget vim git \  
cmake cmake-curses-gui make ninja-build \  
g++ gdb clang-format ccache doxygen graphviz \  
libusb-1.0-0-dev \  
&& apt-get clean  
  
# Build and install latest boost  
RUN set -eu; cd /tmp \  
&& wget https://dl.bintray.com/boostorg/release/1.64.0/source/boost_1_64_0.7z
\  
&& 7za x boost_1_64_0.7z \  
&& cd boost_1_64_0/tools/build \  
&& ./bootstrap.sh \  
&& ./b2 --prefix=/usr/local install \  
&& cd ../.. \  
&& b2 --prefix=/usr/local toolset=gcc link=static install \  
&& cd .. \  
&& rm -rf boost_1_64_0 boost_1_64_0.7z  
  
RUN mkdir /src  
  
WORKDIR /src  
  
ENV HOME=/tmp  
  
ENTRYPOINT ["/bin/bash"]  

