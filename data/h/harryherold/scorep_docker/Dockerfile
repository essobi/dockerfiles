# Download base image ubuntu  
FROM harryherold/scorep_docker  
  
# Update software repo  
RUN apt-get update  
  
# Install required software  
RUN apt-get -y install \  
pkg-config  
  
RUN git clone https://github.com/pmem/pmdk /tmp/pmdk && \  
cd /tmp/pmdk && make -j4 && \  
make install prefix=/opt/pmdk  
  
ENV PMDK_ROOT /opt/pmdk  
ENV PKG_CONFIG_PATH ${PMDK_ROOT}/lib/pkgconfig  

