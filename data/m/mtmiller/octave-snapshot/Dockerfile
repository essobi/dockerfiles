FROM ubuntu:trusty  
MAINTAINER Mike Miller <mtmiller@octave.org>  
  
RUN apt-get update && apt-get --no-install-recommends --yes install \  
autoconf \  
automake \  
build-essential \  
curl \  
default-jre-headless \  
epstool \  
g++ \  
gcc \  
gdb \  
gfortran \  
ghostscript \  
gnuplot-qt \  
info \  
less \  
libamd2.3.1 \  
libarpack2 \  
libblas-dev \  
libcamd2.3.1 \  
libccolamd2.8.0 \  
libcholmod2.1.2 \  
libcolamd2.8.0 \  
libcurl3-gnutls \  
libcxsparse3.1.2 \  
libfftw3-dev \  
libfltk-gl1.3 \  
libfontconfig1 \  
libfreetype6 \  
libgl1-mesa-glx \  
libgl2ps0 \  
libglpk36 \  
libglu1-mesa \  
libgraphicsmagick++3 \  
libhdf5-7 \  
liblapack-dev \  
libncurses5 \  
libopenblas-dev \  
libpcre3 \  
libportaudio2 \  
libqhull6 \  
libqrupdate1 \  
libqscintilla2-11 \  
libqt4-network \  
libqt4-opengl \  
libreadline-dev \  
libsndfile1 \  
libsundials-ida2 \  
libsundials-nvecserial0 \  
libtool \  
libumfpack5.6.2 \  
make \  
pstoedit \  
texinfo \  
transfig \  
unzip \  
xz-utils \  
zip \  
&& apt-get clean \  
&& rm -rf \  
/tmp/hsperfdata* \  
/var/*/apt/*/partial \  
/var/lib/apt/lists/* \  
/var/log/apt/term*  
  
ADD https://s3.amazonaws.com/octave-snapshot/public/SHA256SUMS /  
RUN curl -SL https://s3.amazonaws.com/octave-snapshot/public/octave-ubuntu-
trusty-snapshot.tar.xz \  
| tar -xJC /usr/local --strip-components=1  

