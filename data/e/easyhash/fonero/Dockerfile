FROM ubuntu:xenial  
  
# Get needed packages  
RUN apt-get update \  
&& apt-get install -y build-essential cmake libboost-all-dev libssl-dev pkg-
config git g++ make libzmq3-dev  
  
# Create app directory  
RUN mkdir -p /daemon && mkdir -p /daemon/data && mkdir -p /daemon  
  
# Install Daemon  
WORKDIR /daemon/  
RUN git clone https://github.com/fonero-project/fonero.git src  
WORKDIR /daemon/src/  
RUN make -j 3  
  
RUN mv /daemon/src/build/release/bin/* /daemon && rm -rf /daemon/src  
  
EXPOSE 19734 19735  
WORKDIR /daemon/  

