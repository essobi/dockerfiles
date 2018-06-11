FROM ubuntu:trusty  
MAINTAINER Daniel Vera  
  
ENV MALLOC_PER_THREAD 1  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y gcc make libjemalloc-dev zlib1g-dev wget g++ netpbm  
  
RUN cd /root  
RUN wget -O-
ftp://ftp.broadinstitute.org/pub/crd/DiscovarDeNovo/latest_source_code/LATEST_VERSION.tar.gz
| tar zx  
RUN cd discovardenovo-* && ./configure && make && make install  
RUN mkdir /ddn  
  
WORKDIR /ddn  
  
ENTRYPOINT ["DiscovarDeNovo"]  

