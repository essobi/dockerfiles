FROM ubuntu:16.04  
MAINTAINER Daisuke Miyamoto <miyamoto@brain.imi.i.u-tokyo.ac.jp>  
  
ARG CFLAGS="-O3"  
ARG CXXFLAGS="-O3"  
RUN apt-get update \  
&& apt-get install -y \  
locales \  
wget \  
gcc \  
g++ \  
build-essential \  
openmpi-bin \  
openmpi-common \  
libopenmpi-dev \  
&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8 \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get autoclean  
  
RUN useradd bench \  
&& mkdir /work  
  
COPY Makefile /work/  
COPY run.sh /work/  
COPY run_small.sh /work/  
COPY himeno /work/himeno  
COPY stream /work/stream  
COPY fio /work/fio  
COPY unixbench /work/unixbench  
COPY jobs /work/jobs  
  
RUN chown -R bench /work  
  
USER bench  
WORKDIR /work  
RUN make \  
&& chmod +x jobs/* \  
&& chmod +x run.sh \  
&& chmod +x run_small.sh  
  

