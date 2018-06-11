FROM hadrieng/docker_base  
  
MAINTAINER Hadrien Gourlé <gourlehadrien@gmail.com>  
  
#installs scythe  
RUN git clone https://github.com/vsbuffalo/scythe.git && \  
cd scythe && \  
make all && \  
cd ..  
  
#installs sickle  
RUN git clone https://github.com/najoshi/sickle.git && \  
cd sickle && \  
make && \  
cd ..  
  
#installs velvet  
RUN git clone https://github.com/dzerbino/velvet.git && \  
cd velvet && \  
make 'MAXKMERLENGTH=301' && \  
cd ..  
  
#adds scythe and sickle to the path  
ENV PATH /scythe:/sickle:/velvet:$PATH  

