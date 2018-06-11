FROM ubuntu:15.04  
MAINTAINER Tiago Cogumbreiro  
  
ENV WHY3_VER 0.86.1  
# Install base software  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y \  
gcc \  
make \  
git \  
curl \  
ocaml \  
pkg-config \  
libgmp10 \  
libgmp-dev \  
libgtksourceview2.0 \  
libgtksourceview2.0-dev \  
menhir \  
libzip-ocaml \  
libzip-ocaml-dev \  
liblablgtksourceview2-ocaml \  
liblablgtksourceview2-ocaml-dev && \  
cd /tmp && curl -L
https://gforge.inria.fr/frs/download.php/file/34797/why3-$WHY3_VER.tar.gz |
tar zx && \  
cd /tmp/why3-$WHY3_VER && \  
./configure --prefix=/usr/local && \  
make && \  
make install && \  
rm -rf /tmp/why3-$WHY3_VER && \  
apt-get autoremove -y \  
m4 \  
libc6-dev \  
make \  
libgmp-dev \  
manpages-dev \  
gcc \  
make \  
git \  
curl \  
pkg-config \  
libgtksourceview2.0-dev \  
dbus \  
libzip-ocaml-dev \  
liblablgtksourceview2-ocaml-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  

