#  
# TreasureBoat.org  
# by ishimoto  
#  
# Oracel Java 8u25 on CentOS 6.6  
#  
# build : docker build -t treasureboat/java:0.6 .  
# run : docker run -d -P --name tbJava8 treasureboat/java:0.6  
FROM treasureboat/ssh:latest  
MAINTAINER treasureboat <office@treasureboat.org>  
  
# download Java8  
RUN wget -q -O /tmp/jdk-8u25-linux-x64.rpm
'https://dl.dropboxusercontent.com/u/1548210/TB/Docker/jdk-8u25-linux-x64.rpm'  
RUN rpm -ivh /tmp/jdk-8u25-linux-x64.rpm  
RUN rm -f /tmp/jdk-8u25-linux-x64.rpm  
  
# export JDK_VERSION=8u25  
ENV JDK_VERSION 8u25  
  
# export JAVA_HOME=/usr/java/default  
ENV JAVA_HOME /usr/java/default  
  
# check Java version  
RUN java -version  

