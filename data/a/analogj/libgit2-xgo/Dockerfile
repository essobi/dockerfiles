# Go cross compiler (xgo): Wildcard layer to the latest Go release  
# Copyright (c) 2014 Péter Szilágyi. All rights reserved.  
#  
# Released under the MIT license.  
FROM karalabe/xgo-1.8.x  
  
MAINTAINER Jason Kulatunga <jason@thesparktree.com>  
  
WORKDIR /scripts  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
cmake \  
clang-3.6 \  
mingw-w64-tools \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /usr/local/osx-ndk-x86/tools  
  
#RUN git clone https://go.googlesource.com/go /usr/local/go-1.5 && \  
# cd /usr/local/go-1.5/src && \  
# GOROOT_BOOTSTRAP=/usr/local/go ./make.bash  
#ENV PATH /usr/local/go-1.5/bin:$PATH  
COPY . /scripts/  
  
COPY toolchains/osx/osxcross-macports /usr/local/osx-ndk-x86/tools  
  
RUN /scripts/build.sh  
  
ENTRYPOINT []

