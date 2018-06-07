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
RUN wget -O /tmp/go-server.deb http://download.go.cd/gocd-deb/go-
server-14.2.0-377.deb  
RUN dpkg -i /tmp/go-server.deb  
RUN rm /tmp/go-server.deb  
  
EXPOSE 8153  
EXPOSE 8154  
CMD ["/etc/init.d/go-server", "start"]  
CMD /etc/init.d/go-server start && tail -f /var/log/go-server/go-server.log  

