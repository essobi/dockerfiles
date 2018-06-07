# Copyright 2016 Jiglesgom  
  
FROM ubuntu:trusty  
LABEL maintainer "jiglesgom@gmail.com"  
  
# Install Oracle Java 8  
ENV JAVA_VER 8  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
RUN echo 'deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main' >>
/etc/apt/sources.list && \  
echo 'deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main' >>
/etc/apt/sources.list && \  
apt-key adv --keyserver keyserver.ubuntu.com \--recv-keys C2518248EEA14886 &&
\  
apt-get update && \  
echo oracle-java${JAVA_VER}-installer shared/accepted-oracle-license-v1-1
select true | /usr/bin/debconf-set-selections && \  
apt-get install -y \--force-yes --no-install-recommends oracle-
java${JAVA_VER}-installer oracle-java${JAVA_VER}-set-default && \  
pwd  
  
#install maven  
RUN apt-get update && \  
apt-get install -y \--force-yes --no-install-recommends python-software-
properties && \  
# add-apt-repository ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y \--force-yes --no-install-recommends maven && \  
apt-get install -y \--force-yes --no-install-recommends git && \  
rm -rf /var/lib/apt/lists && \  
pwd  
  
#genera el cache de todas las dependencias maven del springboot y NetflixOSS  
ADD pom.xml /  
RUN mvn verify clean --fail-never  
  
CMD ["mvn", "-version"]

