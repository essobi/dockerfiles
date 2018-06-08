FROM ubuntu:16.04  
MAINTAINER Sascha Schade (strongly-typed) <stronglytyp3d@gmail.com>  
LABEL Description="Image with prerequisites for building Atmel AVR GNU
toolchain for Linux"  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y \  
git \  
wget \  
autoconf2.64 \  
build-essential \  
netpbm \  
texlive-latex-base \  
texlive-latex-recommended \  
texlive-latex-extra \  
texlive-font-utils \  
texinfo \  
doxygen \  
flex \  
bison \  
libexpat1-dev \  
slang-xfig \  
python2.7-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
WORKDIR /work  
  
ADD . /work  

