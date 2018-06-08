FROM phusion/baseimage:0.10.0  
MAINTAINER rui@deniable.org  
  
LABEL description="Base image for Z3"  
  
ENV WRKSRC /opt  
ENV DEBIAN_FRONTEND noninteractive  
  
SHELL ["/bin/bash", "-c"]  
  
RUN apt-get update && apt-get -y upgrade && \  
apt-get -y install python build-essential git llvm-4.0 clang-4.0 && \  
cd $WRKSRC && \  
git clone https://github.com/Z3Prover/z3 && \  
cd z3 && CXX=clang++ CC=clang python scripts/mk_make.py && \  
cd build && make && make install && \  
# Create ``z3`` user for container with password ``z3``.  
useradd -m z3 && \  
echo z3:z3 | chpasswd && usermod -aG sudo z3 && \  
cd $WRKSRC && chown -R z3:z3 z3 && \  
rm -rf /var/lib/apt/lists/*  
  
USER z3  
WORKDIR /home/z3  
  
CMD ["/bin/bash"]  

