FROM debian:jessie  
MAINTAINER Matt McCormick <matt.mccormick@kitware.com>  
  
RUN apt-get update && apt-get install -y \  
apt-utils \  
build-essential \  
curl \  
git \  
python \  
vim  
  
# Install the latest CMake release  
WORKDIR /tmp/  
RUN curl -L https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \  
python get-pip.py && \  
pip install cmake  
  
# Normal user  
RUN useradd -m itk  
RUN echo 'root:itk' | chpasswd  
RUN echo 'itk:itk' | chpasswd  
ENV HOME /home/itk  
USER itk  
WORKDIR /home/itk  
RUN mkdir /home/itk/src  
RUN mkdir /home/itk/bin  
CMD ["/bin/bash"]  

