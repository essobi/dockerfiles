FROM stackbrew/ubuntu:saucy  
MAINTAINER frio "http://frio.name"  
# Install Java  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install --no-install-recommends
openjdk-7-jre-headless default-jre-headless  
RUN DEBIAN_FRONTEND=noninteractive apt-get clean  
  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64  

