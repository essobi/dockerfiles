##  
#  
# Dockerfile for Node.js v 0.10.x  
#  
##  
FROM sunnybhanot/ubuntu  
  
# Versions  
ENV NODE_VERSION 0.10.40  
# Install  
RUN apt-get update -y \  
&& apt-get install -y \  
libssl-dev \  
&& apt-get clean \  
&& wget http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.gz \  
&& tar -xzf node-v$NODE_VERSION-linux-x64.tar.gz -C /usr/local \--strip-
components=1 \  
&& rm node-v$NODE_VERSION-linux-x64.tar.gz \  
&& npm install -g npm \  
&& npm cache clear  
  
# Set Enviroment Variable  
ENV HOME /root  
  
# Working directory  
WORKDIR /root  
  
# Default Command  
CMD ["node"]  

