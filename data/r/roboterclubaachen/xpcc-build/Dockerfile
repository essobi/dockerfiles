FROM stronglytyped/arm-none-eabi-gcc  
MAINTAINER Sascha Schade (strongly-typed) <stronglytyp3d@gmail.com>  
LABEL Description="Image for building and debugging xpcc for ARM and AVR from
git"  
WORKDIR /work  
  
ADD . /work  
  
ENV SCONS_LIB_DIR="/usr/local/lib/python2.7/dist-packages/scons-2.5.1"  
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
locales \  
gcc-avr \  
avr-libc \  
binutils-avr \  
gdb-avr \  
texlive-latex-base \  
texlive-fonts-recommended && \  
apt clean && \  
locale-gen en_US.UTF-8 && \  
pip install -r requirements.txt && \  
pip3 install -r requirements3.txt  

