  
# LICENSE MIT License 2015  
#  
# Jeferson de Sá DOCKER FILES For JAVA 7 instalation  
# -----------------------------------------  
# This is the Dockerfile for a default installation for Oracle Java 7  
#  
# IMPORTANT  
# -----------------------------------------  
# the files for setup are hosted in my dropbox  
#  
# REQUIRED FILES TO BUILD THIS IMAGE  
# -----------------------------------------  
# (1) Oracle Java SE Development Kit 7 for Linux x64  
#  
#  
# HOW TO BUILD THIS IMAGE  
# -----------------------------------------  
# Put all downloaded files in the same directory as this Dockerfile  
# Run:  
# $ sudo docker build -t jefersonbsa/docker-java-7 .  
#  
# AUTHOR  
# -----------------------------------------  
# Jeferson de Sá <jeferson.bsa@gmail.com>  
# https://br.linkedin.com/in/jefersonsa  
# -----------------------------------------  
# Oracle Java 7 Dockerfile  
#  
# https://github.com/dockerfile/java  
# https://github.com/dockerfile/java/tree/master/oracle-java7  
#  
# Pull base image.  
FROM fedora:latest  
  
  
MAINTAINER Jeferson Sa "jefersonbsa@gmail.com"  
# Update and install  
RUN [ "yum","update","-y"]  
RUN [ "yum", "install", "unzip", "-y" ]  
RUN [ "yum", "install", "wget", "-y" ]  
RUN [ "yum", "install", "binutils.x86_64", "-y" ]  
RUN [ "yum", "install", "gcc.x86_64", "-y" ]  
RUN [ "yum", "install", "gcc-c++.x86_64", "-y" ]  
RUN [ "yum", "install", "glibc.x86_64", "-y" ]  
RUN [ "yum", "install", "glibc.i686", "-y" ]  
RUN [ "yum", "install", "glibc-devel.i686", "-y" ]  
RUN [ "yum", "install", "libaio.x86_64", "-y" ]  
RUN [ "yum", "install", "libaio-devel.x86_64", "-y" ]  
RUN [ "yum", "install", "libgcc.x86_64", "-y" ]  
RUN [ "yum", "install", "libstdc++.x86_64", "-y" ]  
RUN [ "yum", "install", "libstdc++.i686", "-y" ]  
RUN [ "yum", "install", "libstdc++-devel.x86_64", "-y" ]  
RUN [ "yum", "install", "libXext.i686", "-y" ]  
RUN [ "yum", "install", "libXtst.i686", "-y" ]  
RUN [ "yum", "install", "redhat-lsb-core.x86_64", "-y" ]  
RUN [ "yum", "install", "sysstat.x86_64", "-y" ]  
  
#Create folder oracle  
RUN mkdir -p /u01/app/oracle/java  
  
#Work folder  
WORKDIR /u01/app/oracle/java  
  
#Add java to docker  
#ADD jdk-7u79-linux-x64.rpm ./jdk-7u79-linux-x64.rpm  
RUN wget https://dl.dropboxusercontent.com/u/10127753/jdk-7u79-linux-x64.rpm  
  
#Copy with sucess  
RUN echo "jdk copy sucess"  
RUN chmod +x jdk-7u79-linux-x64.rpm  
RUN ls -la /u01/app/oracle/java  
  
# Install Java.  
RUN rpm -Uvh jdk-7u79-linux-x64.rpm  
  
#Remove installer  
RUN rm -rf jdk-7u79-linux-x64.rpm  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME=/usr/lib/jvm/java-7-oracle  
  
ENV PATH=$PATH:$JAVA_HOME/bin  
# Define default command.  
CMD ["bash"]  

