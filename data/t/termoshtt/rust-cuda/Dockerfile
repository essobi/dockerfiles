FROM nvidia/cuda:9.1-devel AS cuda9.1-llvm6.0  
RUN apt-get update && apt-get install -y \  
git \  
curl \  
zlib1g-dev \  
&& curl https://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add - \  
&& echo "deb http://apt.llvm.org/xenial/ llvm-toolchain-xenial-6.0 main" >
/etc/apt/sources.list.d/llvm.list \  
&& apt-get update \  
&& apt-get install -y \  
llvm-6.0 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y --default-toolchain nightly  
ENV PATH $PATH:/root/.cargo/bin  
RUN cargo install xargo cargo-check cargo-expand  
RUN rustup component add rust-src rustfmt-preview  
  
RUN chown -R root:users /root && chmod -R 770 /root  
ENV LIBRARY_PATH "/usr/local/cuda/lib64:/usr/local/cuda/lib64/stubs"  
ENV LD_LIBRARY_PATH "/usr/local/cuda/lib64:/usr/local/cuda/lib64/stubs"  
RUN mkdir -p /source  
WORKDIR /source  
  
FROM cuda9.1-llvm6.0 AS cuda9.1  
RUN bash -c 'for e in $(ls /usr/bin/ll*-6.0); do mv $e ${e%-6.0}; done'  

