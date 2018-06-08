# Ubuntu 14.04 LTS  
# Oracle Java 1.8.0_11 64 bit  
# Maven 3.2.2  
# Jenkins 1.574  
# git 1.9.1  
# Nano 2.2.6-1ubuntu1  
# extend the most recent long term support Ubuntu version  
FROM ubuntu:14.04.5  
MAINTAINER Asim Khawaja. Based on the image Stephen L. Reed (http://texai.org,
stephenreed@yahoo.com)  
  
# this is a non-interactive automated build - avoid some warning messages  
ENV DEBIAN_FRONTEND noninteractive  
# prepping for mongod  
RUN sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10  
#running non-standard install for ubuntu to work  
RUN echo "deb http://downloads-distro.mongodb.org/repo/debian-sysvinit dist
10gen" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.0.list  
  
# update dpkg repositories  
RUN apt-get update  
  
# installing nodejs  
RUN apt-get install --fix-missing -y curl  
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -  
RUN apt-get install -y nodejs  
  
RUN npm install -g gulp@3.9.1  
  
# install wget  
RUN apt-get install -y wget  
  
# get maven 3.2.2  
RUN wget --no-verbose -O /tmp/apache-maven-3.2.2.tar.gz
http://archive.apache.org/dist/maven/maven-3/3.2.2/binaries/apache-
maven-3.2.2-bin.tar.gz  
  
# verify checksum  
RUN echo "87e5cc81bc4ab9b83986b3e77e6b3095 /tmp/apache-maven-3.2.2.tar.gz" |
md5sum -c  
  
# install maven  
RUN tar xzf /tmp/apache-maven-3.2.2.tar.gz -C /opt/  
RUN ln -s /opt/apache-maven-3.2.2 /opt/maven  
RUN ln -s /opt/maven/bin/mvn /usr/local/bin  
RUN rm -f /tmp/apache-maven-3.2.2.tar.gz  
ENV MAVEN_HOME /opt/maven  
  
# install git  
RUN apt-get install -y git  
  
# install nano  
RUN apt-get install -y nano  
  
# remove download archive files  
RUN apt-get clean  
  
# set shell variables for java installation  
ENV java_version 1.8.0_11  
ENV filename jdk-8u11-linux-x64.tar.gz  
ENV downloadlink http://download.oracle.com/otn-
pub/java/jdk/8u11-b12/$filename  
  
# download java, accepting the license agreement  
RUN wget --no-cookies --header "Cookie: oraclelicense=accept-securebackup-
cookie" -O /tmp/$filename $downloadlink  
  
# unpack java  
RUN mkdir /opt/java-oracle && tar -zxf /tmp/$filename -C /opt/java-oracle/  
ENV JAVA_HOME /opt/java-oracle/jdk$java_version  
ENV PATH $JAVA_HOME/bin:$PATH  
  
# configure symbolic links for the java and javac executables  
RUN update-alternatives --install /usr/bin/java java $JAVA_HOME/bin/java 20000
&& update-alternatives --install /usr/bin/javac javac $JAVA_HOME/bin/javac
20000  
  
# installing python 3.5 for boto and amazon push  
RUN apt-get install -y software-properties-common python-software-properties  
RUN add-apt-repository -y ppa:fkrull/deadsnakes  
RUN apt-get update  
RUN apt-get install -y python3.5  
  
#installing pip  
RUN wget -O /tmp/get-pip.py https://bootstrap.pypa.io/get-pip.py  
RUN python /tmp/get-pip.py

