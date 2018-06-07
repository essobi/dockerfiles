# Pull base image.  
FROM ubuntu:14.04  
MAINTAINER Ismail CHAIDA <chaida.ismail@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install dev tools: jdk, git etc...  
RUN apt-get update -y  
  
RUN apt-get install -y build-essential unzip curl git-core  
  
# Fix: add-apt-repository command not found  
RUN apt-get install software-properties-common -y  
RUN apt-get install python-software-properties -y  
  
RUN add-apt-repository ppa:webupd8team/java -y  
RUN apt-get update -y  
  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | sudo /usr/bin/debconf-set-selections  
RUN apt-get install -y oracle-java8-installer  
RUN sudo apt-get install -y oracle-java8-set-default  
  
RUN apt-get update -y  
  
RUN rm -rf /var/lib/apt/lists/*  
RUN rm -rf /var/cache/oracle-jdk8-installer  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
# Define working directory.  
RUN mkdir -p /usr/local  
WORKDIR /usr/local  
  
# Define default command.  
CMD ["bash"]

