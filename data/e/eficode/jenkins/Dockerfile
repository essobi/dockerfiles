FROM jenkins:latest  
MAINTAINER Jouni Rajala <jouni.rajala@eficode.com>  
  
# Change as 'root' to continue installation  
USER root  
RUN apt-get update  
  
# Install Oracle's Java 8  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee /etc/apt/sources.list.d/webupd8team-java.list  
RUN echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty
main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886  
RUN apt-get update  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-get install -y oracle-java8-installer  
RUN update-alternatives --set java /usr/lib/jvm/java-8-oracle/jre/bin/java  
  
# Clean Up apt  
RUN rm -rf /var/lib/apt/lists/*  
  
# Change back as 'jenkins'  
USER jenkins  

