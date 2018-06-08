FROM anapsix/docker-oracle-java8  
  
MAINTAINER Javier Ortiz <javier.ortiz.78@gmail.com>  
  
#Install sudo  
RUN apt-get update && apt-get -y install sudo  
RUN useradd -m docker && echo "docker:docker" | chpasswd && adduser docker
sudo  
  
#Uninstall OpenJDK  
RUN sudo apt-get purge openjdk-7-jre openjdk-6-jre-headless  
  
#Install tools  
RUN sudo apt-get -y install maven mercurial git

