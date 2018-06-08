FROM phusion/baseimage:0.10.0  
MAINTAINER rui@deniable.org  
  
LABEL description="Base image for AFL with LLVM"  
  
WORKDIR ~/WRKDIR  
COPY scripts/tweaks.sh ~/WRKDIR  
COPY scripts/ramdisk.sh ~/WRKDIR  
  
ENV TARGETS ~/TARGETS  
ENV WRKSRC /opt  
ENV DEBIAN_FRONTEND noninteractive  
  
SHELL ["/bin/bash", "-c"]  
  
RUN apt-get update && apt-get -y upgrade && \  
apt-get -y install curl build-essential llvm-4.0 clang-4.0 && \  
update-alternatives --install /usr/bin/clang++ clang++ `which clang++-4.0` 1
&& \  
update-alternatives --install /usr/bin/clang clang `which clang-4.0` 1 && \  
update-alternatives --install /usr/bin/llvm-config llvm-config `which llvm-
config-4.0` 1 && \  
update-alternatives --install /usr/bin/llvm-symbolizer llvm-symbolizer `which
llvm-symbolizer-4.0` 1 && \  
mkdir -p $TARGETS && cd $WRKSRC && \  
curl -L http://lcamtuf.coredump.cx/afl/releases/afl-latest.tgz | tar zxf - &&
\  
cd afl-* && make && cd llvm_mode && make && cd .. && make install && \  
apt-get -qy clean autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
CMD ["/bin/bash"]  

