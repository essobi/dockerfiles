FROM evarga/jenkins-slave  
MAINTAINER Pablo Orviz <orviz@ifca.unican.es>  
  
USER root  
  
RUN apt-get update  
RUN apt-get -y install git maven checkstyle  
  
RUN apt-get -y install software-properties-common  
RUN add-apt-repository -y ppa:openjdk-r/ppa  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EB9B1D8886F44E2A  
RUN apt-get update  
RUN apt-get -y install openjdk-8-jdk openjdk-8-jre g++  
  
RUN update-alternatives --set java /usr/lib/jvm/java-8-openjdk-
amd64/jre/bin/java  
RUN update-alternatives --set javac /usr/lib/jvm/java-8-openjdk-
amd64/bin/javac  

