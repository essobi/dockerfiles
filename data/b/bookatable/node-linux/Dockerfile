FROM bookatable/aws-cli-linux:latest  
MAINTAINER Bookatable - Mobile <mobile.devs@bookatable.com>  
  
# Latest Node Version  
ENV NODE_VERSION v4.4.3  
# Install Dependencies  
RUN apt-get update && \  
apt-get install -y \  
libkrb5-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Download and install Node  
RUN \  
NODE_ARCHIVE_FILENAME=node-$NODE_VERSION && \  
NODE_URL=http://nodejs.org/dist/$NODE_VERSION/$NODE_ARCHIVE_FILENAME.tar.gz &&
\  
cd /tmp && \  
wget $NODE_URL && \  
tar -xvzf $NODE_ARCHIVE_FILENAME.tar.gz && \  
cd $NODE_ARCHIVE_FILENAME && \  
./configure --prefix=/opt/node && \  
make && \  
mkdir -p /opt/node && \  
make install && \  
cd /tmp && \  
rm -rf $NODE_ARCHIVE_FILENAME && \  
echo 'export PATH=/opt/node/bin:$PATH' >> .bashrc  
  
# Set Node Path  
ENV PATH /opt/node/bin:$PATH  
  
# Install NPM  
RUN \  
npm config set registry http://registry.npmjs.org/ && \  
npm install -g npm && \  
npm cache clear && \  
rm -rf /tmp/* /var/tmp/*  
  
# Print Installed Node and NPM Version  
RUN \  
NODE_AND_NPM_VERSION="Node Version: "$(node --version)", NPM Version: "$(npm
--version) && \  
echo $NODE_AND_NPM_VERSION  
  
WORKDIR /  

