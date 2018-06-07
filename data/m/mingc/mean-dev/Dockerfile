# Build:  
# docker build -t mingc/mean-dev .  
#  
# Run:  
# docker run -it --rm mingc/mean-dev bash  
#  
  
FROM ubuntu:16.04  
  
MAINTAINER Ming Chen  
  
ENV MONGO_VERSION "3.4"  
ENV REDIS_VERSION "3.2.8"  
ENV NODE_VERSION "7.x"  
  
ENV LANG en_US.UTF-8  
RUN locale-gen $LANG  
COPY start.sh /start.sh  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
build-essential \  
curl \  
git \  
net-tools \  
python \  
vim \  
wget && \  
  
# Install mongodb  
# https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
0C49F3730359A14518585931BC711F9BA15703C6 && \  
echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-
org/${MONGO_VERSION} multiverse" | tee /etc/apt/sources.list.d/mongodb-
org-${MONGO_VERSION}.list && \  
apt-get update && \  
apt-get install -y mongodb-org && \  
  
# Install redis  
wget -q http://download.redis.io/releases/redis-${REDIS_VERSION}.tar.gz && \  
tar xzf redis-${REDIS_VERSION}.tar.gz && \  
( cd redis-${REDIS_VERSION} && make && make install ) && \  
rm -fr redis-{$REDIS_VERSION} redis-${REDIS_VERSION}.tar.gz && \  
  
# Install nodejs, npm etc.  
# https://github.com/nodesource/distributions  
curl -sL -k https://deb.nodesource.com/setup_${NODE_VERSION} | bash - && \  
apt-get install -yq nodejs && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
npm install -g npm && \  
npm install --quiet -g npm-check-updates eslint jshint node-gyp gulp bower yo
mocha karma-cli pm2 && \  
npm cache clean  

