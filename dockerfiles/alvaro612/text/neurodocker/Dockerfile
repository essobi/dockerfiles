FROM ubuntu:14.04
MAINTAINER alvaroabascar@gmail.com

# Update, install git, python, install dependencies
RUN apt-get update && apt-get install -y\
    python \
    git \
    build-essential \
    zlib1g-dev \
    libgsl0-dev \
    automoc

# Download and compile mrtrix3
RUN cd /root/ &&\
    git clone https://github.com/MRtrix3/mrtrix3 &&\
    cd mrtrix3 &&\
    ./configure &&\
    ./build

# Add mrtrix3 bin folder to the path
ENV PATH /root/mrtrix3/bin/:$PATH

# Update, install wget, then fsl & cmake (cmake to compile ANTs)
RUN apt-get update && apt-get install -y wget

RUN cd /root/ &&\
    wget -O- http://neuro.debian.net/lists/trusty.de-md.full | tee /etc/apt/sources.list.d/neurodebian.sources.list &&\
    apt-key adv --recv-keys --keyserver hkp://pgp.mit.edu:80 0xA5D32F012649A5A9 &&\
    apt-get update &&\
    apt-get install -y\
        fsl-complete\
        cmake

RUN cd /root/ &&\
    git clone git://github.com/stnava/ANTs.git &&\
    mkdir antsbin && cd antsbin &&\
    cmake ../ANTs &&\
    make -j 4

ENV ANTSPATH /root/antsbin/bin/
ENV PATH /root/antsbin/bin/:$PATH
