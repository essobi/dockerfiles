FROM ocaml/opam:debian-stable_ocaml-4.02.3  
# AFL Dockerfile obtained from:  
# https://github.com/ozzyjohnson/docker-afl/blob/master/Dockerfile  
# MAINTAINER Ozzy Johnson <docker@ozzy.io>  
# and merged with the OCaml setup  
RUN sudo -u opam sh -c "opam remote add ocl https://github.com/ocamllabs/opam-
repo-dev.git" && \  
sudo -u opam sh -c "opam switch 4.02.3+afl" && \  
sudo -u opam sh -c "opam depext -u utop mirage" && \  
sudo -u opam sh -c "opam install -y -j 2 -v utop mirage"  
ENV AFL_INSTALL http://lcamtuf.coredump.cx/afl/releases/afl-latest.tgz  
ENV LIBJPEG_TURBO_INSTALL svn://svn.code.sf.net/p/libjpeg-
turbo/code/branches/1.4.x  
RUN \  
sudo apt-get update \  
\--quiet \  
&& sudo apt-get install \  
\--yes \  
\--no-install-recommends \  
\--no-install-suggests \  
autoconf \  
automake \  
gcc \  
libtool \  
make \  
nasm \  
subversion \  
wget \  
&& sudo apt-get clean \  
&& sudo rm -rf /var/lib/apt/lists/*  
WORKDIR /tmp  
RUN \  
wget \  
$AFL_INSTALL \  
\--no-verbose \  
&& mkdir afl-src \  
&& tar -xzf afl-latest.tgz \  
-C \  
afl-src \  
\--strip-components=1 \  
&& cd afl-src \  
&& sed -i 's/^\/\/ #define USE_64BIT/#define USE_64BIT/gI' config.h \  
&& make \  
&& sudo make install \  
&& rm -rf \  
/tmp/afl-latest.tgz \  
/tmp/afl-src  
RUN \  
svn \  
-q \  
co \  
$LIBJPEG_TURBO_INSTALL \  
libjpeg-turbo \  
&& cd libjpeg-turbo \  
&& autoreconf -fiv \  
&& CC=/usr/local/bin/afl-gcc ./configure \  
&& make -j`getconf _NPROCESSORS_ONLN` \  
&& sudo make install \  
&& rm -rf /tmp/libjpeg-turbo  
VOLUME ["/data"]  
WORKDIR /data  

