FROM ingeus/ubuntu-base  
MAINTAINER Stephen Masters <steve@scattercode.co.uk>  
  
# Add a repo where OpenJDK can be found.  
RUN apt-get install -y software-properties-common  
RUN add-apt-repository -y ppa:webupd8team/java  
RUN apt-get update  
  
# Auto-accept the Oracle JDK license  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | sudo /usr/bin/debconf-set-selections  
  
RUN apt-get install -y oracle-java8-installer  
  
#set environment variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  

