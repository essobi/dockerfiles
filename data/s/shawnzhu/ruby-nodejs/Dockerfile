FROM shawnzhu/ruby  
  
RUN apt-get update  
  
# from http://stackoverflow.com/questions/13018626/  
RUN apt-get install -y python-software-properties git curl socat wget sudo  
  
# from https://github.com/dockerfile/nodejs/blob/master/Dockerfile  
# Install Node.js  
RUN \  
cd /tmp && \  
curl -O http://nodejs.org/dist/v0.10.40/node-v0.10.40.tar.gz && \  
tar xvzf node-v0.10.40.tar.gz && \  
rm -f node-v0.10.40.tar.gz && \  
cd node-v* && \  
./configure && \  
CXX="g++ -Wno-unused-local-typedefs" make && \  
CXX="g++ -Wno-unused-local-typedefs" make install && \  
cd /tmp && \  
rm -rf /tmp/node-v* && \  
npm install -g npm && \  
echo -e '\n# Node.js\nexport PATH="node_modules/.bin:$PATH"' >> /root/.bashrc  

