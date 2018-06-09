#  
# Scala and sbt Dockerfile  
#  
# Pull base image  
FROM openjdk:8-jdk  
MAINTAINER Pratim Chaudhuri <pratim.chaudhuri@barclays.com>  
  
ENV SCALA_VERSION 2.12.2  
ENV SBT_VERSION 0.13.15  
# Install SBT  
RUN apt-get update -y \  
&& apt-get install -y apt-transport-https apt-utils \  
&& echo "deb https://dl.bintray.com/sbt/debian /" | tee -a
/etc/apt/sources.list.d/sbt.list \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
2EE0EA64E40A89B84B2DF73499E82A75642AC823 \  
&& apt-get update -y \  
&& apt-get install -y sbt python3 python3-pip \  
&& sbt sbt-version \  
&& apt-get clean  
  
# Install AWS CLI  
RUN pip3 install --upgrade --user awscli  

