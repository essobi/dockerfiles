#  
# Java Dockerfile  
#  
# https://github.com/dubture-dockerfiles/java  
#  
# Pull base image.  
FROM stackbrew/ubuntu:13.10  
# Install Java  
RUN apt-get install -y --force-yes software-properties-common  
RUN add-apt-repository -y ppa:webupd8team/java  
RUN apt-get update  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-
set-selections  
RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections  
RUN apt-get install -y --force-yes oracle-java7-installer  
  
# Define default command.  
CMD ["java"]  
  

