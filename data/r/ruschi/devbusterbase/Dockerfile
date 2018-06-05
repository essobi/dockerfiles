FROM debian:buster  
LABEL maintainer="Thomas Ruschival <t.ruschival@gmail.com>"  
# Setup language environment and encoding  
ENV LC_ALL C.UTF-8  
ENV LANG C.UTF-8  
# Update package cache and install devtools  
RUN apt-get update && \  
apt-get install -y \  
bc \  
cmake \  
curl \  
git \  
build-essential \  
g++ \  
gcc \  
doxygen \  
lcov \  
gcovr \  
autoconf \  
automake \  
libtool \  
pkg-config \  
flex \  
bison \  
zip \  
unzip \  
libssl-dev \  
uuid-dev && \  
apt-get clean  
  
  
# Add a build user  
RUN useradd -m -s /bin/bash -G src build  

