FROM ubuntu:14.04  
MAINTAINER Dong-hee Na <corona10@gmail.com>  
RUN apt-get update  
RUN apt-get install -y build-essential  
RUN apt-get install -yq automake git cmake ninja-build ccache libncurses5-dev
liblzma-dev libreadline-dev libgmp3-dev libmpfr-dev autoconf libtool python-
dev texlive-extra-utils clang libssl-dev libsqlite3-dev pkg-config libbz2-dev  
RUN apt-get install git  
RUN git clone https://github.com/dropbox/pyston.git ~/pyston  
RUN mkdir ~/pyston_deps  
RUN git clone https://github.com/llvm-mirror/llvm.git ~/pyston_deps/llvm-trunk  
RUN git clone https://github.com/llvm-mirror/clang.git ~/pyston_deps/llvm-
trunk/tools/clang  
RUN cd ~/pyston && git config --global user.email "docker@pyston.com" && git
config --global user.name "docker"  
RUN cd ~/pyston && git submodule update --init --recursive build_deps &&make
llvm_up && make pyston_release  

