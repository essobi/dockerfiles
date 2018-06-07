FROM edgecase/docker-ubuntu-node-awscli  
MAINTAINER Lee Goolsbee "lee@edgecase.io"  
# Add ability to install from PPA  
RUN apt-get install -y software-properties-common  
  
# Prepare for Java installation  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | debconf-set-selections  
RUN add-apt-repository -y ppa:webupd8team/java  
  
# Update packages (again)  
RUN apt-get update -y  
  
# Install some packages we need  
RUN apt-get install -y wget oracle-java8-installer maven  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  

