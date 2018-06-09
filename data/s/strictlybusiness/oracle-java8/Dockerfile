FROM debian:wheezy  
MAINTAINER Sean Lynch <techniq35@gmail.com>  
  
# Add Oracle Java repository  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" >
/etc/apt/sources.list.d/webupd8team-java.list  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886  
RUN apt-get update  
  
# Install Oracle Java 8  
RUN echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true" | debconf-set-selections  
RUN apt-get install -y oracle-java8-installer oracle-java8-set-default  
RUN apt-get clean  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  

