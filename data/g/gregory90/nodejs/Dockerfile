FROM gregory90/base:latest  
  
ENV NODE_VERSION 6.0.0  
# Install Node.js  
RUN \  
mkdir -p /code && \  
DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y make g++ build-essential
python && \  
cd /tmp && \  
wget http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION.tar.gz && \  
tar xvzf node-v$NODE_VERSION.tar.gz && \  
rm -f node-v$NODE_VERSION.tar.gz && \  
cd node-v* && \  
./configure && \  
CXX="g++ -Wno-unused-local-typedefs" make && \  
CXX="g++ -Wno-unused-local-typedefs" make install && \  
cd /tmp && \  
rm -rf /tmp/node-v* && \  
echo '\n# Node.js\nexport PATH="node_modules/.bin:$PATH"' >>
/root/.bash_profile  
  
RUN npm set progress=false  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

