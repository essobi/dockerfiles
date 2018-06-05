FROM docker.io/java:openjdk-8-jdk  
  
ENV ACTIVATOR_VER 1.3.12  
RUN cd /opt && \  
apt-get -y update && \  
apt-get -y upgrade && \  
apt-get -y install unzip && \  
apt-get -y install wget && \  
apt-get -y install git  
  
RUN cd /opt && \  
wget http://downloads.typesafe.com/typesafe-
activator/${ACTIVATOR_VER}/typesafe-activator-${ACTIVATOR_VER}.zip && \  
unzip typesafe-activator-${ACTIVATOR_VER}.zip && \  
ln -s /opt/activator-dist-${ACTIVATOR_VER} /opt/activator && \  
rm -f /opt/typesafe-activator-${ACTIVATOR_VER}.zip  
  
ENV PATH $PATH:/opt/activator/bin  
  
EXPOSE 9000 8888  
RUN mkdir /app  
  
WORKDIR /app  
  
# Define an entry point.  
CMD ["activator", "testProd"]  

