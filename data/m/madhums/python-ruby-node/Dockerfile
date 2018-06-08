# Pull base image.  
FROM buildpack-deps:trusty  
  
# Install.  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y build-essential && \  
apt-get install -y software-properties-common && \  
apt-get install -y byobu curl git htop man unzip vim wget && \  
rm -rf /var/lib/apt/lists/*  
  
# Install Ruby.  
RUN \  
apt-add-repository ppa:brightbox/ruby-ng && \  
apt-get update && \  
apt-get install -y ruby2.2 && \  
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
printf '\n# Node.js\nexport PATH="node_modules/.bin:$PATH"' >> /root/.bashrc  
  
# Define working directory.  
WORKDIR /data  
  
# Define default command.  
CMD ["bash"]  

