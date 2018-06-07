# Docker file containing minimal build environment for gradle Java8 project  
# with front-end tools. Image contains:  
# - ubuntu 16.04  
# - oracle-java8  
# - mysql server  
# - git  
# - gradle  
# - nodejs  
# - npm  
# - node-gyp  
  
FROM ubuntu:16.04  
  
RUN { \  
echo debconf debconf/frontend select Noninteractive; \  
echo mysql-community-server mysql-community-server/data-dir select ''; \  
echo mysql-community-server mysql-community-server/root-pass password ''; \  
echo mysql-community-server mysql-community-server/re-root-pass password ''; \  
echo mysql-community-server mysql-community-server/remove-test-db select true;
\  
echo debconf shared/accepted-oracle-license-v1-1 select true; \  
} | debconf-set-selections && \  
apt-get update -y && \  
apt-get upgrade -y && \  
apt-get install -y software-properties-common && \  
add-apt-repository ppa:webupd8team/java -y && \  
apt-get update -y && \  
apt-get install -y oracle-java8-installer && \  
apt-get install -y mysql-server && \  
apt-get install -y git && \  
apt-get install -y gradle && \  
apt-get install -y nodejs && \  
apt-get install -y npm && \  
apt-get install -y curl && \  
apt-get clean && \  
npm install -g node-gyp  

