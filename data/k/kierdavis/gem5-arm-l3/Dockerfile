FROM kierdavis/gem5-arm:latest  
  
RUN apt-get install -y patch  
  
ADD l3cache.patch /tmp/l3cache.patch  
RUN patch --directory /opt/gem5 -p1 < /tmp/l3cache.patch && \  
rm /tmp/l3cache.patch  
  
RUN cd /opt/gem5 && \  
scons build/ARM/gem5.opt -j$(nproc)  

