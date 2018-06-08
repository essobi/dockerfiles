FROM ubuntu:14.04  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee -a /etc/apt/sources.list  
RUN echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty
main" | tee -a /etc/apt/sources.list  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 && apt-
get update && apt-get install -y curl dnsutils oracle-java8-installer ca-
certificates  

