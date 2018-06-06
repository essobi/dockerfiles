  
# Ubuntu 14.04 LTS  
# Oracle Java 1.8.0_11 64 bit  
# Maven 3.0.5-1  
# Jenkins 1.643  
# Nano 2.2.6-1ubuntu1  
FROM ubuntu:14.04  
# forked from Chris' Repo  
MAINTAINER Chad Reed (chad_n_reed@homedepot.com)  
  
# setup proxy variables  
ENV QA_PROXY_HOST=str-www-proxy2-qa.homedepot.com  
ENV QA_PROXY_PORT=8080  
# install apps  
RUN apt-get update && apt-get install -y \  
wget \  
gradle \  
git \  
nano \  
curl \  
libxml-xpath-perl \  
build-essential \  
nodejs \  
npm  
# && curl -sL https://deb.nodesource.com/setup | sudo bash - && \  
# apt-get install -yq nodejs  
RUN npm config set strict-ssl false && npm install -g npm  
  
# Install Go  
RUN \  
mkdir -p /goroot && \  
curl https://storage.googleapis.com/golang/go1.6.1.linux-amd64.tar.gz | tar
xvzf - -C /goroot --strip-components=1  
  
# Set environment variables.  
ENV GOROOT /goroot  
ENV GOPATH /gopath  
ENV PATH $GOROOT/bin:$GOPATH/bin:$PATH  
  
# download certificates  
RUN mkdir certificates  
RUN wget https://www.entrust.com/root-certificates/entrust_g2_ca.cer -O
certificates/entrust_g2_ca.cer --no-check-certificate  
  
# set shell variables for java installation  
ENV java_version 1.8.0_11  
ENV filename jdk-8u11-linux-x64.tar.gz  
ENV downloadlink http://download.oracle.com/otn-
pub/java/jdk/8u11-b12/$filename  
  
# download java, accepting the license agreement  
RUN wget --no-cookies --header "Cookie: oraclelicense=accept-securebackup-
cookie" -O /tmp/$filename $downloadlink \--no-check-certificate  
  
# unpack java  
RUN mkdir /opt/java-oracle && tar -zxf /tmp/$filename -C /opt/java-oracle/  
ENV JAVA_HOME /opt/java-oracle/jdk$java_version  
ENV PATH $JAVA_HOME/bin:$PATH  
  
# configure symbolic links for the java and javac executables  
RUN update-alternatives --install /usr/bin/java java $JAVA_HOME/bin/java 20000
&& update-alternatives --install /usr/bin/javac javac $JAVA_HOME/bin/javac
20000  
  
# download and install cf client  
RUN wget https://cli.run.pivotal.io/stable?release=linux64-binary -O
/tmp/cf.tgz --no-check-certificate  
RUN tar zxf /tmp/cf.tgz -C /usr/bin && chmod 755 /usr/bin/cf  
  
# install gradle  
ENV GRADLE_HOME /usr/share/gradle  
  
# configure git  
RUN git config --global http.sslcainfo "$PWD/certificates/entrust_g2_ca.cer"  
RUN git config --global http.proxy "$QA_PROXY_HOST:$QA_PROXY_PORT"  
RUN git config --global url."https://".insteadOf git://  
  
# install nodejs  
#RUN curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -  
#RUN ln -s -f /usr/bin/nodejs /usr/bin/node  
# configure npm  
RUN npm config set proxy http://$QA_PROXY_HOST:$QA_PROXY_PORT  
RUN npm config set https-proxy http://$QA_PROXY_HOST:$QA_PROXY_PORT  
RUN npm config set registry
https://npm.artifactory.homedepot.com/artifactory/api/npm/npm  
  
# install Bower  
RUN npm install -g bower  
  
#install gulp  
RUN npm install -g gulp  
  
# ENV http_proxy="http://$QA_PROXY_HOST:$QA_PROXY_PORT"  
# ENV https_proxy="http://$QA_PROXY_HOST:$QA_PROXY_PORT"  
# install cf zero-downtime-push plugin  
RUN git config --global http.sslVerify false && go get
github.com/concourse/autopilot && git config --global http.sslVerify true  
RUN cf install-plugin $GOPATH/bin/autopilot -f  
  
# # set maven to save dependencies  
# RUN mvn org.apache.maven.plugins:maven-dependency-plugin:2.8:get
-Dartifact=org.hibernate:hibernate-entitymanager:3.4.0.GA:jar:sources  
# RUN mvn org.apache.maven.plugins:maven-dependency-plugin:2.8:get
-Dartifact=org.apache.maven.plugins:maven-clean-plugin:2.5:jar:sources  
# RUN mvn org.apache.maven.plugins:maven-dependency-plugin:2.8:get
-Dartifact=org.apache.maven.surefire:surefire-booter:2.10:jar:sources  
# install jq  
RUN curl -o /usr/local/bin/jq -L
https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64 \  
&& chmod +x /usr/local/bin/jq  
  
# Define default command.  
CMD ["bash"]  

