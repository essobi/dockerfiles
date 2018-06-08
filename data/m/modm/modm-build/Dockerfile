FROM modm/arm-none-eabi-gcc:latest  
MAINTAINER Niklas Hauser <niklas.hauser@rwth-aachen.de>  
LABEL Description="Image for building and debugging modm for ARM and AVR from
git"  
WORKDIR /work  
  
ADD . /work  
  
ENV SCONS_LIB_DIR="/usr/local/lib/python3.6/dist-packages/scons-3.0.1"  
# Install any needed packages specified in requirements.txt  
RUN apt update && \  
apt upgrade -y && \  
apt install -y \  
python \  
python-dev \  
python-pip \  
python3 \  
python3-dev \  
python3-pip \  
libboost-all-dev \  
libsdl1.2-dev \  
libsdl-image1.2-dev \  
libgtkmm-2.4-dev \  
libzmqpp-dev \  
libmpc-dev \  
libmpfr-dev \  
libgmp-dev \  
cmake \  
locales \  
texlive-latex-base \  
texlive-fonts-recommended && \  
apt clean && \  
locale-gen en_US.UTF-8 && \  
pip install -r requirements.txt && \  
python3 -m pip install --upgrade pip && \  
pip3 install -r requirements3.txt && \  
pip3 install git+https://github.com/dergraaf/library-builder && \  
pip3 install graphviz && \  
wget -qO- https://github.com/salkinium/docker-avr-
gcc-7/releases/download/v7.3.0/avr-gcc.tar.bz2 | tar xj  
  
ENV PATH "/work/avr-gcc/avr-gcc/bin:/work/avr-gcc/avr-binutils/bin:$PATH"

