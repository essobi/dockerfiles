# Ubuntu 15.10 with Openjdk-8-jre-headless  
FROM ubuntu:15.10  
MAINTAINER Sebastien LANGOUREAUX <linuxworkgroup@hotmail.com>  
  
# Update distro and install OpenJDK8-jre-headless  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install openjdk-8-jre-headless -y && \  
apt-get install locales -y && \  
update-locale LANG=C.UTF-8 LC_MESSAGES=POSIX && \  
locale-gen en_US.UTF-8 && \  
dpkg-reconfigure locales && \  
apt-get clean all && \  
rm -rf /var/lib/apt/lists/*  
  
  
  

