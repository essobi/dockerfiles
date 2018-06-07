FROM ubuntu:latest  
MAINTAINER Philip Dodds, philip@hohonu.com  
  
# Get some tools  
RUN \  
sudo apt-get update && sudo apt-get install -y software-properties-common
python-software-properties  
  
RUN \  
sudo apt-get install -y zip  
  
# Install Java.  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/*  
  
# Grab a coy  
RUN wget -O /tmp/go-agent.deb http://download.go.cd/gocd-deb/go-
agent-14.2.0-377.deb  
RUN dpkg -i /tmp/go-agent.deb  
RUN rm /tmp/go-agent.deb  
  
RUN sed -r -i "s/^(GO_SERVER)=(.*)/\1=\$SERVER_PORT_8153_TCP_ADDR/g"
/etc/default/go-agent  
  
VOLUME ["/var/lib/go-agent"]  
  
CMD java -jar /usr/share/go-agent/agent-bootstrapper.jar
$SERVER_PORT_8153_TCP_ADDR $SERVER_PORT_8153_TCP_PORT  

