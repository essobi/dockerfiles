FROM debian:jessie  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && apt-get install -y git build-essential bison flex && \  
git clone git://git.code.sf.net/p/filebench/code filebench-src && \  
cd filebench-src && \  
git checkout filebench-1.5 && \  
cd /filebench-src && ./configure && \  
make -j4 && \  
apt-get remove --purge -y build-essential wget $(apt-mark showauto) && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
ENTRYPOINT ["/filebench-src/filebench"]  
CMD ["--help"]  

