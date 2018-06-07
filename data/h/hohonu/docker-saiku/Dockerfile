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
RUN wget -O saiku-server-2.6.tar.gz http://meteorite.bi/downloads/saiku-
server-2.6.tar.gz  
RUN tar xvfz saiku-server-2.6.tar.gz  
  
EXPOSE 8080  
CMD ~/saiku-server/start-saiku.sh && tail -f ~/saiku-
server/tomcat/logs/catalina.out  

