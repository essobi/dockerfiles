FROM debian:jessie
MAINTAINER Jan-Gerd Tenberge <jan-gerd.tenberge@uni-muenster.de>

ADD sources.list /etc/apt/sources.list
RUN apt-get update 
RUN apt-get install -y --no-install-recommends \
    python \
    python-numpy \
    libeigen3-dev \
    clang \
    zlib1g-dev \
    libqt4-opengl-dev \
    libgl1-mesa-dev \
    git \
    ca-certificates
RUN mkdir /mrtrix
RUN git clone https://github.com/MRtrix3/mrtrix3.git /mrtrix
WORKDIR /mrtrix
RUN git checkout tags/0.3.15
ENV CXX=/usr/bin/clang++
RUN ./configure
RUN ./build
ENV PATH=/root/mrtrix3/release/bin:$PATH
