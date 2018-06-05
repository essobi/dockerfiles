FROM bradegler/base-ubuntu  
MAINTAINER Brad Egler "begler@gmail.com"  
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
echo '\n# Node.js\nexport PATH="node_modules/.bin:$PATH"' >>
/root/.bash_profile  
  
RUN npm install -g grunt gulp ember-cli broccoli-cli  
  
# Define mountable directories.  
VOLUME ["/data"]  
  
# Define working directory.  
WORKDIR /data  
  
# Define default command.  
CMD ["/bin/bash"]  

