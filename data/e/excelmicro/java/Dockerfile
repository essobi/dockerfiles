FROM excelmicro/base:v1.3.0  
MAINTAINER Elizabeth Harper <eharper@excelmicro.com>  
  
# Install java package  
# Add java repository  
RUN apt-get update  
RUN apt-get -y install software-properties-common python-software-properties  
RUN add-apt-repository -y ppa:webupd8team/java  
RUN apt-get update  
  
# automatically accept oracle license  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | debconf-set-selections  
  
# Install java & set the java environment variables for when you "bash -l"  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \  
oracle-java8-installer \  
oracle-java8-set-default  
  
# Remove cached installer files  
RUN rm -rf /var/cache/oracle-jdk8-installer && apt-get clean  
  
# set the JAVA_HOME explicitly  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  

