FROM ubuntu:14.04  
  
MAINTAINER Sion Smith sion.smith@gmail.com  
  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu precise main"
|\  
tee -a /etc/apt/sources.list  
RUN echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu precise
main" |\  
tee -a /etc/apt/sources.list  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886  
RUN apt-get update  
RUN apt-get -y upgrade  
  
# auto accept oracle jdk license  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true |\  
/usr/bin/debconf-set-selections  
RUN apt-get -y install oracle-java8-installer  
RUN apt-get clean  
RUN update-alternatives --display java  
  
# add JAVA_HOME to path.  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  

