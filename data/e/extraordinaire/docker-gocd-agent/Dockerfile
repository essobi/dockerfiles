FROM ubuntu:13.10  
MAINTAINER Andrei Serdeliuc, andrei@apikot.com  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu saucy main universe" >
/etc/apt/sources.list  
RUN apt-get -y update && apt-get -y upgrade  
RUN apt-get install -y wget openjdk-7-jre-headless curl unzip git subversion
mercurial  
  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64  
  
RUN wget -O /tmp/go-agent.deb
http://download01.thoughtworks.com/go/13.4.1/ga/go-agent-13.4.1-18342.deb  
RUN dpkg -i /tmp/go-agent.deb  
RUN rm /tmp/go-agent.deb  
  
RUN sed -r -i "s/^(GO_SERVER)=(.*)/\1=\$SERVER_PORT_8153_TCP_ADDR/g"
/etc/default/go-agent  
  
VOLUME ["/var/lib/go-agent"]  
  
CMD /usr/lib/jvm/java-7-openjdk-amd64/bin/java -jar /usr/share/go-agent/agent-
bootstrapper.jar $SERVER_PORT_8153_TCP_ADDR $SERVER_PORT_8153_TCP_PORT  

