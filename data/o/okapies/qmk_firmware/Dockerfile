FROM ubuntu:trusty  
MAINTAINER Yuta Okamoto <okapies@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV DEBCONF_NONINTERACTIVE_SEEN true  
RUN echo "grub-pc hold" | dpkg --set-selections  
RUN apt-get -y update && apt-get -y --allow-unauthenticated upgrade \  
-o Dpkg::Options::="--force-confdef" \  
-o Dpkg::Options::="--force-confold"  
RUN apt-get install -y \  
build-essential \  
gcc \  
unzip \  
wget \  
zip \  
gcc-avr \  
binutils-avr \  
avr-libc \  
dfu-programmer \  
dfu-util \  
gcc-arm-none-eabi \  
binutils-arm-none-eabi \  
libnewlib-arm-none-eabi \  
git \  
diffutils \  
curl \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*

