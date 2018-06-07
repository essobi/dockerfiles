FROM dockerfile/python  
  
# Install Node.js  
RUN \  
cd /tmp && \  
wget http://nodejs.org/dist/v0.10.30/node-v0.10.30.tar.gz && \  
tar xvzf node-v0.10.30.tar.gz && \  
rm -f node-v0.10.30.tar.gz && \  
cd node-v* && \  
./configure && \  
CXX="g++ -Wno-unused-local-typedefs" make && \  
CXX="g++ -Wno-unused-local-typedefs" make install && \  
cd /tmp && \  
rm -rf /tmp/node-v*  
  
  
VOLUME ["/shared"]  
  
# Define working directory.  
WORKDIR /shared

