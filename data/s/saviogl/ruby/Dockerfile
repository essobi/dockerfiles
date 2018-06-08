FROM saviogl/ruby:2.1.2-1.14.6  
# Define Node version  
ARG NODE_VERSION=v6.11.1  
ARG NPM_VERSION=5.3.0  
ARG YARN_VERSION=1.2.1  
# Fetch nodejs  
RUN wget -O /tmp/node-$NODE_VERSION.tar.gz
http://nodejs.org/dist/$NODE_VERSION/node-$NODE_VERSION.tar.gz  
RUN tar -C /tmp -xvf /tmp/node-$NODE_VERSION.tar.gz && \  
chmod +x /tmp/node-$NODE_VERSION.tar.gz  
# Compile nodejs  
RUN cd /tmp/node-$NODE_VERSION/ && \  
./configure && \  
make -j$(nproc) && \  
make install  
  
# Clean up after ourselves  
RUN rm -rf /tmp/node-$NODE_VERSION*  
  
# Update npm and install yarn  
RUN npm install npm@$NPM_VERSION && \  
rm -rf rm -rf /usr/local/lib/node_modules && \  
mv node_modules /usr/local/lib && \  
npm install --global yarn@$YARN_VERSION  

