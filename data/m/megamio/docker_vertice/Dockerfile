FROM ubuntu:16.04  
MAINTAINER Megam systems <info@megam.io>  
  
ENV DEB_VERSION 1.5.2  
ENV RELEASE testing  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV REPO_URL https://get.megam.io/repo/$DEB_VERSION/ubuntu/16.04/$RELEASE
xenial $RELEASE  
  
RUN buildDeps=' \  
vertice nsqd verticegateway\  
' \  
set -x \  
&& apt-get update \  
&& apt-get -y install software-properties-common git nano supervisor apt-
transport-https wget apt-utils ca-certificates netcat-openbsd \  
&& apt-add-repository "deb [arch=amd64] $REPO_URL" \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 9B46B611 \  
&& apt-get update \  
&& apt-get install -y openjdk-8-jre-headless \  
&& apt-get -y install $buildDeps  
  
EXPOSE 7777 4150 4151 4160 4161 4171 9000  
COPY start.sh /  
  
CMD ["/start.sh"]  

