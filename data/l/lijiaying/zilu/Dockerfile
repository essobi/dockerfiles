FROM lijiaying/klee:2.9  
MAINTAINER lijiaying <lijiaying1989@gmail.com>  
  
# FIXME: Docker doesn't currently offer a way to  
# squash the layers from within a Dockerfile so  
# the resulting image is unnecessarily large!  
ENV klee_home=/klee_home \  
zilu_src=/zilu_home  
  
RUN apt-get -y --no-install-recommends install \  
libgsl0-dev \  
z3 libz3-dev \  
clang vim  
  
#mkdir -p ${zilu_src}  
# Copy across source files needed for build  
#git clone https://github.com/lijiaying/ZILU.git ${zilu_src}  
ADD / ${zilu_src}  
  
#RUN git clone https://github.com/lijiaying/ZILU.git ${zilu_src} && \  
RUN cd ${klee_home}/klee && \  
git apply ${zilu_src}/patch/klee.6609a03.patch && \  
export PATH=$PATH:/klee_home/llvm-gcc4.2-2.9-x86_64-linux/bin && \  
export C_INCLUDE_PATH=/usr/include/x86_64-linux-gnu && \  
export CPLUS_INCLUDE_PATH=/usr/include/x86_64-linux-gnu && \  
make ENABLE_OPTIMIZED=1 -j && \  
make install && \  
make clean  
  
RUN cd ${zilu_src} && \  
rm -rf test/*.cpp && \  
rm -rf tmp/* && \  
mkdir -p build && \  
cd build && \  
rm -rf * && \  
mkdir -p parser && \  
cd parser && \  
rm -rf * && \  
cmake ../../parser && \  
make  
#> /dev/null 2>&1 || mv parser.hpp .. && \  
#cd .. && \  
#rm -rf build  
#RUN cd ${zilu_src} && \  
# export PATH=$PATH:/klee_home/llvm-gcc4.2-2.9-x86_64-linux/bin && \  
# ./run benchmark/03.cfg && \  
# ./run benchmark/07.cfg  

