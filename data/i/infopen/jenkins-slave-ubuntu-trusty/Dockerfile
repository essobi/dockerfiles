FROM infopen/ubuntu-trusty-ssh:0.1.0  
MAINTAINER Alexandre Chaussier <a.chaussier@infopen.pro>  
  
# Install base packages  
RUN apt-get update && \  
apt-get install -y openjdk-7-jdk=7u91-2.6.3* \  
git=1:1.9.1*  
  
# Create user for Jenkins  
RUN useradd -m \  
-s /bin/bash \  
jenkins  
  
# Set password for jenkins user  
RUN echo "jenkins:jenkins" | chpasswd  
  

