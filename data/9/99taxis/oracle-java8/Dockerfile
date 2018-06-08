FROM phusion/baseimage:0.9.17  
MAINTAINER "Fabio Hisamoto" <fhisamoto@gmail.com>  
  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
echo "deb http://dl.bintray.com/sbt/debian /" | tee -a
/etc/apt/sources.list.d/sbt.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 642AC823 && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-add-repository -y ppa:andrei-pozolotin/maven3 && \  
apt-get update && \  
apt-get install -y postgresql-client oracle-java8-installer maven3 sbt unzip
&& \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  

