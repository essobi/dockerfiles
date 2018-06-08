FROM fedora:23  
RUN dnf -y install \  
git \  
make \  
gcc \  
gcc-c++  
  
RUN cd /usr/local/src && \  
git clone https://github.com/automatak/dnp3.git  
  
RUN dnf -y install \  
cmake \  
asio-devel \  
findutils  
  
RUN cd /usr/local/src/dnp3 && \  
cmake -DDEMO=true . && \  
make -j3  
  
RUN cd /usr/local/src/dnp3 && \  
cp outstation-demo /usr/local/bin  
  
EXPOSE 20000  
ENTRYPOINT /usr/local/bin/outstation-demo  

