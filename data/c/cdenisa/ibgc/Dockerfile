FROM ubuntu:latest  
  
RUN apt-get -y update && \  
apt-get -y dist-upgrade && \  
# Install prerequisities  
apt-get -y install software-properties-common unzip && \  
# Install java  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get -y update && \  
apt-get -y install oracle-java8-installer && \  
# Install IB Gateway (to ~/Jts)  
wget https://download2.interactivebrokers.com/installers/ibgateway/stable-
standalone/ibgateway-stable-standalone-linux-x64.sh && \  
chmod +x ibgateway-stable-standalone-linux-x64.sh && \  
./ibgateway-stable-standalone-linux-x64.sh -q && \  
#wget -O ~/Jts/jts.ini http://cdn.quantconnect.com/interactive/ibgateway-
latest-standalone-linux-x64-v968.2d.jts.ini && \  
rm ibgateway-stable-standalone-linux-x64.sh && \  
# Install IB Controller (to /opt/IBController)  
wget http://github.com/ib-controller/ib-
controller/releases/download/3.4.0/IBController-3.4.0.zip && \  
unzip IBController-3.4.0.zip -d /opt/IBController && \  
chmod -R 777 /opt/IBController && \  
rm IBController-3.4.0.zip && \  
# Clean up  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* && rm -rf /var/cache/oracle-jdk8-installer  
  

