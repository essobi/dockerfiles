FROM magruschinske/thesis-netperf-java  
MAINTAINER mathias.gruschinske@gmail.com  
  
RUN apt-get update && \  
apt-get install -y build-essential autoconf libtool git pkg-config && \  
apt-get clean  
  
RUN git clone https://github.com/grpc/grpc /var/local/git/grpc  
  
RUN cd /var/local/git/grpc && \  
git submodule update --init && \  
make && \  
make install && make clean  
  
RUN cd /var/local/git/grpc/third_party/protobuf && \  
make && make install && make clean  

