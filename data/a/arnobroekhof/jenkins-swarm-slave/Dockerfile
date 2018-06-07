FROM ubuntu:14.04  
MAINTAINER Arno Broekhof <arnobroekhof@gmail.com>  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && \  
apt-get -y upgrade  
  
RUN apt-get install -y ca-certificates wget xz-utils  
RUN apt-get install -y git subversion  
  
RUN apt-get install -y software-properties-common && \  
add-apt-repository ppa:openjdk-r/ppa && \  
apt-get update && \  
apt-get install -y openjdk-8-jdk  
  
RUN mkdir /apps  
  
RUN wget http://apache.mirror1.spango.com/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.tar.gz -O /tmp/apache-maven-3.3.9-bin.tar.gz && \  
tar xvfz /tmp/apache-maven-3.3.9-bin.tar.gz -C /apps/ && \  
ln -s /apps/apache-maven-3.3.9/bin/mvn /usr/bin/mvn  
  
RUN wget https://nodejs.org/dist/v4.4.4/node-v4.4.4-linux-x64.tar.xz -O
/tmp/node.tar.xz && \  
tar xvf /tmp/node.tar.xz -C /apps/ && \  
ln -s /apps/node-v4.4.4-linux-x64/bin/npm /usr/bin/npm && \  
ln -s /apps/node-v4.4.4-linux-x64/bin/node /usr/bin/node && \  
/usr/bin/npm install -g bower  
  
RUN mkdir /apps/jenkins && \  
wget http://repo.jenkins-ci.org/releases/org/jenkins-ci/plugins/swarm-
client/2.0/swarm-client-2.0-jar-with-dependencies.jar -O /apps/jenkins/swarm-
client.jar  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  

