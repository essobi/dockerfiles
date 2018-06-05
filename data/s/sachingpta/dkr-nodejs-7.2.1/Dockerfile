# Set the base image sachingpta/dkr-python3.4.3  
FROM sachingpta/dkr-python3.4.3  
# Author or maintainer of this image file  
MAINTAINER Sachin Gupta <sachin.aut@gmail.com>  
  
# Define working directory.  
WORKDIR /data  
  
# Define default command.  
CMD ["bash"]  
  
# All packages must work in noninteractive mode.  
ENV DEBIAN_FRONTEND noninteractive  
RUN export DEBIAN_FRONTEND=noninteractive  
  
#-------------------------------------------------------------------  
# Install & check node.js 7.2.1 & npm 4.1.1 (integrated with node.js)  
#-------------------------------------------------------------------  
# Setup enviornment variables  
ENV NODE_VERSION 7.2.1  
RUN export NODE_VERSION=7.2.1  
  
# Install Node.js  
RUN \  
cd /tmp && \  
wget https://github.com/nodejs/node/archive/v$NODE_VERSION.zip && \  
apt-get install p7zip-full && \  
7z x v$NODE_VERSION.zip && \  
rm -rf v$NODE_VERSION.zip && \  
cd node-$NODE_VERSION && \  
./configure && \  
CXX="g++ -Wno-unused-local-typedefs" make -j4 && \  
CXX="g++ -Wno-unused-local-typedefs" make install && \  
cd /tmp && \  
rm -rf /tmp/node-$NODE_VERSION && \  
npm install -g npm && \  
printf '\n# Node.js\nexport PATH="node_modules/.bin:$PATH"' >> /root/.bashrc  
  
RUN node -v  
RUN npm -v  
  
#-------------------------------------------------------------------  
# Cleanup Actions  
#-------------------------------------------------------------------  
# Remove redundant apt-get packages and all update information of packages to
reduce image size  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

