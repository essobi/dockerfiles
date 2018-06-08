FROM ubuntu  
  
LABEL maintainer="Guilherme Prado <grprado@gmail.com>"  
LABEL description="Ubuntu + Open JDK 8 headless."  
  
# Install Java.  
RUN \  
apt-get update && \  
apt-get install -y openjdk-8-jdk-headless && \  
rm -rf /var/lib/apt/lists/*  

