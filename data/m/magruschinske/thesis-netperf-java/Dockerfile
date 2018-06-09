FROM magruschinske/thesis-netperf  
MAINTAINER mathias.gruschinske@gmail.com  
  
RUN echo 'deb http://httpredir.debian.org/debian/ jessie-backports main
contrib non-free' >> /etc/apt/sources.list  
  
RUN apt-get update && \  
apt-get install -y openjdk-8-jdk && \  
apt-get clean  

