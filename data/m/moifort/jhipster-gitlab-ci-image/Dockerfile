# DOCKER-VERSION 1.8.2  
FROM ubuntu:trusty  
MAINTAINER Thibaut Mottet <thibaut.mottet@gmail.com>  
  
ENV JAVA_VERSION 8  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
ENV MAVEN_VERSION 3.3.9  
ENV MAVEN_HOME /usr/share/maven  
ENV PATH "$PATH:$MAVEN_HOME/bin"  
ENV NODEJS_VERSION 5.x  
ENV YEOMAN_VERSION 1.5.0  
ENV BOWER_VERSION 1.7.1  
ENV GRUNT_VERSION 0.1.13  
ENV GULP_VERSION 3.9.0  
# install utilities  
RUN apt-get -y install nano git sudo zip bzip2 fontconfig curl unzip  
  
# install java8  
RUN echo 'deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main' >>
/etc/apt/sources.list && \  
echo 'deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main' >>
/etc/apt/sources.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C2518248EEA14886 && \  
apt-get update && \  
echo oracle-java${JAVA_VERSION}-installer shared/accepted-oracle-license-v1-1
select true | sudo /usr/bin/debconf-set-selections && \  
apt-get install -y --force-yes --no-install-recommends oracle-
java${JAVA_VERSION}-installer oracle-java${JAVA_VERSION}-set-default  
  
# install maven  
RUN curl -fsSL
http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C /usr/share \  
&& mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
# install node.js  
RUN curl -sL https://deb.nodesource.com/setup_${NODEJS_VERSION} | sudo bash -  
RUN apt-get install -y nodejs python g++ build-essential  
  
# install yo  
RUN npm install -g yo@${YEOMAN_VERSION}  
  
# install bower  
RUN npm install -g bower@${BOWER_VERSION}  
  
# install grunt  
RUN npm install -g grunt-cli@${GRUNT_VERSION}  
  
# install gulp  
RUN npm install -g gulp@${GULP_VERSION}  
  
# add .m2 dependecies  
ADD static/.m2 /root/.m2  
  
# add node_modules dependecies  
ADD static/node_modules /root/node_modules  
  
WORKDIR /data  

