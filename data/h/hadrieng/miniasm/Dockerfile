FROM hadrieng/docker_base  
  
MAINTAINER Hadrien Gourlé <gourlehadrien@gmail.com>  
  
# install minimap  
RUN git clone https://github.com/lh3/minimap2 && \  
cd minimap2 && \  
make && \  
cd ..  
  
# install miniasm  
RUN git clone https://github.com/lh3/miniasm && \  
cd miniasm && \  
make && \  
cd ..  
  
ENV PATH /minimap2:/miniasm:$PATH  

