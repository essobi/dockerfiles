FROM ubuntu:16.04  
RUN apt update && apt -y upgrade  
RUN apt install -y \  
wget \  
build-essential \  
libssl-dev  
RUN wget http://download.joedog.org/siege/siege-latest.tar.gz && \  
tar -zxvf siege-latest.tar.gz && \  
cd siege-*/ && \  
./configure --with-ssl=/usr/bin/openssl && \  
make && make install  
  
ENTRYPOINT ["siege"]  
CMD [""]  

