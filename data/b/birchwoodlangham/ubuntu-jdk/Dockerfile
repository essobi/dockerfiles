FROM birchwoodlangham/ubuntu-base:latest  
  
MAINTAINER Tan Quach <tan.quach@birchwoodlangham.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN add-apt-repository -y ppa:webupd8team/java && \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
apt-get update && apt-get -y install oracle-java8-installer maven ant && \  
rm -rf /var/cache/oracle-jdk8-installer && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  

