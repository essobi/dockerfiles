FROM centralping/centos:7  
MAINTAINER Jason Cust <jason@centralping.com>  
  
ENV NODE_VERSION 8.9.1  
ENV NPM_VERSION 5.5.1  
# Add non-root machine user to run node  
# - include home directory for npm history  
# configure and make node and update npm  
RUN useradd -rm node && \  
cd /var/tmp && \  
curl -SLO
"http://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}.tar.gz" && \  
curl -SLO "http://nodejs.org/dist/v${NODE_VERSION}/SHASUMS256.txt" && \  
grep "node-v${NODE_VERSION}.tar.gz\$" SHASUMS256.txt | sha256sum -c - && \  
tar -xzf "node-v${NODE_VERSION}.tar.gz" && \  
cd node-v${NODE_VERSION} && \  
./configure && \  
make && \  
make install && \  
make clean && \  
cd ../ && \  
rm -rf "node-v${NODE_VERSION}" "node-v${NODE_VERSION}.tar.gz" SHASUMS256.txt
&& \  
npm i -g npm@"${NPM_VERSION}" && \  
npm cache clear --force  
  
USER node  
WORKDIR /home/node  
  
CMD ["node"]  

