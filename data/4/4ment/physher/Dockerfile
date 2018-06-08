FROM debian:stretch  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
ca-certificates \  
cmake \  
git \  
libgsl0-dev \  
wget  
  
RUN wget https://github.com/4ment/physher/archive/v1.0.2.tar.gz && tar -xzvf
v1.0.2.tar.gz  
WORKDIR /physher-1.0.2/Release  
RUN cmake -DBUILD_SHARED_LIBS=OFF .. && make && make install  

