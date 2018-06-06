FROM ubuntu  
MAINTAINER Yasith Lokuge <yasith@cobweb.io>  
  
  
  
#######################  
#### Install Java8 ####  
#######################  
RUN \  
  
apt-get update && \  
apt-get install -y software-properties-common && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get upgrade -y && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
#########################  
#### Install Tomcat8 ####  
#########################  
# Define working directory.  
WORKDIR /home  
  
RUN \  
  
apt-get install -y wget && \  
apt-get update && \  
apt-get install -y git-core && \  
mkdir cobweb && \  
cd cobweb && \  
git clone https://github.com/CobwebIO/tomcat8.git && \  
cd tomcat8/webapps && \  
mv ROOT root_ && \  
cd /home/cobweb/tomcat8 && \  
mkdir logs  
  
  
  
# Define default command.  
CMD ["bash"]  
  
ENV CATALINA_HOME /home/cobweb/tomcat8  
ENV PATH $PATH:$CATALINA_HOME/bin  
  
EXPOSE 80  
EXPOSE 8009  
##########################  
#### Install OrientDB ####  
##########################  
WORKDIR /home/cobweb  
  
RUN \  
  
git clone https://github.com/CobwebIO/orientdb.git  
  
EXPOSE 2480  
EXPOSE 2424  
###########################  
#### Install Mosquitto ####  
###########################  
WORKDIR /home/cobweb  
  
RUN \  
  
apt-get install -y build-essential && \  
apt-get install -y libssl-dev && \  
apt-get install -y libcurl4-openssl-dev && \  
apt-get install -y libc-ares-dev && \  
apt-get install -y uuid-dev && \  
git clone https://github.com/CobwebIO/mosquitto.git && \  
cd mosquitto && \  
make binary && \  
make install  
  
EXPOSE 1883  
#########################  
#### Download Cobweb ####  
#########################  
WORKDIR /home/cobweb  
  
RUN \  
  
git clone https://github.com/CobwebIO/Deploy.git && \  
cd Deploy && \  
cp cobweb.war /home/cobweb/tomcat8/webapps && \  
mv /home/cobweb/tomcat8/webapps/cobweb.war
/home/cobweb/tomcat8/webapps/ROOT.war  
  
EXPOSE 5683  
#######################  
##### bootstrap #######  
#######################  
RUN \  
  
echo "cd /home/cobweb/tomcat8/bin" >> /root/.bashrc && \  
echo "sh ./shutdown.sh" >> /root/.bashrc && \  
echo "sh ./startup.sh" >> /root/.bashrc && \  
echo "cd /home/cobweb/orientdb/bin" >> /root/.bashrc && \  
echo "sh ./orientdb.sh start" >> /root/.bashrc && \  
echo "mosquitto -d -c /home/cobweb/mosquitto/mosquitto.conf" >> /root/.bashrc
&& \  
echo "cd /home/cobweb/Deploy" >> /root/.bashrc && \  
echo "java -jar CoAP-1.0-jar-with-dependencies.jar &" >> /root/.bashrc && \  
echo "sleep 10" >> /root/.bashrc && \  
echo "java -jar /home/cobweb/Deploy/Mqtt-1.0-jar-with-dependencies.jar &" >>
/root/.bashrc  
  
CMD ["bash"]

