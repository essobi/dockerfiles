FROM ubuntu:wily  
MAINTAINER Adam Szalkowski <adam.szalkowski@bbv.ch>  
  
RUN apt-get -qq update && apt-get -qq install -y --fix-missing --no-install-
recommends \  
build-essential \  
autoconf \  
automake \  
libtool \  
make \  
m4 \  
gawk \  
autoconf-archive \  
flex \  
bison \  
gdb \  
gettext \  
binutils-gold \  
g++-5 \  
libstdc++-5-dev \  
libcairomm-1.0-dev \  
libcairomm-1.0-doc \  
libcairo2-doc \  
libgtkmm-3.0-dev \  
libgtkmm-3.0-doc \  
libgtk-3-doc \  
eclipse-cdt \  
clang \  
&& apt-get -qq clean  
  
RUN useradd -m -U user  
  
USER user  
WORKDIR /home/user  
CMD /usr/bin/eclipse  

