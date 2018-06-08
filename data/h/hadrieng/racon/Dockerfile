FROM hadrieng/docker_base  
  
MAINTAINER Hadrien Gourlé <gourlehadrien@gmail.com>  
  
# install minimap2  
RUN git clone https://github.com/lh3/minimap2 && \  
cd minimap2 && \  
make && \  
cd ..  
  
# cmake 3.2  
RUN wget http://www.cmake.org/files/v3.2/cmake-3.2.2.tar.gz && \  
tar xf cmake-3.2.2.tar.gz && \  
cd cmake-3.2.2 && \  
./configure && \  
make && \  
make install  
  
# install racon  
RUN git clone \--recursive https://github.com/isovic/racon.git && \  
cd racon && \  
mkdir build && \  
cd build && \  
cmake -DCMAKE_BUILD_TYPE=Release .. && \  
make  
  
ENV PATH /minimap2:/racon/build/bin:$PATH  

