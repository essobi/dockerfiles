# 1 ubuntu  
# Ubuntu Dockerfile  
#  
# https://github.com/xiongjungit/ubuntu  
#  
# Pull base image.  
FROM daocloud.io/library/ubuntu:latest  
MAINTAINER xiongjun,dockerxman <fenyunxx@163.com>  
  
ADD sources.list /etc/apt/sources.list  
  
# Install.  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y build-essential && \  
apt-get install -y software-properties-common && \  
apt-get install -y byobu curl git htop man unzip vim wget && \  
rm -rf /var/lib/apt/lists/*  
  
# Add files.  
ADD root/.bashrc /root/.bashrc  
ADD root/.gitconfig /root/.gitconfig  
ADD root/.scripts /root/.scripts  
  
# Set environment variables.  
ENV HOME /root  
ENV TZ "Asia/Shanghai"  
ENV TERM xterm  
  
# 2 python  
# Python Dockerfile  
#  
# https://github.com/xiongjungit/python  
#  
# Install Python.  
RUN \  
apt-get update && \  
apt-get install -y python python-dev python-pip python-virtualenv && \  
rm -rf /var/lib/apt/lists/*  
  
# 3 nodejs  
# Node.js Dockerfile  
#  
# https://github.com/xiongjungit/nodejs  
#  
# Install Node.js  
RUN \  
cd /tmp && \  
wget http://npm.taobao.org/mirrors/node/v0.10.40/node-v0.10.40.tar.gz && \  
tar xvzf node-v0.10.40.tar.gz && \  
rm -f node-v0.10.40.tar.gz && \  
cd node-v* && \  
./configure && \  
CXX="g++ -Wno-unused-local-typedefs" make && \  
CXX="g++ -Wno-unused-local-typedefs" make install && \  
cd /tmp && \  
rm -rf /tmp/node-v* && \  
npm config set registry https://registry.npm.taobao.org && \  
npm install -g npm && \  
printf '\n# Node.js\nexport PATH="node_modules/.bin:$PATH"' >> /root/.bashrc  
  
# 4 ghost  
# Ghost Dockerfile  
#  
# https://github.com/xiongjungit/ghost  
#  
# Install Ghost  
RUN \  
cd /tmp && \  
wget http://dl.ghostchina.com/Ghost-0.7.0-zh-full.zip && \  
unzip Ghost-0.7.0-zh-full.zip -d /ghost && \  
rm -f Ghost-0.7.0-zh-full.zip && \  
cd /ghost && \  
npm install --production && \  
sed 's/127.0.0.1/0.0.0.0/' /ghost/config.example.js > /ghost/config.js && \  
useradd ghost --home /ghost  
  
# Add files.  
ADD start.bash /ghost-start  
  
# Set environment variables.  
ENV NODE_ENV production  
  
# Define mountable directories.  
VOLUME ["/data", "/ghost-override"]  
  
# Define working directory.  
WORKDIR /ghost  
  
# Define default command.  
CMD ["bash", "/ghost-start"]  
  
# Expose ports.  
EXPOSE 2368  

