FROM debian:wheezy  
  
MAINTAINER Romain Fihue <romain.fihue@gmail.com>  
  
RUN apt-get update > /dev/null  
  
RUN apt-get install -y wget openjdk-7-jdk  
  
RUN wget -O /tmp/go-agent.deb http://download.go.cd/gocd-deb/go-
agent-14.4.0-1356.deb  
  
RUN apt-get install -y unzip git  
  
RUN dpkg -i /tmp/go-agent.deb  
  
RUN ln -s /dev/stdout /var/log/go-agent/go-agent.log  
  
ADD go-agent /etc/default/go-agent  
  
CMD /usr/share/go-agent/agent.sh  
  

