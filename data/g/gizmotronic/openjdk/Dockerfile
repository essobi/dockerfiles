#  
# OpenJDK 9 Dockerfile  
#  
# Pull base image.  
FROM ubuntu:16.04  
# Install Java.  
RUN \  
apt-get update && \  
apt-get install -y openjdk-9-jdk-headless=9~b114-0ubuntu1 && \  
rm -rf /var/lib/apt/lists/*  
# Define working directory.  
WORKDIR /data  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-9-openjdk-amd64  
# Define default command.  
CMD ["bash"]  

