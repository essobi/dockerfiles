#  
# Node.js (on top of nginx) Dockerfile  
#  
# https://github.com/InAnimaTe/docker-nginx-nodejs/  
#  
# Pull base image. See it here: http://dockerfile.github.io/#/nginx  
FROM dockerfile/nginx  
  
# Install Python.  
RUN \  
apt-get update && \  
apt-get install -y python python-dev python-pip python-virtualenv && \  
rm -rf /var/lib/apt/lists/*  
  
# Install Node.js  
RUN \  
cd /tmp && \  
wget http://nodejs.org/dist/node-latest.tar.gz && \  
tar xvzf node-latest.tar.gz && \  
rm -f node-latest.tar.gz && \  
cd node-v* && \  
./configure && \  
CXX="g++ -Wno-unused-local-typedefs" make && \  
CXX="g++ -Wno-unused-local-typedefs" make install && \  
cd /tmp && \  
rm -rf /tmp/node-v* && \  
npm install -g npm && \  
echo -e '\n# Node.js\nexport PATH="node_modules/.bin:$PATH"' >> /root/.bashrc  
# Define working directory.  
WORKDIR /data  
  
# Define default command.  
CMD ["bash"]  

