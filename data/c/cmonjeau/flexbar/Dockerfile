############################################################  
# Dockerfile to build Flexbar 3.0.3 tool container image  
# Based on debian ubuntu  
############################################################  
  
FROM ubuntu:14.04  
  
RUN apt-get update \  
&& apt-get install -y software-properties-common \  
tar \  
wget \  
xz-utils \  
curl \  
unzip \  
gcc \  
git \  
zlib1g-dev \  
libncurses5-dev \  
libncursesw5-dev \  
cmake \  
build-essential \  
tabix \  
libtbb-dev  
  
################## GCC INSTALLATION ######################  
  
RUN add-apt-repository ppa:ubuntu-toolchain-r/test  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get dist-upgrade -y  
  
RUN apt-get install -y g++-4.9  
RUN ln -f -s /usr/bin/g++-4.9 /usr/bin/g++  
  
################## FLEXBAR INSTALLATION ######################  
  
WORKDIR /opt  
  
RUN wget https://github.com/seqan/seqan/releases/download/seqan-v2.2.0/seqan-
library-2.2.0.tar.xz  
RUN wget https://github.com/seqan/flexbar/archive/v3.0.3.tar.gz  
RUN tar -xzf v3.0.3.tar.gz  
RUN tar -xJf seqan-library-2.2.0.tar.xz  
RUN mv seqan-library-2.2.0/include flexbar-3.0.3  
  
WORKDIR /opt/flexbar-3.0.3  
  
RUN cmake .  
RUN make  
  
ENV LD_LIBRARY_PATH="/opt/flexbar-3.0.3:$LD_LIBRARY_PATH"  
ENV PATH="/opt/flexbar-3.0.3:$PATH"  

