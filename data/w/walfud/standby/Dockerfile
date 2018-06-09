FROM ubuntu:16.04  
MAINTAINER walfud "walfud@aliyun.com"  
# Configuration  
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  
  
# Install Utils  
RUN apt-get update  
  
RUN apt-get install -y vim \  
unzip \  
xz-utils \  
cron \  
git \  
tree  
  
RUN apt-get install -y iputils-ping \  
wget \  
curl \  
openssh-server  
  
# Java  
RUN apt-get install -y openjdk-8-jdk  
  
# Nodejs  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& apt-get install -y nodejs  
  
# Mongo  
ENV LC_ALL C  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927 \  
&& echo "deb http://repo.mongodb.com/apt/ubuntu xenial/mongodb-enterprise/3.2
multiverse" | tee /etc/apt/sources.list.d/mongodb-enterprise.list \  
&& apt-get update \  
&& apt-get install -y --allow-unauthenticated mongodb-enterprise  
  
EXPOSE 22 23 80 443  
VOLUME /root  
WORKDIR /  

