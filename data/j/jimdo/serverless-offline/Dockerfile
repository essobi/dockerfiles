FROM node:6.10  
  
RUN apt-get update && apt-get install -y apt-transport-https  
  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \- && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" >
/etc/apt/sources.list.d/yarn.list && \  
apt-get update && apt-get install -y yarn  
  
RUN \  
echo "===> add webupd8 repository..." && \  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee
/etc/apt/sources.list.d/webupd8team-java.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee -a /etc/apt/sources.list.d/webupd8team-java.list && \  
apt-key adv --keyserver keyserver.ubuntu.com \--recv-keys EEA14886 && \  
apt-get update  
  
RUN echo "===> install Java" && \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \--force-yes oracle-
java8-installer oracle-java8-set-default  
  
RUN echo "===> clean up..." && \  
rm -rf /var/cache/oracle-jdk8-installer && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /usr/src/app  
  
RUN echo "===> install serverless command" && \  
npm install -g serverless && \  
echo "===> install dynamodb package" && \  
cd /usr/src/app && \  
npm install dynamodb-localhost && \  
echo "===> install dynamodb" && \  
node -e "var dynamodbLocal = require('dynamodb-localhost'); \  
dynamodbLocal.install(function() {});" && \  
echo "===> install pm2 monitor" && \  
npm install -g pm2  

