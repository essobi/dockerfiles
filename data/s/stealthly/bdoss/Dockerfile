FROM ubuntu:precise  
MAINTAINER Joe Stein <joe.stein@stealth.ly>  
  
# Install dependencies  
RUN apt-get install -y wget dnsmasq-base vim curl screen  
  
RUN apt-get install -y software-properties-common python-software-properties  
RUN add-apt-repository -y ppa:webupd8team/java  
RUN apt-get -y update  
RUN /bin/echo debconf shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections  
RUN apt-get -y install oracle-java7-installer oracle-java7-set-default  
  
EXPOSE 9160 9042 2181 9091 5050 8000 8001 8080 45678 4321 5555 80 22 443  

