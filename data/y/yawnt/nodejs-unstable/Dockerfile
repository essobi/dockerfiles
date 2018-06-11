FROM dockerfile/ubuntu  
  
RUN \  
apt-get update && \  
apt-get install -y python python-dev python-pip python-virtualenv imagemagick
&& \  
rm -rf /var/lib/apt/lists/* && \  
cd /tmp && \  
wget http://nodejs.org/dist/v0.11.14/node-v0.11.14.tar.gz && \  
tar xvzf node-v0.11.14.tar.gz && \  
rm -f node-v0.11.14.tar.gz && \  
cd node-v* && \  
./configure && \  
CXX="g++ -Wno-unused-local-typedefs" make && \  
CXX="g++ -Wno-unused-local-typedefs" make install && \  
cd /tmp && \  
rm -rf /tmp/node-v* && \  
npm install -g npm && \  
echo '\n# Node.js\nexport PATH="node_modules/.bin:$PATH"' >> /root/.bashrc  

