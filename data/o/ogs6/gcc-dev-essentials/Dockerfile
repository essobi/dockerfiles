FROM ubuntu:14.04  
MAINTAINER Lars Bilke <lars.bilke@ufz.de>  
  
RUN apt-get update \  
&& apt-get -y install \  
software-properties-common \  
wget \  
vim \  
&& echo 'deb http://llvm.org/apt/trusty/ llvm-toolchain-trusty-3.4 main' >>
/etc/apt/sources.list \  
&& wget -O - http://llvm.org/apt/llvm-snapshot.gpg.key|sudo apt-key add - \  
&& add-apt-repository -y ppa:ubuntu-toolchain-r/test \  
&& apt-get update \  
&& apt-get install -y \  
make \  
git \  
curl \  
&& apt-get install -y \  
gcc-4.9 \  
g++-4.9 \  
gcc-4.9-base \  
&& update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.9 100 \  
&& update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.9 100 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Build and install CMake from source.  
RUN curl -O https://cmake.org/files/v3.4/cmake-3.4.0.tar.gz \  
&& tar -xvf cmake-3.4.0.tar.gz  
WORKDIR cmake-3.4.0  
RUN ./bootstrap \  
&& make -j$(nproc) \  
&& make install \  
&& rm -rf *  
  
# Add user jenkins to the image  
RUN adduser --uid 500 --quiet jenkins  
  
# Add user jenkins to sudoers with NOPASSWD  
RUN echo "jenkins ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
  
# Set password for the jenkins user (you may want to alter this).  
RUN echo "jenkins:jenkins" | chpasswd  
  
WORKDIR /usr/src  

