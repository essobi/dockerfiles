FROM ubuntu:14.04  
MAINTAINER Robin Chen <yenpai.mis@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install JDK 8  
RUN apt-get update && \  
apt-get install -y wget && \  
apt-get clean && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/* && \  
wget --output-document=/tmp/jdk-8.tar.gz \  
\--no-check-certificate --no-cookies \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie" \  
http://download.oracle.com/otn-pub/java/jdk/8u65-b17/jdk-8u65-linux-x64.tar.gz
&& \  
mkdir -p /usr/lib/jvm && \  
tar zxvf /tmp/jdk-8.tar.gz -C /usr/lib/jvm && \  
chown -R root:root /usr/lib/jvm && \  
rm -f /tmp/* && \  
locale-gen en_US.UTF-8  
# Set the environment variables for JDK 8  
ENV JDK_HOME="/usr/lib/jvm/jdk1.8.0_65" \  
JAVA_HOME="/usr/lib/jvm/jdk1.8.0_65" \  
PATH="$PATH:$JAVA_HOME/bin" \  
LANG="en_US.UTF-8" \  
LANGUAGE="en_US:en" \  
LC_ALL="en_US.UTF-8"  

