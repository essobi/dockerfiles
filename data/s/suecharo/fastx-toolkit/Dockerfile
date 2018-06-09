# Docker image for FASTX-Toolkit  
FROM ubuntu:trusty  
MAINTAINER suecharo, suehiro619@gmail.com  
  
# Install build tools  
RUN apt-get update \  
&& apt-get install -y \  
wget \  
make \  
g++ \  
pkg-config \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install libgtextutils  
WORKDIR /src  
RUN wget
https://github.com/agordon/libgtextutils/releases/download/0.7/libgtextutils-0.7.tar.gz
\  
&& tar -zxvf libgtextutils-0.7.tar.gz \  
&& rm -rf libgtextutils-0.7.tar.gz \  
&& cd libgtextutils-0.7 \  
&& ./configure \  
&& make \  
&& make install  
  
# Install FASTX-toolkit  
WORKDIR /src  
RUN wget
https://github.com/agordon/fastx_toolkit/releases/download/0.0.14/fastx_toolkit-0.0.14.tar.bz2
\  
&& tar -jxvf fastx_toolkit-0.0.14.tar.bz2 \  
&& rm -rf fastx_toolkit-0.0.14.tar.bz2 \  
&& cd fastx_toolkit-0.0.14 \  
&& ./configure \  
&& make \  
&& make install  
  
WORKDIR /mount  
CMD ["bash"]  

