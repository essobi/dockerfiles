FROM ubuntu:trusty  
  
# install dependencies  
RUN apt-get update && apt-get install -y \  
automake \  
bison \  
build-essential \  
flex \  
gfortran \  
git \  
g++ \  
libtool \  
openjdk-7-jre \  
wget \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /srv  
  
# install boost  
RUN wget -O boost_1_61_0.tar.bz2
https://sourceforge.net/projects/boost/files/boost/1.61.0/boost_1_61_0.tar.bz2/download
\  
&& tar xf boost_1_61_0.tar.bz2 \  
&& rm boost_1_61_0.tar.bz2 \  
&& cd boost_1_61_0 \  
&& ./bootstrap.sh --with-
libraries=chrono,date_time,filesystem,iostreams,program_options,random,regex,serialization,signals,system,thread,wave
\  
&& ./b2 -sNO_BZIP2=1 install  
  
RUN wget https://github.com/rose-compiler/rose/archive/v0.9.9.0.tar.gz \  
&& tar xf v0.9.9.0.tar.gz \  
&& rm v0.9.9.0.tar.gz  
  
ENV ROSESRC=$WORKSPACE/rose-0.9.9.0  
ENV ROSEBLD=$WORKSPACE/build  
ENV BOOSTROOT=/usr/local  
ENV LD_LIBRARY_PATH="$BOOSTROOT/lib:$LD_LIBRARY_PATH"  
WORKDIR $ROSEBLD  

