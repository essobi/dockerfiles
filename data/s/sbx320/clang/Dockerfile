FROM buildpack-deps:xenial  
RUN apt-get update && apt-get install -y software-properties-common  
RUN add-apt-repository -s "deb http://apt.llvm.org/xenial/ llvm-toolchain-
xenial main" && \  
wget -O - http://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add -  
  
RUN apt-get update && apt-get install -y clang-4.0 && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Setup clang as default compiler  
ENV CC clang-4.0  
ENV CXX clang++-4.0  
RUN ln -s /usr/bin/clang-4.0 /bin/cc &&\  
ln -s /usr/bin/clang++-4.0 /bin/cxx  
  

