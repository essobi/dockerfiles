FROM ubuntu:trusty  
  
ARG DEBIAN_FRONTEND=noninteractive  
RUN apt-get update -y && \  
apt-get install -y mpich cmake libfuse-dev libfuse2 zlib1g-dev man-db tree
graphviz && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* debian/  
  
RUN apt-get update -y && apt-get install -y git  
  
RUN echo "-- Compile and Install PLFS" && \  
git clone \--recursive https://github.com/plfs/plfs-core.git && \  
cd plfs-core && \  
cmake . && \  
make -j24 && \  
make install  
  
ADD entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  

