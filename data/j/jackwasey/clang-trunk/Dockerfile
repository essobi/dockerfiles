# don't acutally need r-devel for R, just all the dependencies.  
FROM rocker/r-devel:latest  
  
RUN apt-get update -qq; exit 0  
RUN apt-get install -t unstable -y --no-install-recommends \  
automake \  
cmake \  
curl \  
fonts-inconsolata \  
git \  
libcurl4-openssl-dev \  
libssh2-1-dev \  
libssl-dev \  
libxml2-dev \  
pandoc \  
pandoc-citeproc \  
qpdf \  
texlive-base  
  
WORKDIR /usr/local/src  
COPY bin/get-llvm* bin/  
RUN bin/get-llvm-svn.sh  
  
RUN mkdir llvm-build \  
&& cd llvm-build \  
&& cmake \  
-DCMAKE_BUILD_TYPE:STRING=Release \  
-DLLVM_TARGETS_TO_BUILD:STRING=host \  
-DCMAKE_INSTALL_PREFIX=/usr/local \  
-DCLANG_DEFAULT_OPENMP_RUNTIME:STRING=libomp \  
../llvm \  
&& make -j6 \  
&& make install \  
&& make clean \  
&& cd .. \  
&& rm -rf llvm-build llvm \  
&& ldconfig  

