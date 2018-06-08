FROM ubuntu:15.10  
  
ENV DEBIAN_FRONTEND=noninteractive  
# Install base utilities  
RUN apt-get update && apt-get install -y software-properties-common python-
software-properties git build-essential  
# Install Java.  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk7-installer  
  
RUN \  
echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
apt-get update && \  
apt-get install -y oracle-java7-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk7-installer  
  
#define env var for 7 and 8.  
ENV JAVA_7_HOME /usr/lib/jvm/java-7-oracle  
ENV JAVA_8_HOME /usr/lib/jvm/java-8-oracle  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle  
# Install Deps  
RUN dpkg --add-architecture i386 && apt-get update && apt-get install -y
--force-yes expect git wget libc6-i386 lib32stdc++6 lib32gcc1 lib32ncurses5
lib32z1 python curl  
  
# Cleaning  
RUN apt-get clean  
WORKDIR ~  

