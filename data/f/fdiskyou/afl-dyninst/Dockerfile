FROM fdiskyou/afl:0.1  
MAINTAINER rui@deniable.org  
  
# check https://hub.docker.com/u/fdiskyou/ for more information  
ENV WRKSRC /opt  
ENV DEBIAN_FRONTEND noninteractive  
  
SHELL ["/bin/bash", "-c"]  
  
RUN apt-get update && apt-get -y upgrade && \  
apt-get -y install git cmake libelf-dev libelf1 libiberty-dev libboost-all-dev
zlib1g-dev m4 libdw1 && \  
cd $WRKSRC && cd afl-* && ln -s afl-analyze afl && cd $WRKSRC && \  
cd $WRKSRC && git clone https://github.com/dyninst/dyninst.git && \  
cd dyninst && mkdir build && cd build && cmake .. && make && make install && \  
cd $WRKSRC && git clone https://github.com/talos-vulndev/afl-dyninst.git && \  
cd afl-dyninst && ln -s `ls -1d $WRKSRC/afl-* | head -1` afl && make && \  
cp afl-dyninst /usr/local/bin && \  
cp libAflDyninst.so /usr/local/lib && \  
echo "/usr/local/lib" > /etc/ld.so.conf.d/dyninst.conf && ldconfig && \  
apt-get -qy clean autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
ENV DYNINSTAPI_RT_LIB /usr/local/lib/libdyninstAPI_RT.so  
  
CMD ["/bin/bash"]  

