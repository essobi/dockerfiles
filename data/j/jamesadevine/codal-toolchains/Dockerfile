##  
## Toolchain and tools to build AVR projects with C/C++ and Assembler.  
FROM coolya/gcc-avr  
RUN useradd -g 0 --create-home --no-log-init --shell /bin/bash codal  
MAINTAINER James Devine <j.devine@lancaster.ac.uk>  
  
ENV PYTHON_VERSION 2.7.13  
ENV PATH $PATH:/usr/local/avr/bin  
  
RUN \  
apt-get update && apt-get install -y --no-install-recommends \  
wget \  
make \  
build-essential \  
gcc-arm-none-eabi \  
libstdc++-arm-none-eabi-newlib \  
libnewlib-arm-none-eabi \  
ca-certificates \  
git \  
&& wget
https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tgz
--no-check-certificate \  
&& tar -xvf Python-$PYTHON_VERSION.tgz \  
&& cd Python-$PYTHON_VERSION \  
&& ./configure && make && make install && cd ..  
  
USER codal  
WORKDIR /home/codal

