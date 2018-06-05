## -*- docker-image-name: "local/java-dev" -*-  
FROM debian:jessie  
ENV java_version 8  
LABEL java_version="$java_version"  
MAINTAINER Aleksandra Fedorova <alpha@bookwar.info>  
RUN echo "deb http://ftp.de.debian.org/debian/ jessie-backports main" >
/etc/apt/sources.list.d/backports.list  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y wget
&& apt-get clean  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y
openjdk-$java_version-jdk && apt-get clean  
RUN update-alternatives --set java /usr/lib/jvm/java-$java_version-openjdk-
amd64/jre/bin/java  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y -t
jessie-backports gradle && apt-get clean  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y
protobuf-compiler && apt-get clean  
  

