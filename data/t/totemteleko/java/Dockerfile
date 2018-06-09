#  
# Java Dockerfile  
#  
# Pull base image.  
FROM ubuntu:12.04  
MAINTAINER Roberto Jimenez totemteleko@gmail.com  
  
# Install Python-properties  
RUN apt-get update && apt-get install python-software-properties -y  
  
# Install Java.  
RUN \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
apt-add-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java7-installer  
  
# Define default command.  
CMD ["bash"]  
  

