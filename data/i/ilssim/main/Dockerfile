FROM ilssim/cppcheck-sql:latest  
RUN apt-get -y update && apt-get install -y --no-install-recommends \  
wget \  
unzip && \  
wget --no-check-certificate
https://github.com/google/protobuf/releases/download/v3.0.0-beta-3/protobuf-
cpp-3.0.0-beta-3.zip && \  
unzip protobuf-cpp-3.0.0-beta-3.zip && \  
cd protobuf-3.0.0-beta-3/ && \  
./configure && \  
make && \  
make install && \  
cd .. && \  
rm -rf protobuf-cpp-3.0.0-beta-3* && \  
apt-get remove -y wget unzip && \  
rm -rf /var/lib/apt/lists/*  

