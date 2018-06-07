FROM phusion/baseimage:0.9.19  
MAINTAINER Wessel Pieterse <jimfromsa<at>gmail<dot>com>  
  
#Install required packages  
RUN apt-get update && apt-get install -y \  
git \  
screen \  
automake \  
autoconf \  
pkg-config \  
libcurl4-openssl-dev \  
libjansson-dev \  
libssl-dev \  
libgmp-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /opt  
  
#Clone the repo  
RUN git clone https://github.com/zcoinofficial/cpuminer-xzc  
  
WORKDIR /opt/cpuminer-xzc  
  
#Build the miner  
RUN ./autogen.sh && ./configure CFLAGS="-march=native" \--with-crypto --with-
curl && make  
  
#Commands to run  
CMD screen ./cpuminer -a lyra2z -o stratum+tcp://$URL -u $USERNAME -p
$PASSWORD  

