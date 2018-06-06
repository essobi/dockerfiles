FROM ubuntu:14.04  
MAINTAINER neko1990 <neko1990@gmail.com>  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
  
## work around in Mainland China  
# RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak  
# ADD sources.list /etc/apt/sources.list  
  
RUN apt-get update \  
&& apt-get install -y \  
clang-3.3 llvm-3.3-dev dragonegg-4.7 \  
gcc-4.7 gfortran-4.7 \  
autoconf automake build-essential libtool \  
ruby-ronn \  
python python-matplotlib python-jinja2 python-pygraphviz python-sklearn
python-numpy python-networkx python-pip \  
google-perftools libgoogle-perftools-dev numactl dc \  
unzip \  
&& pip install pulp \  
&& ln -s /usr/bin/llvm-config-3.3 /usr/local/bin/llvm-config \  
&& ln -s /usr/lib/x86_64-linux-gnu/libgfortran.so.3 /usr/lib/libgfortran.so  
  
# clean up  
RUN apt-get autoclean \  
&& apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /opt  
RUN curl -L https://github.com/benchmark-subsetting/cere/archive/master.zip -o
/tmp/cere.zip \  
&& unzip -uo /tmp/cere.zip -d /opt/  
RUN cd cere-master && ./autogen.sh \  
&& ./configure \  
\--with-dragonegg=/usr/lib/gcc/x86_64-linux-gnu/4.7/plugin/dragonegg.so \  
CC=gcc-4.7 \  
&& make && make check  

