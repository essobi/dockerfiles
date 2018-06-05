FROM debian:wheezy  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get install -y build-essential automake make git libcurl4-openssl-dev  
  
WORKDIR /usr/src  
RUN git clone https://github.com/arbedout/cpuminer-multi cpuminer && cd
cpuminer && ./autogen.sh && ./configure CFLAGS="-O3" && make -j4  
  
WORKDIR /usr/src/cpuminer  
CMD ./minerd  

