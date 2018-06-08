FROM debian:jessie  
  
MAINTAINER FreakErn git@freakern.de  
  
RUN echo 'APT::Install-Recommends "false";' > /etc/apt/apt.conf.d/zz-local-
tame  
RUN apt-get update && apt-get upgrade -y && apt-get install -y git ca-
certificates build-essential autoconf automake pkg-config libssl-dev make
libcurl4-openssl-dev libjansson-dev libgmp-dev  
RUN git clone https://github.com/magi-project/m-cpuminer-v2.git /m-cpuminer-v2  
  
WORKDIR /m-cpuminer-v2  
  
RUN cd /m-cpuminer-v2 && ./autogen.sh && ./configure CFLAGS="-O3"
CXXFLAGS="-O3" && make -j 8  
  
ENTRYPOINT ["/m-cpuminer-v2/m-minerd"]  

