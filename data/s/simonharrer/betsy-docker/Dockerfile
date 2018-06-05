# This is a Dockerfile to create an image with betsy installed.  
# Version 1.0  
# oracle-jdk-8 required!  
FROM kurron/docker-oracle-jdk-8  
MAINTAINER Simon Harrer (simon.harrer@uni-bamberg.de)  
  
# install all packages  
RUN add-apt-repository ppa:cwchien/gradle &&\  
apt-get update --quiet=2 &&\  
apt-get install --assume-yes git=1:1.9.1-1ubuntu0.3\  
ant=1.9.3-2build1\  
maven=3.0.5-1\  
wget\  
tar\  
openjdk-7-jre:amd64=7u111-2.6.7-0ubuntu0.14.04.3\  
gradle=3.1-0ubuntu1 &&\  
rm --force --recursive /var/lib/apt/lists/*  
  
ENV ANT_HOME=/usr/share/ant  
ENV MAVEN_HOME=/usr/share/maven  
  
# Set environment variables  
# JAVA_HOME set to JDK 8  
ENV JAVA7_HOME=/usr/lib/jvm/java-7-openjdk-amd64/jre  
  
# when copying the Dockerfile in the repo, this is no longer necessary  
# see http://stackoverflow.com/questions/27482504/dockerfile-cannot-access-
git-repo-with-my-private-key  
RUN mkdir --parents ~/.ssh && ssh-keyscan -t rsa github.com >
~/.ssh/known_hosts  
  
# install betsy  
RUN git clone https://github.com/uniba-dsg/betsy && cd betsy && git checkout
efda3910ac81bf191dfc4fa713b0d0388fd14acb  
  
WORKDIR betsy  
  
# build betsy  
RUN gradle installDist  

