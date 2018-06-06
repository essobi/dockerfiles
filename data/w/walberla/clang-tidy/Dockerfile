FROM walberla/buildenv-ubuntu-basic:16.04  
MAINTAINER Sebastian Eibl "sebastian.eibl@fau.de"  
RUN apt-get update && apt-get install -y \  
python \  
gawk \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN cd /usr/local \  
&& curl -L http://llvm.org/releases/3.8.1/clang+llvm-3.8.1-x86_64-linux-gnu-
ubuntu-16.04.tar.xz | tar --strip-components=1 -xJ  
  
ADD ansi2html.sh /usr/local/bin/ansi2html.sh  
ADD run-clang-tidy.py /usr/local/bin/run-clang-tidy.py  
  
ENV CC=clang CXX=clang++  
  
  

