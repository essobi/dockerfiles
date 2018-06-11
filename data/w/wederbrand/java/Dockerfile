# Java 8  
#  
# VERSION 1.0  
FROM wederbrand/base  
MAINTAINER Andreas Wederbrand andreas@wederbrand.se  
  
# Accept oracle license  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | debconf-set-selections  
  
# Add source repositories  
RUN add-apt-repository ppa:webupd8team/java  
RUN apt-get update  
RUN apt-get install -y oracle-java8-installer  
RUN apt-get install -y maven  
  
# Remove useless files  
RUN rm -rf /var/lib/apt/lists/*  
RUN rm -rf /var/cache/oracle-jdk8-installer  
  
# set JAVA_HOME  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
USER root  
CMD bash  

